Slightly obsessed with GPX
==========================

In December 2020, I downloaded an app called [Trackbook](https://codeberg.org/y20k/trackbook) by author y20k. This records your GPS position while you walk, hike, drive, or bike, so you can see where you went. [GPX](https://www.topografix.com/GPX/1/1/) is a standardized XML format for storing these tracks.

![](gpx_1.png)

There are quite a few Android apps for recording GPX files, but I always found Trackbook to be the most pleasant to use for both its aesthetics and simplicity. I submitted some bug reports and even stumbled my way through Android Studio enough to make code changes and submit a few pull requests, which were merged.

GPX files are helpful for contributing edits to [openstreetmap](https://openstreetmap.org), because you can more accurately trace out paths that might not be clear in aerial photos, and you can publish the GPX for other mappers to reference as well. You can also use the GPX to know where you were standing when you took a photo of a point of interest, so that you can position the POI more accurately on the map. This is better than relying on EXIF geotagging in some cases.

Besides being useful, I think GPX recordings are fun. I don't need a GPX to help me map out a sidewalk, but I record my walks anyway because it's cool to see where I was at some time in the past. Much like a photograph, a GPX recording is an artifact by which to remember the day.

Now that I've recorded more than 100 GPX files, I have become quite fascinated with dumping all of them into [JOSM](https://josm.openstreetmap.de/) and seeing every single track overlaid on top of each other. The rivers of common routes and spiderwebs of distant destinations are very pretty. I zoom in and out, recognizing locations by their pink periphery against a plain black background.

![](gpx_2.png)

![](gpx_3.png)

![](gpx_4.png)

In March 2023, I became seriously interested in the idea of recording GPX 24/7. I started to think about how awesome these pink rivers and spiderwebs would look if every single path were lit up. Until now, I had primarily used Trackbook to record deliberate outings and special trips. And that's great, but it meant that my track collection mostly showed little disconnected bubbles of places I've been to only once or twice because I didn't typically record day-to-day events. Also, if I was [driving](/writing/not_just_bikes) to a location to hike at, I'd intentionally wait until I got there to start recording because the drive would dominate the statistics like distance travelled and average speed. What's worse is that I would sometimes forget to start recording at all, and I'd miss the whole day. I knew that micromanaging the start and stop time of each recording for the purpose of statistics was silly, and that it would be better to collect as many trackpoints as possible and then make sense of it in post.

Initially, I was concerned that if I recorded too many tracks, the boring commutes would drown out the interesting trips, but it turns out that boring tracks are actually interesting too, given time. Seeing how easily JOSM handled the quantity of points I loaded into it gave me confidence that I should proceed. It is probably better to regret having too much data than to regret not having it.

However, the data structure and user interface of Trackbook are not geared toward 24/7 recording. It is designed for recording outings with a distinct start and end, and this presented me with some [friction](/writing/friction) in using it the way I imagined.

<p style="text-align:center;"><a style="display:inline-block;" href="https://git.voussoir.net/voussoir/trkpt"><img src="trkpt_squircle_128x128.png"/></a></p>

I sat on the problem for a very long time, and then I finally decided to make a fork of Trackbook called [trkpt](https://git.voussoir.net/voussoir/trkpt) that takes the data model in a direction more suited to my goal. This is my first time forking someone else's project and republishing it with a new name. It makes me feel somewhat guilty, or rude, but it's ok by the license and I'm enjoying the freedom to make this work just how I want it.

Basically, I swapped out the JSON-based file storage with an [SQLite](/writing/sqlite_what_a_hunk) database, and removed the entire concept of "Tracks" as a stored object. Instead, the database of trackpoints is queried on the fly to produce tracks with any start and end time you want, which you can export as GPX files. This also opens the door to JOSM-style megarenders and geospatial queries like "what day was I here?". I even made it pink.

![](trkpt_1.png)

I also added "homepoints", which are points you can put on the map around your home or workplace so that trkpt does not record any trackpoints there. Due to GPS's natural inaccuracy and drift, which is especially bad when you are indoors, you tend to get large clouds of points around buildings if you leave the recording on, so homepoints eliminate that.

In the first draft of this article, I wrote:

> I do not literally run trkpt 24/7 just yet, because my instinct for optimization doesn't like the thought of leaving the GPS at full power all night long and at work, capturing tens of thousands of fixes that are immediately thrown away; or worse, struggling to capture a fix at all. It is hard to shake the somewhat superstitious feeling that it would have a negative effect on my phone's long-term battery lifespan. Maybe I will find a balance that reduces power consumption near homepoints without sleeping the GPS so much that it is late to capture departures. These mental blocks are the only thing in the way of me running trkpt all the time, so the code changes themselves have been successful, I think. I am still starting trkpt when I wake up in the morning and turning it off at work. But for day trips on weekends I record the whole day with no stress, thanks to the flexibility of the new data model.

But, I sent an email to y20k to share my work with him, and he suggested using the device's accelerometers to improve the sleep/wake cycle and conserve battery. This really helps!

Android provides a [significant motion sensor](https://source.android.com/docs/core/interaction/sensors/sensor-types#significant_motion) which, while implementation surely depends on the manufacturer, is meant to be used in low power scenarios where a latency of several seconds is acceptable. When we are near a homepoint, we can reduce the polling frequency of the GPS to once per minute, or perhaps five minutes. As soon as motion is detected, we can wake it back up to full power, so that by the time your shoes are tied, your fix is hot again.

When I am at work, my device struggles to acquire any GPS fixes at all, so trkpt can't even know if I'm near the homepoint. In this case, there is no benefit in reducing the polling frequency of the GPS. If you ask Android for one location per minute and it has to struggle for several minutes to get a single fix, then you're not saving anything. The GPS burns a lot of energy in this state and it's better to turn it fully off. This means we are placing a lot of trust in the motion sensor to restart the GPS, so I will see how it goes and continue experimenting with the balance between all these features.

Anyway, the code is the easy part. Now I have to do the hard part which is actually going out to interesting places more often and turning the world pink.

Thank you y20k for making Trackbook!
