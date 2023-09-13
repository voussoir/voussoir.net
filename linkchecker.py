import argparse
import bs4
import collections
import requests
import sys
import urllib.parse

from voussoirkit import dotdict
from voussoirkit import niceprints
from voussoirkit import progressbars
from voussoirkit import vlogging

log = vlogging.get_logger(__name__, 'linkchecker')
vlogging.get_logger('urllib3').setLevel(vlogging.SILENT)

REDIRECT_CODES = {301, 302, 303, 307}

session = requests.Session()
session.headers['User-Agent'] = 'voussoir.net link health checker'

class BrokenAnchor(Exception):
    pass

def extract_links(url, soup):
    links = set()
    for a in soup.select('a[href]'):
        if not a['href'].startswith('#'):
            links.add(a['href'])

    for img in soup.select('img[src]'):
        links.add(img['src'])

    for audio in soup.select('audio[src]'):
        links.add(audio['src'])

    for video in soup.select('video[src]'):
        links.add(video['src'])

    links = {urllib.parse.urljoin(url, link) for link in links}
    links = {link for link in links if not ignore_link(link)}
    links = {normalize_link(link) for link in links}
    return links

def ignore_link(url):
    return (
        url.startswith('https://voussoir.net/writing/tags') or
        url.startswith('https://github.com/voussoir/voussoir.net/commit/')
    )

def normalize_link(url):
    parts = urllib.parse.urlparse(url)
    # Youtube returns HTTP 200 even for invalid video ids at /watch URLs, but
    # the thumbnail images return 404.
    if parts.netloc.endswith('youtube.com'):
        query = urllib.parse.parse_qs(parts.query, keep_blank_values=False)
        video_id = query.get('v', [''])[0]
        if video_id:
            return f'https://i3.ytimg.com/vi/{video_id}/default.jpg'
    elif parts.netloc.endswith('youtu.be'):
        video_id = parts.path.strip('/')
        if video_id:
            return f'https://i3.ytimg.com/vi/{video_id}/default.jpg'
    return url

def linkchecker(do_external=True):
    seen = set()
    queue = collections.deque()
    queue.append('https://voussoir.net/')
    if vlogging.ARGV_LEVEL >= vlogging.INFO:
        progressbar = progressbars.Bar1(total=1)
    else:
        progressbar = progressbars.DoNothing()

    results = {}
    linked_by = {
        'https://voussoir.net/writing': set()
    }
    linked_by['https://voussoir.net/writing/'] = linked_by['https://voussoir.net/writing']

    goods = 0
    warnings = 0
    bads = 0

    processed_count = 0
    while len(queue) > 0:
        url = queue.popleft()
        if url == 'https://voussoir.net/writing':
            url = 'https://voussoir.net/writing/'
        result = dotdict.DotDict()
        result.exc = None
        result.url = url
        result.url_parts = urllib.parse.urlparse(url)
        if result.url_parts.netloc == 'voussoir.net':
            log.debug('HEAD %s', url)
            result.head = session.head(url, allow_redirects=False)
            if result.head.status_code in REDIRECT_CODES:
                link = result.head.headers['Location']
                linked_by.setdefault(link, set()).add(url)
                if link not in seen:
                    queue.append(link)
                seen.add(link)
            elif 'text/html' in result.head.headers['content-type'] and not url.endswith('.html'):
                log.debug('GET %s', url)
                response = session.get(url)
                soup = bs4.BeautifulSoup(response.text, 'html.parser')
                if result.url_parts.fragment:
                    if not soup.find(id=result.url_parts.fragment):
                        result.exc = BrokenAnchor(f'Broken anchor: #{result.url_parts.fragment}')
                links = extract_links(url, soup)
                for link in links:
                    linked_by.setdefault(link, set()).add(url)
                new_links = links.difference(seen)
                seen.update(new_links)
                queue.extend(new_links)
            key = (result.exc, result.head.status_code, result.url_parts.netloc)
            results.setdefault(key, []).append(result)
        elif do_external:
            log.debug('HEAD %s', url)
            status = 999
            try:
                result.head = session.head(url, timeout=10)
                status = result.head.status_code
                if result.head.status_code == 405:
                    try:
                        result.head = session.get(url)
                        status = result.head.status_code
                    except Exception as exc:
                        result.exc = exc
            except Exception as exc:
                result.exc = exc
            key = (result.exc, status, result.url_parts.netloc)
            results.setdefault(key, []).append(result)
        else:
            continue

        if result.exc or result.head.status_code >= 400:
            bads += 1
        elif result.head.status_code == 200:
            goods += 1
        else:
            warnings += 1

        progressbar.set_total(len(seen))
        processed_count += 1
        progressbar.step(processed_count)

    progressbar.done()

    results = sorted(results.items(), key=lambda pair: (pair[0][0] is not None, pair[0][1]))

    def makemessage(result):
        if result.exc:
            mainline = f'EXC {result.url}\n{result.exc}'
        else:
            mainline = f'{result.head.status_code} {result.url}'
            if result.head.status_code == 200 and vlogging.ARGV_LEVEL > vlogging.DEBUG:
                return mainline
            if result.head.status_code in REDIRECT_CODES:
                mainline += f' -> {result.head.headers.get("location")}'

        lines = [mainline]
        for linked in linked_by[result.url]:
            lines.append(f'    Linked by {linked}')
        return '\n'.join(lines)

    for ((exc, status, domain), result_group) in results:
        print(niceprints.equals_header(f'{status} {domain}'))
        for result in result_group:
            message = makemessage(result)
            if result.exc or result.head.status_code >= 400:
                log.error(message)
            elif result.head.status_code == 200:
                log.info(message)
            else:
                log.warning(message)
        print()

    print(f'{goods} good, {warnings} warnings, {bads} bad.')

def linkchecker_argparse(args):
    linkchecker(do_external=not args.internal)
    return 0

@vlogging.main_decorator
def main(argv):
    parser = argparse.ArgumentParser(
        description='''
        ''',
    )
    parser.add_argument(
        '--internal',
        action='store_true',
        help='''
        Only check internal links.
        ''',
    )
    parser.set_defaults(func=linkchecker_argparse)

    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
