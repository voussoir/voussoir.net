[tag:photography]

Sharing photos with friends and strangers
=========================================

## Introduction

In the [previous episode](/writing/hobby_photography), I said that taking pictures of friends and family was the most worthwhile thing I can do with photography at the moment. In this episode I will detail how exactly I'm going about giving these people copies of the pictures to keep for their own memories.

For the purpose of this discussion, I'm not talking about sending a single picture by MMS or email attachment. I'm talking about sending 100+ photos of an event or outing to one or more people at full resolution, files of about 16 megabytes each. I have been improving this process over the past few months with photos going out to friends, family, friends-of-friends, coworkers, concert performers, and the parents of a youth sports team.

The end results are pages that look like this: https://files.voussoir.net/2022-11-12%20Sharing%20Photos/gallery.html

## Process

The first step is to take the pictures. This step is very important.

I am currently using [Honeyview](https://en.bandisoft.com/honeyview/) to review and cull photos. I like that it has minimal interface elements and a good fullscreen mode.

I don't do much editing, but some pictures need a bit of level adjustment due to harsh sunlight or missed exposure. I do this in Photoshop, but Photoshop has an annoying habit of trampling all over the EXIF data as if it owns the place. I always make a copy of the original photo before doing these edits, so that afterward a quick call to this [exiftool bat file](https://github.com/voussoir/cmd/blob/master/exifcopy.bat) can put the EXIF back where it belongs. You may say that this results in dishonest metadata, but to me that is less of a sin than letting Adobe put its name all over my files.

For hosting and distributing the files, it is important to me that the system is under my ownership, for a few reasons. Firstly, the HTML that I can put together is better for the purpose of looking at and downloading original pictures than the interface you'll get from most image sharing or cloud drive websites. Secondly, I want all of these files to be private, or at least non-indexed, because I respect my friends and don't want to make pictures of them public on the internet. They can download their favorites and put those on social media if they choose to, but I won't.

The website you are reading now is currently hosted on an OVH VPS, which comes with 20 gigabytes of disk space. I can pay more for more space, but the cost is not economical for the purpose of cold storage of static files. I decided to make an account with [Cloudflare R2](https://www.cloudflare.com/products/r2/), whose billing is much simpler than Amazon S3 at 1.5¢ per gigabyte of storage per month and no cost for ingress/egress bandwidth. This is cheaper than any kind of Flickr Pro or Google Drive, and is accessible by command line.

In order to give my R2 bucket a domain name, I had to move my DNS nameservers to Cloudflare's. Adding A records on my registrar's DNS was not good enough because Cloudflare does special serverside checks of some kind. If I am wrong about this and it's possible to use R2 with non-cloudflare nameservers, please email me as I'd like to know. I am not thrilled about making this compromise but, obviously, the other factors outweighed it. I turned off all of Cloudflare's enabled-by-default caching / traffic routing for the rest of voussoir.net. All of the files I upload to R2 are publicly accessible by just their URL, but since there are no directory listings it is not really possible for search engines to discover them unless someone I've given the link to has put it online [footnote_link].

I wrote [photo_rename.py](https://github.com/voussoir/cmd/blob/master/photo_rename.py) to rename the files from "DSCF0001.jpg" to timestamps. Even though we live in an age of 10 to 30 fps burst shooting modes, a lot of cameras still don't put subsecond timing in their EXIF data, mine included unfortunately. So, photos from the same second are marked as x1, x2, etc.

I wrote [photogallery.py](https://github.com/voussoir/cmd/blob/master/photogallery.py) to generate a simple HTML page. Remember, the goals are to **look at pictures**, so there is no "page 1... page 2... page 3..." nuisance or teeny-tiny thumbnails as you'd get on most photo gallery websites; and to **download pictures**, so every element links to the full res file and an `<a download>` button is added to every photo for additional convenience. This requires that the server allows hotlinking, which you don't typically get from cloud drive providers but you do get from object storage providers. The image links are `target="_blank"` so that if you miss the download button, you get the big photo in a new tab and don't lose your scroll position on the gallery. `photogallery *.jpg --title "2022-11-12 Sharing Photos" --urlroot "https://files.voussoir.net/2022-11-12 Sharing Photos/"` prepares the HTML, and I usually go in and add some kind of greeting like "Hi everyone, here are the photos from today's event, please enjoy".

I use [resize.py](https://github.com/voussoir/cmd/blob/master/resize.py) to prepare the gallery thumbnails. `resize *.jpg --width 1024 --height 1024 --output thumbs\small_{filename} --quality 80` does the job. 1024px is large enough to comfortably browse the photos without clicking through to the big version of each, and the thumbnails are decently light and not too [jpeggy](https://www.youtube.com/watch?v=QEzhxP-pdos "Do I look like I know what a JPEG is?") at about 125-150 kilobytes on average. I make sure to put the word "small" at the beginning of the thumbnail filename so that if someone downloads the thumbnail instead of the full picture by mistake, it should be pretty obvious unless they are particularly undiscerning, in which case their ignorance is bliss.

I followed Cloudflare's guide to set up the AWS S3 commandline utility for use with R2 ([one](https://developers.cloudflare.com/r2/data-access/s3-api/api/), [two](https://developers.cloudflare.com/r2/data-access/s3-api/tokens/), [three](https://developers.cloudflare.com/r2/examples/aws-cli/)) and I put that in a shortcut file on my PATH. So, `voussoirr2.lnk` points to `C:\Python\__latest\Scripts\aws.cmd --endpoint-url "https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.r2.cloudflarestorage.com"`. I call `voussoirr2 s3 cp . "s3://voussoir/2022-11-12 Sharing Photos" --recursive` to upload.

I log into the R2 web interface to make sure the photos went where I intended, and then I give out the link to the gallery.html file: https://files.voussoir.net/2022-11-12%20Sharing%20Photos/gallery.html

If I wanted to, I could prepare a zip file containing all the photos and upload that as well, so that viewers could bulk download. If I was doing some kind of contract work, delivering a photo package to a customer, I would. But friends and family don't really care to download all 100+ pictures from a day. They'll pick their favorites that contain themselves or their kid, so bulk downloading is not necessary for the task at hand.

Wow, it's just that easy!

[footnote_text] If I wanted to further prevent indexing, I would write some clientside javascript to prompt the user for a gallery password which is integral to the path of the photos. The password would not even need to be hashed. As long as HTML never statically contains the true links to the photos, no off-the-shelf scraper would find them without the out-of-band password. It's not Fort Knox, anyway.
