Youtube-dl format code cheatsheet
=================================

Here are all the youtube-dl format codes I can find.
Please let me know if there are more.

You can pass them to youtube-dl as `--format a+b/c+d/e`,
where a+b is your preferred video+audio pair, c+d is your second-best
preference, and e is your last resort.
Don't forget the magic words like "bestvideo", "bestaudio" to round out your selection.

See https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection

## Video formats

id|quality|codec
-:|-:|-:
571|4320p60|AV1
272|4320p30|VP9
337|2160p60 HDR|VP9
401|2160p60|AV1
315|2160p60|VP9
313|2160p30|VP9
336|1440p60 HDR|VP9
400|1440p60|AV1
308|1440p60|VP9
271|1440p30|VP9
335|1080p60 HDR|VP9
399|1080p60|AV1
299|1080p60|AVC
303|1080p60|VP9
137|1080p30|AVC
248|1080p30|VP9
334|720p60 HDR|VP9
398|720p60|AV1
298|720p60|AVC
302|720p60|VP9
136|720p30|AVC
247|720p30|VP9
333|480p60 HDR|VP9
397|480p30|AV1
135|480p30|AVC
244|480p30|VP9
332|360p60 HDR|VP9
396|360p30|AV1
134|360p30|AVC
243|360p30|VP9
331|240p60 HDR|VP9
395|240p30|AV1
133|240p30|AVC
242|240p30|VP9
330|144p60 HDR|VP9
394|144p30|AV1
160|144p30|AVC
278|144p30|VP9

### AVC only

id|quality|codec
-:|-:|-:
299|1080p60|AVC
137|1080p30|AVC
298|720p60|AVC
136|720p30|AVC
135|480p30|AVC
134|360p30|AVC
133|240p30|AVC
160|144p30|AVC

### VP9 only

id|quality|codec
-:|-:|-:
272|4320p30|VP9
337|2160p60 HDR|VP9
315|2160p60|VP9
313|2160p30|VP9
336|1440p60 HDR|VP9
308|1440p60|VP9
271|1440p30|VP9
335|1080p60 HDR|VP9
303|1080p60|VP9
248|1080p30|VP9
334|720p60 HDR|VP9
302|720p60|VP9
247|720p30|VP9
333|480p60 HDR|VP9
244|480p30|VP9
332|360p60 HDR|VP9
243|360p30|VP9
331|240p60 HDR|VP9
242|240p30|VP9
330|144p60 HDR|VP9
278|144p30|VP9

### AV1 only

id|quality|codec
-:|-:|-:
571|4320p60|AV1
401|2160p60|AV1
400|1440p60|AV1
399|1080p60|AV1
398|720p60|AV1
397|480p30|AV1
396|360p30|AV1
395|240p30|AV1
394|144p30|AV1

## Audio formats

id|quality|codec
-:|-:|-:
251|160k|Opus
140|130k|m4a
250|70k|Opus
249|50k|Opus

## Combined formats

id|quality|codec
-:|-:|-:
22|720p30|AVC+m4a
18|360p30|AVC+m4a

This document is generated [programmatically](youtubedl_formats.sql) (with the manual addition of :- for md tables).

    sqlite3 :memory: ".read youtubedl_formats.sql" > youtubedl_formats.md
