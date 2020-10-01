CREATE TABLE formats(id TEXT, kind TEXT, quality TEXT, codec TEXT);
INSERT INTO formats VALUES
('18', 'Combined', '360p30', 'AVC+m4a'),
('22', 'Combined', '720p30', 'AVC+m4a'),
('133', 'Video', '240p30', 'AVC'),
('134', 'Video', '360p30', 'AVC'),
('135', 'Video', '480p30', 'AVC'),
('136', 'Video', '720p30', 'AVC'),
('137', 'Video', '1080p30', 'AVC'),
('140', 'Audio', '130k', 'm4a'),
('160', 'Video', '144p30', 'AVC'),
('242', 'Video', '240p30', 'VP9'),
('243', 'Video', '360p30', 'VP9'),
('244', 'Video', '480p30', 'VP9'),
('247', 'Video', '720p30', 'VP9'),
('248', 'Video', '1080p30', 'VP9'),
('249', 'Audio', '50k', 'Opus'),
('250', 'Audio', '70k', 'Opus'),
('251', 'Audio', '160k', 'Opus'),
('271', 'Video', '1440p30', 'VP9'),
('272', 'Video', '4320p30', 'VP9'),
('278', 'Video', '144p30', 'VP9'),
('298', 'Video', '720p60', 'AVC'),
('299', 'Video', '1080p60', 'AVC'),
('302', 'Video', '720p60', 'VP9'),
('303', 'Video', '1080p60', 'VP9'),
('308', 'Video', '1440p60', 'VP9'),
('313', 'Video', '2160p30', 'VP9'),
('315', 'Video', '2160p60', 'VP9'),
('330', 'Video', '144p60 HDR', 'VP9'),
('331', 'Video', '240p60 HDR', 'VP9'),
('332', 'Video', '360p60 HDR', 'VP9'),
('333', 'Video', '480p60 HDR', 'VP9'),
('334', 'Video', '720p60 HDR', 'VP9'),
('335', 'Video', '1080p60 HDR', 'VP9'),
('336', 'Video', '1440p60 HDR', 'VP9'),
('337', 'Video', '2160p60 HDR', 'VP9'),
('394', 'Video', '144p30', 'AV1'),
('395', 'Video', '240p30', 'AV1'),
('396', 'Video', '360p30', 'AV1'),
('397', 'Video', '480p30', 'AV1'),
('398', 'Video', '720p60', 'AV1'),
('399', 'Video', '1080p60', 'AV1'),
('400', 'Video', '1440p60', 'AV1'),
('401', 'Video', '2160p60', 'AV1'),
('571', 'Video', '4320p60', 'AV1');

.headers on

.print Youtube-dl format code cheatsheet
.print =================================

.print
.print Here are all the youtube-dl format codes I can find.
.print Please let me know if there are more.
.print
.print You can pass them to youtube-dl as `--format a+b/c+d/e`,
.print where a+b is your preferred video+audio pair, c+d is your second-best
.print preference, and e is your last resort.
.print "Don't forget the magic words like \"bestvideo\", \"bestaudio\" to round out your selection."
.print
.print See https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
.print

.print ## Video formats
.print
SELECT id, quality, codec FROM formats WHERE kind == "Video" ORDER BY CAST(quality AS DECIMAL) DESC, quality DESC, codec ASC;

.print
.print ### AVC only
.print
SELECT id, quality, codec FROM formats WHERE codec == "AVC" ORDER BY CAST(quality AS DECIMAL) DESC, quality DESC;

.print
.print ### VP9 only
.print
SELECT id, quality, codec FROM formats WHERE codec == "VP9" ORDER BY CAST(quality AS DECIMAL) DESC, quality DESC;

.print
.print ### AV1 only
.print
SELECT id, quality, codec FROM formats WHERE codec == "AV1" ORDER BY CAST(quality AS DECIMAL) DESC, quality DESC;

.print
.print ## Audio formats
.print
SELECT id, quality, codec FROM formats WHERE kind == "Audio" ORDER BY CAST(quality AS DECIMAL) DESC, quality DESC, codec ASC;

.print
.print ## Combined formats
.print
SELECT id, quality, codec FROM formats WHERE kind == "Combined" ORDER BY CAST(quality AS DECIMAL) DESC, quality DESC, codec ASC;

.print
.print This document is generated [programmatically](youtubedl_formats.sql)  (with the manual addition of :- for md tables).
.print
.print "    sqlite3 :memory: \".read youtubedl_formats.sql\" > youtubedl_formats.md"
