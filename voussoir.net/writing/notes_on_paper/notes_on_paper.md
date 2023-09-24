[tag:today_i_did_this]

Notes on paper
==============

## Introduction

Over the past few weeks, I have been scanning my notes and homework from school using the nice professional scanners at my workplace. These notes have been sitting in my closet for several years because I don't want to keep them, but didn't want to throw them out until scanning them, and I've never had access to a scanner that could do all these pages.

This has prompted me to reflect on some of the habits and choices that I follow in my handwritten notes. I realize there are entire online cultures of journaling and notetaking and notebook-buying, and I'm not here to compete with them. This is just what I do.

## Habits

Always put a date on every page, including pages that are given to you. For multiple pages in one day, it helps to add a page number.

Always use loose leaf paper, never bound notebooks.

- You can hand a single sheet to someone.
- You can rewrite a sheet later and put it back in the same order, instead of keeping or tearing out the bad copy.
- Easier to cross reference a previous day without flipping back and forth.
- Easier to integrate with other material: pages you receive, homework you submit and get back.
- Easier to purchase the same or equivalent paper over the course of years, rather than developing an eclectic assortment of different notebooks or, worse, a brand dependency.
- Easier to scan.

Always use full-size paper (US Letter or A4 depending on your region) so that your notes stack well with printed material. A lot of lined/punched notebook paper is [smaller](2018-03-05.png) than printer paper.

Prefer to write in black ink rather than colored ink or pencil. Use quality pens that produce deep black lines, not cheap pens that produce off-black or hollow lines.

- Easier to scan in 1-bit format.
- I like black, what can I say.

Always write on a single side of the paper, never the backside, unless forced to do so. The dollar cost of the paper is less than the [inconvenience](2018-03-06.png) cost of double sided material.

Resist the urge to cram everything onto one page. The telltale switch from big handwriting to "I'm running out of space" small handwriting at the bottom of the page is shameful. Two pages with healthy margins and spacing is better than one page of cramming.

Consider using graph paper, even for non-mathematics, non-engineering notes. Prefer faint gridlines. You can:

- Accurately indent line continuations, sub-commentary, or [nested bullet points](2017-10-24.png).
- Write in a [two-column](2017-02-21.png) format.
- Cordon off side-thoughts in [boxes](2016-04-03.png).
- Draw pictures or diagrams of [consistent size and spacing](2017-02-02.png).

Consider using plain, blank printer paper. At work, I am currently using blank printer paper for all my notetaking, and my "manuscript" is up to about 140 sheets. I don't think I would recommend this for structured school lectures, but it's good for unstructured meetings.

- Very low cost per sheet.
- Complete freedom to draw (beware, too much freedom = [wobbly, drifting text](2017-10-17.png)).

Consider re-writing your notes after your class/meeting, so that you can:

- Reorganize the information in a new order that you could not have foreseen when taking it down.
- Use slower, more careful handwriting.
- Replace abbreviations with full words and phrases.
- Eliminate the scratched-out mistakes and keep only the good parts.

I have never used a digital tablet for notetaking, and I will not make the appeal to tradition that paper is always better. I can imagine it brings some advantages:

- Don't need to scan it.
- Instant OCR makes it searchable (assuming software support) (requires non-awful handwriting).
- Can mix typing for perfect legibility with drawing for visual aids.
- Easier to integrate photos taken on the spot.
- Infinite paper and ink.
- Undo button, layers, drag to rearrange.

Advantages of paper:

- Cheap.
- Easier to lay out multiple sheets and review / cross-reference pages in any order -- not limited to real estate of one screen and scrolling / tab-switching.
- You can hand someone a single sheet so they can read it while you work on other sheets -- you're not handing them your entire system.
- Easier to integrate with material you receive.
- Open-note exams will probably only allow paper for quite some time yet.

## Scanning

I scanned everything at 600 PPI in 1-bit TIFF. The scanners at work don't seem to support lossless full color, and I'd rather have the aliasing and dithering artifacts of lossless 1-bit than the jpeggy, blocky artifacts of lossy color. This is an aesthetic preference and I think dithering looks cool anyway.

I wrote [imagesequence_to_images.py](https://git.voussoir.net/voussoir/cmd/src/branch/master/imagesequence_to_images.py) to turn the scanner's multi-page TIF file into separate PNGs.

I use [brename.py](https://git.voussoir.net/voussoir/cmd/src/branch/master/brename.py) to rename everything.

When dealing with double-sided material and a single-sided scanner, I scanned the stack twice for the fronts and backs. Then, I did something like this:

```batch
md fronts && move fronts*.png fronts
md backs && move backs*.png backs

cd fronts

# Fronts will get even index numbers, starting from zero.
brename "f'{(index*2):03d}.png'"

cd ..\backs

# Large number minus index to reverse the file order.
brename "f'{(999-index):03d}.png'"

# Backs will get odd index numbers, starting from one.
brename "f'{(index*2)+1:03d}.png'"

cd ..
move fronts\* . && rmdir fronts
move backs\* . && rmdir backs

# ...
# Spend a few minutes manually deleting the blank backsides.
# ...

# Reindex all the files so we can pretend the blank backsides didn't exist.
# Renaming will fail if the target filename already exists, so temporarily
# bump up to more digits, then back down.
brename "f'{index1:04d}.png'"
brename "f'{index1:03d}.png'"
```

## Some pages

Here are some pages that I thought were visually interesting. These are not perfect demonstrations of the habits above, and that's the point -- over time I have realized things I should have been doing all along.

I find there's something really engaging about being able to zoom in and pan around and pixel peep at these millimeter-sized features that, at the time of their making, only occupied a few tenths of a second of attention. The small writ large, as it were.

I am including more pages here than most anybody will care to look through, but I couldn't pick any more to eliminate. I think they're kind of cool.

<style>
section
{
    text-align: center;
}
</style>

<section>
<a href="2015-10-29.png"><img src="small_2015-10-29.png" height="512"/></a>
<a href="2015-11-19.png"><img src="small_2015-11-19.png" height="512"/></a>
<a href="2016-04-08.png"><img src="small_2016-04-08.png" height="512"/></a>
<a href="2016-04-25.png"><img src="small_2016-04-25.png" height="512"/></a>
<a href="2017-01-12.png"><img src="small_2017-01-12.png" height="512"/></a>
<a href="2017-01-26.png"><img src="small_2017-01-26.png" height="512"/></a>
<a href="2017-02-02.png"><img src="small_2017-02-02.png" height="512"/></a>
<a href="2017-02-28.png"><img src="small_2017-02-28.png" height="512"/></a>
<a href="2017-04-13.png"><img src="small_2017-04-13.png" height="512"/></a>
<a href="2017-04-21.png"><img src="small_2017-04-21.png" height="512"/></a>
<a href="2017-05-01.png"><img src="small_2017-05-01.png" height="512"/></a>
<a href="2017-05-03.png"><img src="small_2017-05-03.png" height="512"/></a>
<a href="2017-05-15.png"><img src="small_2017-05-15.png" height="512"/></a>
<a href="2017-05-22.png"><img src="small_2017-05-22.png" height="512"/></a>
<a href="2017-06-22.png"><img src="small_2017-06-22.png" height="512"/></a>
<a href="2017-06-29.png"><img src="small_2017-06-29.png" height="512"/></a>
<a href="2017-07-11.png"><img src="small_2017-07-11.png" height="512"/></a>
<a href="2017-10-06.png"><img src="small_2017-10-06.png" height="512"/></a>
<a href="2017-10-13.png"><img src="small_2017-10-13.png" height="512"/></a>
<a href="2017-10-20.png"><img src="small_2017-10-20.png" height="512"/></a>
<a href="2017-10-30.png"><img src="small_2017-10-30.png" height="512"/></a>
<a href="2017-11-05.png"><img src="small_2017-11-05.png" height="512"/></a>
<a href="2017-11-13.png"><img src="small_2017-11-13.png" height="512"/></a>
<a href="2017-11-27.png"><img src="small_2017-11-27.png" height="512"/></a>
<a href="2018-01-03.png"><img src="small_2018-01-03.png" height="512"/></a>
<a href="2018-01-12.png"><img src="small_2018-01-12.png" height="512"/></a>
<a href="2018-01-22.png"><img src="small_2018-01-22.png" height="512"/></a>
<a href="2018-01-26.png"><img src="small_2018-01-26.png" height="512"/></a>
<a href="2018-01-29.png"><img src="small_2018-01-29.png" height="512"/></a>
<a href="2018-01-31.png"><img src="small_2018-01-31.png" height="512"/></a>
<a href="2018-02-12.png"><img src="small_2018-02-12.png" height="512"/></a>
<a href="2018-06-20.png"><img src="small_2018-06-20.png" height="512"/></a>
<a href="2018-10-10.png"><img src="small_2018-10-10.png" height="512"/></a>
<a href="2018-11-07.png"><img src="small_2018-11-07.png" height="512"/></a>
</section>
