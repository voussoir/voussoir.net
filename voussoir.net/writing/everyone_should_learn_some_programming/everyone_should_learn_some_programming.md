Everyone should learn some programming
======================================

## It's easier than you think

When people look at programming, they tend to say "That looks so complicated! I could never do that!". But you can. As long as you can describe how to do something step by step, then you have the ability to write a program. That's because writing programs is basically just writing down the steps to solve the problem, and letting the computer do it for you. You could follow the steps yourself and get the exact same result. You could even hire a bunch of schoolchildren for pennies on the dollar under the guise of "enrichment" to carry out your dastardly dictations... if you trust them to be as exacting as the computer, that is. Did you know that the word "computer" [used to refer to people who did computations](<https://en.wikipedia.org/wiki/Computer_(job_description)>)?

## Why

I think that everyone should learn some programming, but I don't think that everyone should become a "programmer". This is like knowing how to put gasoline in your car and air in your tires without being a mechanic; or knowing that protein is good for you and sugar is bad for you without being a nutritionist. Computers and digital files are now involved in just about everything we do, so being comfortable with them automatically improves your ability everywhere else. You will find that knowing a little bit of programming will suddenly be helpful in moments where you didn't expect you'd need it.

Don't think that programming is only for programmers. That's like thinking that reading is only for Literature majors. Capability with computers is the new literacy.

### Solve your own problems

Most software we use today is designed to be used by hundreds, thousands, or millions of people. The creators of the software will try to solve the most common problems of the most common users. They'll make something that works "good enough" for almost everybody, though it won't be totally perfect for almost anybody. There will be something you want to do that the software doesn't have a button for. That's your problem, and it's up to you to solve it.

If you use computers at all for work, I'm sure you'll find cases where you wish you could improve the tools you have to work with. Recently, at my workplace, I've been writing javascript bookmarklets to add feature improvements to the web-based tools we have to use, so I get things done faster and more easily. And a lot of office jobs will have you working with a slew of document files, making small changes to each or converting them to some other format. This kind of repetitive task is perfect for programming. I recently wrote about [one such example](/writing/inkscape_batch_png_pdf).

If you don't use computers for work, don't think you're off the hook. Programming will help you become disciplined in efficiency and planning ahead, and will give you a new vocabulary to express concepts you've probably already thought of. Vocabulary like latency versus throughput or bandwidth, parallel versus sequential tasks, the batching of similar tasks, and bringing down overhead. You'll notice real-life examples of abstractions and interfaces in the design and engineering of physical objects and structures.

This is not to guarantee that people will congratulate you on automating something, or promote you for doing it. But if you're working at a job you're not satisfied with, programming can turn a boring, rote, why-dont-they-replace-me-with-a-robot task into a fun puzzle that still winds up saving you time in the end. At any rate, I feel that being a strong critical thinker is its own reward while looking for something better.

I'll give some more of these down below.

### Improve critical thinking, problem solving, and what-if skills

When you give instructions to a computer, you have to be pretty specific. They don't exactly think by themselves, and they won't try to figure out what you really mean if your instructions are unclear. You can make a program called `add` that actually subtracts, and the computer won't notice or care. If you feel that computers are becoming smarter than people, and you're worried about a cyberpocalyptic android takeover of Earth, just trick your computer into saying 7+3=4 and everything will seem okay again. For a while.

This means you'll be the one responsible for deciding if the results of your program actually make sense. You'll be the one ensuring that measurements of distance don't become negative, the clock doesn't show a 61^st minute, and 7+3=10. You will encounter many unexpected problems while programming, and you will have to solve them. You will accidentally save a new version of the program while continuing to run the old one and wonder why your changes aren't making a difference. You will inadvertently swap left/right with up/down and see the world from a new, more horizontal perspective. You will gain practice in double checking not only your own work but the work of others, to figure out the exact step, possibly one of dozens, where an error was made. If you can combine these troubleshooting habits with good communications skills, you've got the makings to become a teacher, trainer, leader, or manager, wherever you are now.

As you spend more time programming, you'll find your ability to ask "what if" questions improving. In fact, it's very similar to arguing with someone and trying to poke holes in everything they say. Look for the weaknesses: This program divides two numbers; what if I type in zeroes? This program asks me for my birth year; what if I type in 9999 or HAHA? This program opens multiple urls as browser tabs; what if I give it a billion of them?

When you're the one writing the program, that means you need to predict the what-ifs that someone else [footnote_link] might try on your code, and armor up. Are you prepared to divide by zero, or deal with time travelers from the tenth millennium? This will be an exercise in recognizing your own assumptions and challenging them. This skillset will extend to your real life in the way you interpret arguments, politics, news stories, opinion pieces, advertising, and more.

This is why I have a hard time writing articles about my opinions. I am forever poised to either debunk my own claims or what-if my own thoughts, or else slather the whole article with enough disclaimers and qualifiers as to make the original point unintelligible. But this article is supposed to make you *want* to learn programming, so let's move on.

[footnote_text] You might think that if you're only writing programs for yourself to use, it doesn't matter because there is no "someone else". But just know that in six months you will totally forget how you made everything work, and you'll hope for your own sake that you made it idiot-proof.

### Increase your tech literacy

Let's talk about literacy a little more. We are in a transitional period of history. When I was younger, everyone seemed to believe that my generation and all future generations would be naturally good with computers because we've grown up with them in our lives. But, in fact, that book is now shutting as fast as it opened. More and more kids are growing up with *smartphones* in their lives, but not *computers*. That shouldn't make a difference, because smartphones are just small computers. The thing is that smartphones were invented and developed from start to finish by corporations who have realized how much money there is to be made in an industry of locked-down devices, walled gardens, and advertising-driven-algorithmically-curated experiences. To continue the literacy metaphor, today's children are growing up with nothing but picture books. Desktop computers, on the other hand, are still carrying their heritage from the before days -- the days of inspectibility, customizablilty, and programmability -- because they were designed as a tool for solving your problems rather than dominating your attention. And when I say carrying their heritage, I mean reluctantly. Microsoft, Apple, and Google would love to drop desktop programmability in favor of locked-down devices if they could get away with it. They can't, though, because of all the existing software in the world relying on existing systems. Smartphones didn't have that burden, and look where they've ended up.

Learning a little bit of programming can be a breakthrough into realizing that the world of computers is not meant to be a theme park that you just wander around in. Computers and software are made by people just like you, and you are on equal ground with them. You can be an active participant in this world and mold your tools to work the way you want. Computers were designed to do work *for you*, though corporations will gladly continue to take that power away so they can show you more ads and sell you more junk.

It is liberating to say "This program/website doesn't let me do exactly what I'd like, but that's ok, I'll just fix it myself". You'll start to notice the ways software and publishers want to disempower you, and how you can reclaim the upper hand. Oh, you won't let me right-click the image to download it? That's ok, I've got Inspect Element. Won't let me read the whole article? Let's try spoofing googlebot's useragent. This program doesn't let me choose where it gets installed or stores its files? A few filesystem junctions will put that back in its place. No more waiting around for the software gods at the temple of Goog to eventually fix what's wrong, like you have to do on your smartphone, because you can fix it now.

Throughout history, corrupted leaders have used the illiteracy of their constituents to take advantage of them. This will happen to us digitally, too, if we do not cultivate tech literacy. I do rely on the tech leaders, after all. I'm not able to manufacture my own processors or write my own operating systems, so I need your help in defending what we've got from the current trend of eroding control.

## How to start

Many aspects of computing and programming are interlinked, and it won't be possible to fully understand one part before you know many other parts too. That's okay. Become comfortable with the feeling that you don't understand everything that's going on, because it will be happening a lot. The important thing is to keep growing your web of knowledge and you'll discover how each piece links with the others.

In the beginning, don't buy textbooks. Don't enroll in courses or watch an entire video series. Don't look for a tutor. The first step is to develop your interest and a sense of accomplishment that gives you the motivation to continue. Motivation will be very important, and it comes from achievement. Solving real life problems that are relevant to you, no matter how small, are the perfect way of doing this. I guarantee that writing tiny, simple programs will feel amazing when the result is something that's actually useful and important to you. I am not saying to avoid textbooks forever, but they tend to make you do things that don't feel important yet. Save them for after you've found your footing and want to get a more rounded knowledge of programming as a subject.

Any time you find yourself thinking "doing the same thing over and over again is so boring, I wish I could do it all automatically", this is an immediate sign that you can program it.

- Moving all these jpegs into the jpeg folder is so boring, ...
- Copying all these names from emails into spreadsheets is so boring, ...
- Refreshing this store page to see when the product goes on sale is so boring, ...
- Cross-referencing the deadlines on this page with the details on this other page is so boring, ...

But don't forget to have fun. If you find yourself saying "I wish I had a way to..."

- ... count all the swear words in Tarantino's movies.
- ... put my face on every movie poster I can get my hands on.
- ... practice typing with my own sample text.
- ... get an alert whenever a new post is made on this forum / subreddit.
- ... make all the text on this page look like Runescape's `wave` or Comic Sans.

that's something else you can program for.

As I said earlier, you can write a program for anything *as long as you can describe how to do it step by step*. That means that whenever you want to write a program, the first thing you have to do is actually walk *away* from the computer and think about the problem. Talk through the steps, draw them out on paper, practice them physically, or instruct someone else to perform them as if they were your computer. Don't trick yourself into thinking you can make the computer do things that you yourself don't understand or can't describe. If you get into this mindset, you won't be able to live up to your own expectations which will kill your motivation.

As you try to describe the steps of your program, you will have to figure out how to make the computer understand what you want. You will find yourself searching the internet for "how to count words", "how to read webpage text", "how to only count each thing once", "how to save data to file", "difference between strings and ints and floats", "how to play video/audio file". You should never feel bad about looking these things up. Your job is not to become a memorization machine, but to know your problem and where to find the solution.

You will want a good text editor. I use Sublime Text 2, but I have heard good things about Microsoft's [VS Code](https://code.visualstudio.com/).

If you don't have access to a PC, but you do have an Android smartphone, try [Termux](https://termux.com/). Though, I think you'll want to plug in a real keyboard.

Programs are written in a variety of programming languages. If you want to get started with programming, I recommend the following.

### Javascript

Javascript is the language that your web browser uses to make the page interactive. There is also HTML which contains the page content, and CSS which controls how it looks.

When you first start programming, it will be difficult to write a program from scratch. Instead, it will be easier to take an existing program, make a little change, and see what happens. Keep doing that over and over again with bigger and bigger changes, and pretty soon you're writing your own program. This is how I started too.

Well, the great thing about Javascript is that every website you visit already has a program that you can modify and play with! Just right click and choose "Inspect Element", or press F12, and check out the elements, console, network, and more.

Try making [bookmarklets](https://en.wikipedia.org/wiki/Bookmarklet), which are pieces of Javascript code that you can save on your browser's bookmark bar, and then you just click them to activate it. The code goes in the place where you'd normally put the URL. For example, [this bookmarklet](https://github.com/voussoir/else/blob/master/Javascript/loopplayall.js) automatically plays any video element on the page, which is great for forums with a lot of webms, and [this one](https://github.com/voussoir/else/blob/master/Javascript/tab_renamer.js) can rename the current tab, which is great when several tabs have the same name.

Also try making .html files on your computer and opening them in your browser. It's like creating a website without actually having to create a website. For example, [this page I wrote](https://github.com/voussoir/else/blob/master/Javascript/reddit_live_new.html) shows new posts on a subreddit when they're made. You'll be amazed how simple it is to create something that could be described as a "web app".

A word of warning, though. The Javascript community has created dozens and dozens of frameworks and libraries and packages that they say you should use. Don't. For the time being, don't download anything, don't import anything, don't `require` anything. No jQuery, no React, no nothing. The default javascript tools in your browser are enough to do what you want to do. The low barrier of entry to working with javascript is a great boon, but it also means the internet is overflowing with stuff people have made and shared, and it will be too confusing to navigate it all right now. Just have fun writing what achieves your goal. Stick to the standard stuff, and search [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for how to use it. For example, here's the page on [element.innerText](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText).

### Python and the command line

[Python](https://python.org) has been my favorite programming language since I discovered it in 2014. I mentioned Javascript first because the accessibility of getting started is so much higher, but Python is where it's at if you need to write anything that isn't web browser based.

The standard library (modules and tools included with Python when you download it) are very capable so, like Javascript, you shouldn't have to worry about downloading other people's stuff to get started with the very basics.

I use Python for just about every facet of file management on my computer, like [renaming all files in a folder](https://github.com/voussoir/cmd/blob/master/brename.py), [sending files to the recycle bin](https://github.com/voussoir/cmd/blob/master/recycle.py), [clearing out empty folders](https://github.com/voussoir/cmd/blob/master/prune_dirs.py), [counting file extensions](https://github.com/voussoir/cmd/blob/master/extension_summary.py), and putting together [ffmpeg commands](https://github.com/voussoir/cmd/blob/master/ffstreams.py) that I wouldn't want to write by hand. I also [crop](https://github.com/voussoir/cmd/blob/master/crop.py), [resize](https://github.com/voussoir/cmd/blob/master/resize.py), and convert images to [grayscale](https://github.com/voussoir/cmd/blob/master/grayscale.py) or the [Windows .ico format](https://github.com/voussoir/cmd/blob/master/icoconvert.py). I love writing in Python and I hope you will too.

Once again, you can start by downloading somebody else's program and making small tweaks to it to see what happens. I find this more approachable than starting from a blank screen.

Although text editors and IDEs may let you run Python code within the editor, you will need to get comfortable with the command line to be most effective, so take the time to understand it.

### AutoHotkey

[AutoHotkey](https://autohotkey.com) is in a different category than most programming languages, but I think it's excellent for programming learners to play around with because it's quite exciting to watch your mouse cursor fly around and do things by itself. For example, I once made [an AHK script](https://github.com/voussoir/else/blob/master/AHK/clickerheroes.ahk) that would automatically click on the bonus items in Clicker Heroes, and a similar one for emptying my entire backpack into a chest in Minecraft.

The ability to create custom hotkeys really puts the Personal in Personal Computer. I have [custom volume buttons](https://github.com/voussoir/else/blob/master/AHK/volumecontrol.ahk), custom [English/Korean keyboard swap buttons](https://github.com/voussoir/else/blob/master/AHK/custom%20hangul.ahk), and a button for keeping the current window [always on top](https://github.com/voussoir/else/blob/master/AHK/current%20alwaysontop.ahk), which makes me feel like a wizard.

Also, AHK scripts tend to be short and sweet, so you don't get stuck on a particular project for too long, which is a good thing for learners. You can learn something, enjoy it, and move on.

The AHK syntax is a bit confusing, and I can never remember which of `#`, `^`, `!`, etc. I need to make my hotkey. But that's why there are [docs](https://www.autohotkey.com/docs/Hotkeys.htm#Symbols).

## That's enough reading

Go get started. Have fun.
