Youtube-dl format code cheatsheet
=================================

Here are all the youtube-dl format codes I can find.
Please let me know if there are more.

You can pass them to youtube-dl as `--format a+b/c+d/e`,
where a+b is your preferred video+audio pair, c+d is your second-best
preference, and e is your last resort.
Don't forget the magic words like "bestvideo", "bestaudio" to round out your selection.

See https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection

There are more formats listed in [youtube-dl's source code](https://github.com/ytdl-org/youtube-dl/blob/eb6181759f3a784d7b77ec9d2ec1a65dfd695d92/youtube_dl/extractor/youtube.py#L430),
but some of them seem to be obsolete and are no longer returned by `-F`
even when using the example video IDs listed there. I will only include
codes for which I have an example.

## Video formats

id | quality | codec | examples
-: | -: | -: | :-
571|4320p60|AV1|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ`
272|4320p30|VP9|`youtube-dl -F i6fWG4FxDZw`
337|2160p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
401|2160p60|AV1|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ`
305|2160p60|AVC|`youtube-dl -F -xNN-bJQ4vI`
315|2160p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
266|2160p30|AVC|`youtube-dl -F -xNN-bJQ4vI i6fWG4FxDZw`
313|2160p30|VP9|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
336|1440p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
400|1440p60|AV1|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ`
304|1440p60|AVC|`youtube-dl -F -xNN-bJQ4vI`
308|1440p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
264|1440p30|AVC|`youtube-dl -F -xNN-bJQ4vI i6fWG4FxDZw`
271|1440p30|VP9|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
335|1080p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
399|1080p60|AV1|`youtube-dl -F 1La4QzGeaaQ`
299|1080p60|AVC|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
303|1080p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
137|1080p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
248|1080p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
334|720p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
398|720p60|AV1|`youtube-dl -F 1La4QzGeaaQ`
298|720p60|AVC|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
302|720p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
136|720p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
247|720p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
333|480p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
397|480p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
135|480p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
244|480p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
332|360p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
396|360p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
134|360p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
243|360p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
331|240p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
395|240p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
133|240p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
242|240p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
330|144p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
394|144p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
160|144p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
278|144p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`

### AVC only

id | quality | codec | examples
-: | -: | -: | :-
305|2160p60|AVC|`youtube-dl -F -xNN-bJQ4vI`
266|2160p30|AVC|`youtube-dl -F -xNN-bJQ4vI i6fWG4FxDZw`
304|1440p60|AVC|`youtube-dl -F -xNN-bJQ4vI`
264|1440p30|AVC|`youtube-dl -F -xNN-bJQ4vI i6fWG4FxDZw`
299|1080p60|AVC|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
137|1080p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
298|720p60|AVC|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
136|720p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
135|480p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
134|360p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
133|240p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
160|144p30|AVC|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`

### VP9 only

id | quality | codec | examples
-: | -: | -: | :-
272|4320p30|VP9|`youtube-dl -F i6fWG4FxDZw`
337|2160p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
315|2160p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
313|2160p30|VP9|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
336|1440p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
308|1440p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
271|1440p30|VP9|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
335|1080p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
303|1080p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
248|1080p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
334|720p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
302|720p60|VP9|`youtube-dl -F 1La4QzGeaaQ -xNN-bJQ4vI`
247|720p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
333|480p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
244|480p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
332|360p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
243|360p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
331|240p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
242|240p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`
330|144p60 HDR|VP9|`youtube-dl -F 1La4QzGeaaQ`
278|144p30|VP9|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ -xNN-bJQ4vI i6fWG4FxDZw`

### AV1 only

id | quality | codec | examples
-: | -: | -: | :-
571|4320p60|AV1|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ`
401|2160p60|AV1|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ`
400|1440p60|AV1|`youtube-dl -F kFz9afj8lu0 1La4QzGeaaQ`
399|1080p60|AV1|`youtube-dl -F 1La4QzGeaaQ`
398|720p60|AV1|`youtube-dl -F 1La4QzGeaaQ`
397|480p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
396|360p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
395|240p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`
394|144p30|AV1|`youtube-dl -F S8Zt6cB_NPU 1La4QzGeaaQ`

## Audio formats

id | quality | codec | examples
-: | -: | -: | :-
258|386k|m4a|`youtube-dl -F NMANRHz4UAY`
256|195k|m4a|`youtube-dl -F NMANRHz4UAY`
251|160k|Opus|`youtube-dl -F S8Zt6cB_NPU`
140|128k|m4a|`youtube-dl -F S8Zt6cB_NPU`
250|70k|Opus|`youtube-dl -F S8Zt6cB_NPU`
249|50k|Opus|`youtube-dl -F S8Zt6cB_NPU`

## Combined formats

id | quality | codec | examples
-: | -: | -: | :-
22|720p30|AVC+m4a|`youtube-dl -F S8Zt6cB_NPU`
18|360p30|AVC+m4a|`youtube-dl -F S8Zt6cB_NPU`

This document is generated [programmatically](youtubedl_formats.sql).

    sqlite3 :memory: ".read youtubedl_formats.sql" > youtubedl_formats.md
