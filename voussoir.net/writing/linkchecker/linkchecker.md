[tag:meta]

Finding and fixing dead links on this blog
==========================================

I said from the [beginning](/writing/motivations_for_writing) that gwern.net was a source of motivation for me to start writing, and I specifically linked to his article about [archiving the URLs to which his blog links](https://www.gwern.net/Archiving-URLs). It's time for me to start doing the same! I don't have quite as much to say but I thought it'd be worth documenting. Gwern just recently said he's working on a [new system](https://news.ycombinator.com/item?id=30940141).

## Archiving linked pages

To preserve third-party pages, I use a browser extension called [SingleFile](https://github.com/gildas-lormeau/SingleFile). It saves the entire page into a single .html file by using `data:` URIs to embed images and other resources. Then I just upload that file along with my own article and link to it. At the moment I am not very concerned about cloning entire websites -- I just need one page at a time.

At first I was using [web.archive.org](https://web.archive.org/) to provide archive links, but now I prefer self-hosting SingleFile pages for a few reasons:

While I expect IA to be around for a while, my goal is to reduce dependency on third parties. In some ways, depending on IA as a single third party instead of numerous third parties is better; in some ways it's worse. A single point of trust is also a single point of failure.

IA does not give the reader an easy way to download the archived page for themselves. CTRL+S does not produce a good replica in most cases. With my SingleFile pages, you can just CTRL+S and get the exact same file that I have. My goal is to share information with you, so that's kind of important.

IA might receive a DMCA takedown request and lose the content. If I want to preserve the linked page I'll need to make my own copy of it anyway, so why do both IA plus SingleFile when I can just do the one?

IA is fairly slow to load. I mean no offense to them as they are a fantastic resource and I'm okay with them prioritizing capacity over speed, but it is true.

Sometimes I need to link to a newspaper or other blogger. These articles are often [professionally written](/writing/professionally_written_article) and need to be pasteurized for consumption by a sane audience. Hosting the HTML myself allows me to do this. Here's an article [before](contently_before.html) (4.11 MB) and [after](contently_after.html) (0.14 MB) I cleaned it up [footnote_link]. Oh, and that's with SingleFile's "remove scripts" option enabled. It was 9.75 MB with scripts and I don't want to waste either of our bandwidths by including that here. I shouldn't be too harsh on them, putting two dozen paragraphs of text into a document is really hard and doing it efficiently requires a great engineering team like mine.

For what it's worth, myself and [others](https://news.ycombinator.com/item?id=30777702) have noticed that a lot of news sites today are deathly afraid of including external links in their text -- they'd rather provide a useless link to themselves than a useful link to a third party. I don't want to be like that, so I'll either include the original link alongside the archived one, or I'll edit the archived page to make its above-the-fold title a link back to the original URL.

[footnote_text] Base64 encoding of embedded resources makes them take up about a third more space, a tradeoff for the convenience of having it packed in a single html file. The original source for that article costs me about 3.7 MB over the wire.

## Fixing dead links

I wrote my own [linkchecker.py](https://git.voussoir.net/voussoir/voussoir.net/src/branch/master/linkchecker.py) because for some reason I like writing my own solutions instead of using other people's. It gives me a report organized by HTTP status and domain. If the link has a problem, it tells me what article it's on.

It immediately found multiple problematic links, [all](https://git.voussoir.net/voussoir/voussoir.net/commit/2b966be6357c073043dc2b5b64edc448a559a43b) of [which](https://git.voussoir.net/voussoir/voussoir.net/commit/9c287c719fdf9c07c098a6430fe0fb5dfcbdbadf) were [my fault](https://git.voussoir.net/voussoir/voussoir.net/commit/8224052c8cc9d79a3acf832f69fcd46a4d045552). My engineering team dropped the ball on this because they were too focused on innovating new ways to put paragraphs into documents, but the linkchecker should reduce these incidents in the future.

Actually, it's a good thing if all the dead links are my fault, because I can easily fix it. As long as I continue making SingleFile archives, the majority of dead links I encounter should be resources that I renamed or images that I forgot to upload. I should be able to run it on a cronjob and use [operatornotify](/writing/emailing_myself) to get emails about it, after I fine-tune the error / warning levels. I tend to link to a lot of youtube videos which, of course, I won't be rehosting here due to their large file size, but if it's a video I really care I'll have downloaded a copy to my personal computer and can find some way of getting it to you.

So, that's where we're at for now. If you see any other problems that I missed, you can send me an email.
