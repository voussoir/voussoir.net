Youtube re-encoding videos
==========================

<style>
figure
{
    display: grid;
    justify-content: center;
    align-items: center;
}
figure div
{
    position:relative;
}
figure div:nth-of-type(1):before
{
    content: "A";
    position: absolute;
    background-color: black;
    left: 8px;
    top: 8px;
}
figure div:nth-of-type(2):before
{
    content: "B";
    position: absolute;
    background-color: black;
    right: 8px;
    top: 8px;
}
</style>

## Introduction

Today, I re-downloaded a video that I already had a copy of. I was surprised to find that the video stream lost 33% of its bitrate. The bitrate was down from 600kbps to 400kbps, even though both files were labeled as [f136](https://voussoir.net/writing/youtubedl_formats/#avc_only), which is Youtube's 720p AVC stream.

This video is Tim Minchin's [Storm](https://youtu.be/HhGuXCuDb1U). A classic.

Older copy, acquired September 2020:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : V_MPEG4/ISO/AVC
Duration                                 : 10 min 38 s
Bit rate                                 : 601 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 24.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.027
Stream size                              : 45.7 MiB (98%)
Default                                  : Yes
Forced                                   : No
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
VENDOR_ID                                : [0][0][0][0]
```

Newer copy, acquired July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : V_MPEG4/ISO/AVC
Duration                                 : 10 min 38 s
Bit rate                                 : 400 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 24.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.018
Stream size                              : 30.5 MiB (98%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Default                                  : Yes
Forced                                   : No
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
VENDOR_ID                                : [0][0][0][0]
```

Has Youtube found more optimal compression parameters so they can produce the same visual quality at a lower filesize, or is it just worse?

Click each comparison to enter fullscreen.

<figure class="comparison">
    <div><img src="HhGuXCuDb1U_1a.png"/></div>
    <div><img src="HhGuXCuDb1U_1b.png"/></div>
</figure>

<figure class="comparison">
    <div><img src="HhGuXCuDb1U_2a.png"/></div>
    <div><img src="HhGuXCuDb1U_2b.png"/></div>
</figure>

It's just worse. How dare they! I had to look for more examples.

I replaced about 90% of my youtube library in September 2020 because prior to that point I was not keeping the format code (f136, etc) in the filename. So, if there was any Great Re-encoding already underway by that time, I will have mostly missed it.

When you see "Stream size 24.2 MiB (100%)", please ignore the percentage. In my copies I of course have video+audio, but in today's test downloads I only fetched the video, thus they are 100% of themselves.

## Worse than I remember... barely

[Weird Al - White & Nerdy (Take #1)](https://youtu.be/Vq6OncN6_Fo) lost 16% bitrate and artifacts were very slightly increased.

November 2017:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 7 s
Bit rate                                 : 1 287 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Variable
Frame rate                               : 23.976 (23976/1000) FPS
Minimum frame rate                       : 23.974 FPS
Maximum frame rate                       : 2 000.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.058
Stream size                              : 28.8 MiB (91%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 7 s
Bit rate                                 : 1 082 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 23.976 (24000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.049
Stream size                              : 24.2 MiB (100%)
Title                                    : ISO Media file produced by Google Inc. Created on: 05/25/2019.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2019-05-25 11:27:26
Tagged date                              : UTC 2019-05-25 11:27:26
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="Vq6OncN6_Fo_a.png"/></div>
    <div><img src="Vq6OncN6_Fo_b.png"/></div>
</figure>

<hr/>

[Rick Astley - Never Gonna Give You Up](https://youtu.be/dQw4w9WgXcQ) lost 7% bitrate and artifacts were very slightly increased.

September 2020:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 32 s
Bit rate                                 : 3 159 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 25.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.061
Stream size                              : 79.8 MiB (96%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 32 s
Bit rate                                 : 2 965 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 25.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.057
Stream size                              : 75.0 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2023-01-20 16:50:18
Tagged date                              : UTC 2023-01-20 16:50:18
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="dQw4w9WgXcQ_a.png"/></div>
    <div><img src="dQw4w9WgXcQ_b.png"/></div>
</figure>

<hr/>

[Kitty0706 - Moments with Heavy - French Toast](https://youtu.be/dNB-EREknic) lost a huge 74% bitrate. Artifacts are worse, but honestly not as bad as I expected.

December 2016:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 4 min 23 s
Bit rate                                 : 966 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.035
Stream size                              : 30.4 MiB (88%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 4 min 24 s
Bit rate                                 : 255 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.009
Stream size                              : 8.02 MiB (99%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2023-07-07 08:35:27
Tagged date                              : UTC 2023-07-07 08:35:27
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="dNB-EREknic_a.png"/></div>
    <div><img src="dNB-EREknic_b.png"/></div>
</figure>

<hr/>

[Mega64 - Final Fantasy XII](https://youtu.be/vSyfGm6wXgs) lost 13% and got disproportionately rekt.

June 2017:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 23 s
Bit rate                                 : 892 kb/s
Width                                    : 640 pixels
Height                                   : 480 pixels
Display aspect ratio                     : 4:3
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.097
Stream size                              : 15.3 MiB (87%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 23 s
Bit rate                                 : 777 kb/s
Width                                    : 640 pixels
Height                                   : 480 pixels
Display aspect ratio                     : 4:3
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.084
Stream size                              : 13.3 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Encoded date                             : UTC 2019-11-03 21:14:23
Tagged date                              : UTC 2019-11-03 21:14:23
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="vSyfGm6wXgs_a.png"/></div>
    <div><img src="vSyfGm6wXgs_b.png"/></div>
</figure>

<hr/>

[randytaylor69 - the moistening.](https://youtu.be/KVmOGvQhWYE) lost 44%, though the difference is basically negligible outside of fine hair details.

July 2017:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 1 min 59 s
Bit rate                                 : 2 237 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 25.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.043
Stream size                              : 31.8 MiB (94%)
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 1 min 59 s
Bit rate                                 : 1 267 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 25.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.024
Stream size                              : 18.0 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2022-09-18 12:35:23
Tagged date                              : UTC 2022-09-18 12:35:23
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="KVmOGvQhWYE_a.png"/></div>
    <div><img src="KVmOGvQhWYE_b.png"/></div>
</figure>


## Better than I remember

[POGO - Data & Picard](https://youtu.be/bl5TUw7sUBs) gained 34% bitrate and artifacts were slightly reduced.

June 2018:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 16 s
Bit rate                                 : 1 371 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Variable
Frame rate                               : 23.976 (24000/1001) FPS
Minimum frame rate                       : 23.974 FPS
Maximum frame rate                       : 23.981 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.028
Stream size                              : 32.1 MiB (91%)
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 16 s
Bit rate                                 : 1 847 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 23.976 (24000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.037
Stream size                              : 43.2 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2023-02-20 06:11:57
Tagged date                              : UTC 2023-02-20 06:11:57
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="bl5TUw7sUBs_a.png"/></div>
    <div><img src="bl5TUw7sUBs_b.png"/></div>
</figure>

<hr/>

[GoldVision - Planetside 2 Savepoints - Don't be Greedy](https://youtu.be/BGsID_bMrhA) gained 10% and artifacts were reduced.

December 2016:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 57 s
Bit rate                                 : 3 520 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Variable
Frame rate                               : 29.970 (29970/1000) FPS
Minimum frame rate                       : 29.970 FPS
Maximum frame rate                       : 2 500.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.057
Stream size                              : 74.6 MiB (93%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 57 s
Bit rate                                 : 3 888 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.063
Stream size                              : 82.4 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Encoded date                             : UTC 2019-12-03 02:46:02
Tagged date                              : UTC 2019-12-03 02:46:02
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="BGsID_bMrhA_a.png"/></div>
    <div><img src="BGsID_bMrhA_b.png"/></div>
</figure>

<hr/>

[Ned Batchelder - Facts and Myths about Python names and values](https://youtu.be/_AEJHKGk9ns) lost 68% bitrate with no meaningful loss in quality. It's a slideshow, after all.

March 2017:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 25 min 19 s
Bit rate                                 : 636 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 30.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.023
Stream size                              : 115 MiB (83%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 25 min 19 s
Bit rate                                 : 209 kb/s
Width                                    : 1 280 pixels
Height                                   : 720 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 30.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.008
Stream size                              : 37.9 MiB (99%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2020-12-21 05:00:20
Tagged date                              : UTC 2020-12-21 05:00:20
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="_AEJHKGk9ns_a.png"/></div>
    <div><img src="_AEJHKGk9ns_b.png"/></div>
</figure>

<hr/>

[Demi Adejuyigbe - 9/21/18](https://youtu.be/CG7YHFT4hjw) gained 33% and artifacts were reduced.

September 2020:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 1 min 28 s
Bit rate                                 : 1 480 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.024
Stream size                              : 15.5 MiB (91%)
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 1 min 28 s
Bit rate                                 : 1 983 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.032
Stream size                              : 20.8 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2021-09-21 18:55:13
Tagged date                              : UTC 2021-09-21 18:55:13
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="CG7YHFT4hjw_a.png"/></div>
    <div><img src="CG7YHFT4hjw_b.png"/></div>
</figure>

<hr/>

[DATA - Don't Sing](https://youtu.be/37eEUsd1ASA) gained 33% and artifacts were slightly reduced.

September 2020:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 51 s
Bit rate                                 : 1 292 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 25.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.025
Stream size                              : 35.7 MiB (91%)
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 3 min 51 s
Bit rate                                 : 1 730 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 25.000 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.033
Stream size                              : 47.8 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2023-06-06 01:02:54
Tagged date                              : UTC 2023-06-06 01:02:54
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="37eEUsd1ASA_a.png"/></div>
    <div><img src="37eEUsd1ASA_b.png"/></div>
</figure>

<hr/>

[WASABI WOMAN](https://youtu.be/YECW_iGcrSo) gained 8%. Artifacting is slightly improved around text but is otherwise mostly a wash.

December 2018:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 30 s
Bit rate                                 : 881 kb/s
Width                                    : 854 pixels
Height                                   : 480 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.072
Stream size                              : 15.9 MiB (87%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : Main@L3.1
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 30 s
Bit rate                                 : 952 kb/s
Width                                    : 854 pixels
Height                                   : 480 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.077
Stream size                              : 17.1 MiB (100%)
Encoded date                             : UTC 2017-10-13 21:24:19
Tagged date                              : UTC 2017-10-13 21:24:19
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="YECW_iGcrSo_a.png"/></div>
    <div><img src="YECW_iGcrSo_b.png"/></div>
</figure>

<hr/>

[OK GO - The Writing's On The Wall](https://youtu.be/oL3qDpubXU8) gained 53% and artifacts were pretty significantly reduced.

December 2018:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 4 min 18 s
Bit rate                                 : 1 996 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 076 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Variable
Frame rate                               : 23.976 (24000/1001) FPS
Minimum frame rate                       : 23.974 FPS
Maximum frame rate                       : 23.981 FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.040
Stream size                              : 61.6 MiB (94%)
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 4 min 18 s
Bit rate                                 : 3 071 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 076 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 23.976 (24000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.062
Stream size                              : 94.8 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2023-06-06 07:22:05
Tagged date                              : UTC 2023-06-06 07:22:05
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="oL3qDpubXU8_a.png"/></div>
    <div><img src="oL3qDpubXU8_b.png"/></div>
</figure>

<hr/>

[David Foster Wallace - The Problem with Irony](https://youtu.be/2doZROwdte4) gained 35% and artifacts are very, very slightly reduced (not worth 35% in my opinion).

March 2022:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 9 min 53 s
Bit rate                                 : 1 031 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.017
Stream size                              : 73.0 MiB (89%)
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 9 min 53 s
Bit rate                                 : 1 398 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.022
Stream size                              : 99.0 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="2doZROwdte4_a.png"/></div>
    <div><img src="2doZROwdte4_b.png"/></div>
</figure>

<hr/>

[Gangnam Style](https://youtu.be/9bZkp7q19f0) lost 3%, with differences only appreciable under a microscope.

September 2020:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 4 min 12 s
Bit rate                                 : 3 450 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 23.976 (24000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.069
Stream size                              : 104 MiB (96%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

July 2023

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 4 min 12 s
Bit rate                                 : 3 358 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 23.976 (24000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.068
Stream size                              : 101 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2022-09-23 14:42:00
Tagged date                              : UTC 2022-09-23 14:42:00
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="9bZkp7q19f0_a.png"/></div>
    <div><img src="9bZkp7q19f0_b.png"/></div>
</figure>

<hr/>

[Weird Al - Another Tattoo](https://youtu.be/BF6ct9ZEq5s) lost 18%, yet the linework has been greatly sharpened, possibly too far to the point of aliasing. Whether that's true to the source I cannot say. This video's low-contrast papyrusy background is still pretty hell for blocking artifacts.

December 2016:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 50 s
Bit rate                                 : 2 456 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.040
Stream size                              : 49.8 MiB (95%)
Codec configuration box                  : avcC
```

July 2023:

```
Video
ID                                       : 1
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 3 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 3 frames
Codec ID                                 : avc1
Codec ID/Info                            : Advanced Video Coding
Duration                                 : 2 min 49 s
Bit rate                                 : 2 021 kb/s
Width                                    : 1 920 pixels
Height                                   : 1 080 pixels
Display aspect ratio                     : 16:9
Frame rate mode                          : Constant
Frame rate                               : 29.970 (30000/1001) FPS
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : Progressive
Bits/(Pixel*Frame)                       : 0.033
Stream size                              : 40.9 MiB (100%)
Title                                    : ISO Media file produced by Google Inc.
Writing library                          : x264 core 155 r2901 7d0ff22
Encoded date                             : UTC 2023-05-04 02:57:10
Tagged date                              : UTC 2023-05-04 02:57:10
Color range                              : Limited
Color primaries                          : BT.709
Transfer characteristics                 : BT.709
Matrix coefficients                      : BT.709
Codec configuration box                  : avcC
```

<figure class="comparison">
    <div><img src="BF6ct9ZEq5s_a.png"/></div>
    <div><img src="BF6ct9ZEq5s_b.png"/></div>
</figure>

## Meager plotting attempt

I asked mediainfo for the bitrate of some of my files, and plotted them.

When sorted by video publication date, keeping in mind this is not the acquisition date and therefore would be impacted by any kind of Great Re-encoding that could have happened, I don't see much obvious pattern. You could say that fewer f137 videos are above 4000kbps since 2018.

![](f137_by_publication.png)

![](f136_by_publication.png)

![](f299_by_publication.png)

When sorted by video acquisition date, I don't see anything worth speculating on. This data is simply not enough to work with. I would be much more concerned if I saw some kind of hard ceiling, for example if f137 suddenly stopped crossing 4000kbps, which it did not.

Some of the bitrate clumping could be explained by me downloading a lot of videos from a single channel, each a little different from the global average.

![](f137_by_acquisition.png)

![](f136_by_acquisition.png)

![](f299_by_acquisition.png)

## Conclusion

Fancy that.

This article would have been much more exciting and outrageous if all the videos got worse, and it's a shame that any of them have. But, as usual, the truth is less exciting and outrageous, and in most cases the re-encoded files look better or about the same. I'm totally pixel-peeping these comparisons, and I think you'll agree that even the videos that *did* get worse show underwhelming difference. Except Storm.

This experiment only shows a sample of 16 videos, which is perhaps not up to your standards of rigor. But I went into this expecting to find a clear decrease in bitrate and visual quality, based on my personal experience seeing blocking artifacts in almost every youtube video I watch. If that doesn't pan out after 16 examples, it seems like it would be pathetic and desperate to keep digging for some lucky gotcha. The bitrates have just been low the whole time.

The oldest file I have is from 2016, and the majority are from 2020 onward, so that limits the scope of this experiment. When I tested videos that I acquired during 2021-2023 I found the bitrates were almost always identical to before, so I did not mention them here. I think Youtube's re-encoder is not toying with such recent videos.

For what it's worth, you don't need to tell me that VP9 and AV1 will look better than AVC at equivalent bitrates.

<script>
let state = false;
function switch_figures()
{
    for (const figure of document.getElementsByTagName("figure"))
    {
        if (state)
        {
            figure.children[0].style.display = "none";
            figure.children[1].style.display = "block";
        }
        else
        {
            figure.children[0].style.display = "block";
            figure.children[1].style.display = "none";
        }
    }
    state = (! state);
}
function on_pageload()
{
    for (const figure of document.getElementsByTagName("figure"))
    {
        figure.addEventListener("click", (event) => event.target.closest("figure").requestFullscreen());
    }
    setInterval(switch_figures, 1000);
}
document.addEventListener("DOMContentLoaded", on_pageload);
</script>