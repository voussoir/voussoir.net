E Unibus Pluram (1993)
======================

In the early 90s, [David Foster Wallace](https://en.wikipedia.org/wiki/David_Foster_Wallace) wrote an essay called [E Unibus Pluram: Television and U.S. Fiction](e_unibus_pluram.html). It was published in the June 22, 1993 issue of [Review of Contemporary Fiction](https://en.wikipedia.org/wiki/Review_of_Contemporary_Fiction).

In honor of its 30th anniversary since publication, I've done a narration of it. FLAC, about 328 MiB:

<audio src="https://files.voussoir.net/audio/e_unibus_pluram.flac" controls></audio>

Wallace's writing is extremely dense -- I would not recommend multitasking to it -- and uses some complicated vocabulary words that I probably mispronounced, so I thought it would be nice to provide a scrolling text video to act as a simple accompaniment:

[youtube:Ehqs-Pe3Qqc]

This essay arrived to me via Will Schoder's 2016 video [David Foster Wallace - The Problem with Irony](https://youtube.com/watch?v=2doZROwdte4). This was when my interest in film was growing, my patience for advertising was shrinking, and I was seeking out more media critique.

I'm posting this article to my /writing page, primarily because I don't have a separate RSS feed for purely audio or video releases, so I feel like I need to write something here to justify it. But really, I'd rather let Wallace's words speak for themselves, and I'm just going to provide a few bullet points that come to mind insted of trying to prose it out:

- Wallace's messages about advertising are basically foundational to [my opinions today](/writing/advertixing). From the point about ads becoming more hpynotic and visually engaging so people don't change the channel, to ads mocking themselves first so that all viewer critique is second, I owe much of the time I've spent thinking about advertising to E Unibus Pluram.

- Wallace asks "What implications are there in our sustained voluntary immersion in stuff we hate?" to the audience with respect to what's shown on television, but the same question could be asked to Wallace with respect to the time he spent writing this essay, and to me for writing my advertising article, and so forth. It feels good to [criticize](https://youtube.com/watch?v=Ih6jcKd7VwU "Ratatouille - Ego's Review") and call out and debunk. But maybe we'd be happier if we took the Mr. Rogers or Bob Ross or Field of Dreams approach, putting our hours and effort into leading by example. I don't think you'll find a clip of Bob Ross tearing apart the contemporary art industry...? Obviously Wallace wrote books too, this wasn't his whole output. It's just that it's tempting to think that critique leads to enlightenment when in actuality it probably leads to misery. Here I am gushing over this piece of critique and how much smarter it has made me, rather than something else. I'm also in the aura.

- Every hour that I spend watching a movie (fictional stories of fictional lives) or a youtube video (somebody else's life, activies, travels, creations) is an hour that I am not really putting into my own life, activities, travels, or creations.

- The paragraph about the "earnest gray eminence" is one of my favorites in the whole piece. The most obvious takeaway is that a lot of media critique boils down to "it's wrong because I don't like it", and there's a kind of status-quo syndrome that assumes the world we were born into is the timeless "normal". There is another takeaway I get from this: in the short term, fictional stories are fiction; but in the long term they practically become nonfiction, documentary. Even if the characters didn't exist and the events didn't happen, the fact that the author considered them plausible enough to write essentially captures the state of the environment, culture, and technology of the time. In the distant future, that's what will matter to anthropologists.

- I do not think I have fully internalized the concept of irony as Wallace discusses it, and I do not think I would be able to competently criticize a work as being ironic. I can understand irony as sights contradicting sounds, but Wallace gives the impression that practically all media is drowning in excessive irony, which has not clicked for me yet. "Irreverent" writing and and authors "afraid of sincerity" are easier to spot: recent blockbuster movies along the Marvel and Star Wars lines have been criticized for dropping too many jokes into serious or emotional scenes, as if to say "gee, it's a good thing we're not actually feeling anything here, that would be embarrassing". But I think there is more to irony than this, which I would not spot without help.

- The last section of the essay covers George Gilder's 1990 book Life After Television, and the concept of a "telecomputer, a personal computer adapted for video processing and connected by fiber-optic threads to other telecomputers around the world". By 1990, the World Wide Web was [just about to become generally available](https://en.wikipedia.org/wiki/History_of_the_Internet), so you shouldn't interpret this as Gilder predicting the internet or digitally-encoded video, exactly. Nevertheless, it seems to me that his predictions for our applications of digital video are without fault, thirty years later. Wallace died in 2008, when video delivery over the internet was still very restricted technologically. Unfortunately, I do not think he'd be happy with where we're at. Dependence on electrified furniture is perhaps down, but dependence on electrified pocket squares is up.

- I think Wallace paints a picture in which the majority of Americans are lonely and depressed. At the top of the essay, he says that average households watch six hours of TV per day, and lonely people watch more than that. But throughout the rest of the essay he mostly drops the distinction between average and lonely and continues to use the six hours figure while treating everyone as lonely. In one paragraph, he says "Let's for a second imagine Joe Briefcase as now just average, relatively unlonely, adjusted, ...", but that only lasts for the promised second and then Joe Briefcase is right back to being lonely. Considering the fact that Wallace suffered decades-long depression, and ultimately took his own life, I think it's likely that his perceptions of the average person here were not accurate to reality, and I say that in the most well-meaning way. It is human nature to assume that most people are similar to ourself. And although I daren't be so sincere as to admit to any kind of depression, I find myself in ordinary social situations feeling just how out of the ordinary I am. The kinds of people who spend lots of time thinking about societal problems -- media, advertising, capitalism, ecology, urbanism, nutrition -- find themselves wondering *why is nobody else seeing what I'm seeing here??* or, less politely, *wake up sheeple!!*. Most people do not feel like this. The average person is probably not quite as anguished as Wallace assumes them to be. Which is not to say they are well-nourished.

Some behind-the-scenes remarks about my read-along video:

I don't make a lot of videos and I don't know what video editor would typically be considered the best for producing this kind of thing. The only video editor I have is an older copy of Adobe Premiere (from before they turned subscription-only) and it could not handle such a huge amount of text in a single text box. I of course did not want to bother with managing tens of smaller-but-still-as-large-as-it-can-handle text chunks or downloading other editors. I wouldn't be surprised if 3Blue1Brown's [manim](https://github.com/3b1b/manim) could be coerced to perform this, though, since the goal of scrolling text is so easy to define programmatically. If I needed to make a lot of these I'd probably try.

But, I don't need to make a lot of these, I just needed to make one. So, I prepared this [HTML page](e_unibus_pluram_recording.html) that scrolls by itself, and recorded the screen with [OBS](https://obsproject.com/). Yes, it took 144 minutes, but that's fine because I just set an alarm and took a nap.

To set the pace of the automatic scroll, which varies over time, I added `data-timestamp` attributes to each of the headers and several of the paragraphs to act as keyframes, and wrote javascript to choose a speed between each keyframe. I did not bother to add any seek functionality because it only needed to work once.