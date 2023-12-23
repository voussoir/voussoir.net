import argparse
import collections
import math
import pynmea2
import shutil
import sqlite3
import sys
import traceback
import typing

from voussoirkit import betterhelp
from voussoirkit import pathclass
from voussoirkit import pipeable
from voussoirkit import sqlhelpers
from voussoirkit import vlogging
from voussoirkit import windrives

log = vlogging.getLogger(__name__, 'columbus_ingest')

DEVICE_ID = 'columbusp10'
GPX_FOLDER = pathclass.Path('D:\\Documents\\GPX')
NMEA_FOLDER = GPX_FOLDER.with_child('NMEA')

class Trkpt:
    def __init__(
            self,
            *,
            device_id,
            unixtime,
            lat,
            lon,
            provider,
            accuracy,
            ele,
            sat,
        ):
        self.device_id = device_id
        self.unixtime = unixtime
        self.lat = lat
        self.lon = lon
        self.provider = provider
        self.accuracy = accuracy
        self.ele = ele
        self.sat = sat

    @classmethod
    def from_ggarmc(cls, *, device_id, gga, rmc):
        if not gga:
            return None

        if not rmc:
            return None

        try:
            gga.latitude
            gga.longitude
        except ValueError:
            return None

        try:
            rmc.datetime
        except TypeError:
            return None

        if gga.latitude == 0 or gga.longitude == 0:
            return None

        return cls(
            device_id=device_id,
            provider='gps',
            lat=gga.latitude,
            lon=gga.longitude,
            sat=int(gga.num_sats),
            accuracy=gga.horizontal_dil,
            ele=gga.altitude,
            unixtime=rmc.datetime.timestamp() * 1000,
        )

def nmea_to_ggarmc(nmea_sentences: typing.Iterable[str]) -> tuple:
    '''
    Given a stream of NMEA sentences, yield tuples of (GGA, RMC) messages,
    grouped by their timestamp.
    '''
    time_of_day = None
    gga = None
    rmc = None

    for sentence in nmea_sentences:
        sentence = sentence.strip()
        log.loud(sentence)
        try:
            message = pynmea2.parse(sentence, check=True)
        except pynmea2.nmea.ParseError as exc:
            log.error(traceback.format_exc())
            continue

        if time_of_day is not None and time_of_day != message.timestamp:
            yield (gga, rmc)
            gga = None
            rmc = None

        time_of_day = message.timestamp

        if message.sentence_type == 'GGA':
            gga = message

        if message.sentence_type == 'RMC':
            rmc = message

def nmea_to_trkpts(nmea_sentences: typing.Iterable[str], device_id: str) -> typing.Generator:
    '''
    Given a stream of NMEA sentences, yield Trkpts, ignoring invalid fixes.
    '''
    for (gga, rmc) in nmea_to_ggarmc(nmea_sentences):
        trkpt = Trkpt.from_ggarmc(gga=gga, rmc=rmc, device_id=device_id)
        if trkpt is not None:
            yield trkpt

def haversine_distance(origin, destination):
    '''
    Thank you Martin Thoma
    https://stackoverflow.com/a/38187562/5430534
    '''
    (lat1, lon1) = origin
    (lat2, lon2) = destination
    earth_radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    kilometers = earth_radius * c
    meters = kilometers * 1000

    return meters

def remove_identical_points(trkpts: typing.Iterable[Trkpt]) -> typing.Generator:
    '''
    Remove points that have identical lat/lon to the previous point.
    These duplicates tend to occur while indoors and imply that the device was
    unable to get a new fix, so it reused its previous one.

    I consider this to be an essential filter since identical points are so
    useless.
    '''
    previous_trkpt = None
    keep_trkpts = []

    original_count = 0
    filtered_count = 0
    for trkpt in trkpts:
        original_count += 1
        if previous_trkpt is None:
            pass
        elif previous_trkpt.lat == trkpt.lat and previous_trkpt.lon == trkpt.lon:
            continue
        yield trkpt
        previous_trkpt = trkpt
        filtered_count += 1
    log.debug('Kept %d out of %d (removed %d).', filtered_count, original_count, original_count - filtered_count)

def remove_stationary_points(trkpts, window_size, meters):
    '''
    Remove points when the sum displacement over `window_size` subsequent points
    is less than `meters`.
    '''
    deq = collections.deque(maxlen=window_size)
    original_count = 0
    filtered_count = 0
    previous_trkpt = None
    for trkpt in trkpts:
        original_count += 1
        if previous_trkpt is not None:
            deq.append(haversine_distance((previous_trkpt.lat, previous_trkpt.lon), (trkpt.lat, trkpt.lon)))
        if len(deq) == window_size and sum(deq) < meters:
            continue
        previous_trkpt = trkpt
        yield trkpt
        filtered_count += 1
    log.debug('Kept %d out of %d (removed %d).', filtered_count, original_count, original_count - filtered_count)

def prep_sql():
    sql = sqlite3.connect(GPX_FOLDER.with_child(f'trkpt_{DEVICE_ID}.db').absolute_path)
    # sql = sqlite3.connect('trkpt_g8xa.db')
    sql.execute('''
    CREATE TABLE IF NOT EXISTS trkpt(
        device_id INTEGER NOT NULL,
        time INTEGER NOT NULL,
        lat REAL NOT NULL,
        lon REAL NOT NULL,
        provider TEXT,
        accuracy REAL,
        ele INTEGER,
        sat INTEGER,
        PRIMARY KEY(device_id, time)
    )
    ''')
    sql.execute('CREATE INDEX IF NOT EXISTS index_trkpt_device_id_time on trkpt(device_id, time)')
    sql.commit()
    return sql

def ingest_file(sql, file):
    log.info('Reading %s.', file.absolute_path)
    trkpts = nmea_to_trkpts(file.readlines('r'), device_id=DEVICE_ID)
    trkpts = remove_identical_points(trkpts)
    trkpts = remove_stationary_points(trkpts, window_size=5, meters=3)
    trkpts = list(trkpts)

    cur = sql.cursor()
    for trkpt in trkpts:
        pairs = {
            'device_id': trkpt.device_id,
            'time': trkpt.unixtime,
            'lat': trkpt.lat,
            'lon': trkpt.lon,
            'provider': 'gps',
            'accuracy': trkpt.accuracy,
            'ele': trkpt.ele,
            'sat': trkpt.sat,
        }
        (qmarks, bindings) = sqlhelpers.insert_filler(pairs)
        cur.execute(f'INSERT OR IGNORE INTO trkpt {qmarks}', bindings)

    log.info('Imported %d points.', len(trkpts))
    sql.commit()

def columbus_ingest():
    '''
    Ingest files straight from the mounted Columbus P-10.
    '''
    folder = None
    drives = windrives.get_drive_map()
    for (mount, info) in drives.items():
        if info.get('name').upper() == 'COLUMBUSP10':
            folder = pathclass.Path(mount)

    if folder is None:
        log.fatal('COLUMBUSP10 is not mounted.')
        return 1

    files = [
        file for file in folder.walk()
        if file.extension == 'txt' and
        file.basename not in {'CONFIG.TXT', 'INFO.TXT'}
    ]

    sql = prep_sql()

    for file in files:
        # The columbus is quite slow as a storage device, and reading the
        # mb-sized NMEA files takes quite a few seconds. So we start by
        # checking the first valid point to see if we recognize this file.
        first_trkpt = next(nmea_to_trkpts(file.readlines_generator('r'), device_id=DEVICE_ID))
        copied_basename = str(int(first_trkpt.unixtime)) + '_' + file.replace_extension('nmea').basename
        copied = NMEA_FOLDER.with_child(copied_basename)
        if copied.exists:
            log.info('Skipping %s.', file.absolute_path)
            continue

        ingest_file(sql, file)

        # This time, the file is cached by the operating system so I don't mind
        # calling read again.
        # Note that this copy is made even after the sql commit, so if anything
        # had gone wrong before now, we would not have made the copy file and
        # would not skip it during the next ingest.
        copied.write('wb', file.read('rb'))

    return 0

def ingest_selected_files(files):
    '''
    Ingest these files, whether or not they were already imported previously.
    This is helpful when deliberately re-importing a file.
    '''
    sql = prep_sql()
    for file in files:
        ingest_file(sql, file)
    return 0

def columbus_ingest_argparse(args):
    if args.nmea_patterns:
        files = list(pathclass.glob_many_files(args.nmea_patterns))
        return ingest_selected_files(files)
    else:
        return columbus_ingest()

@vlogging.main_decorator
def main(argv):
    parser = argparse.ArgumentParser(
        description='''
        ''',
    )
    parser.add_argument(
        'nmea_patterns',
        help='''
        Ingest a specific file, instead of reading the mounted Columbus.
        ''',
        nargs='*',
    )
    parser.set_defaults(func=columbus_ingest_argparse)

    return betterhelp.go(parser, argv)

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
