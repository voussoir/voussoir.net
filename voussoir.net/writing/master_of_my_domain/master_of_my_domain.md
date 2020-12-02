Master of my domain
===================

## Introduction

This article is about how I manage the software on my computer to stay organized and in control. I've developed these habits over years of dealing with software installations that each want to behave a little differently and go their own way. But I'm the master of my domain -- queen of my castle, if you will -- and I run the show around here. So here's how I put software in its place:

## Prefer portable over installers

If a software download page offers a choice between "portable"/.zip/.7z downloads and "setup"/.exe/.msi downloads, always pick the portable option. The reason they're called portable is because you can unzip them to a flash drive and just run the .exe on any computer you plug it in to, so that you don't have to actually install the program on every computer you use.

As a result, a well-behaved portable program will:

- Store configuration files in the same folder as the .exe, instead of computer's central registry or other paths.
- Not rely on files outside of the program's folder -- the whole thing is self-contained.
- Not leave much, or anything, behind on the main computer -- usually just some log files in appdata.

These properties are what I want from *all* software! The benefits even for non-portable use are many:

- Easy to find and modify config files by hand -- no hunting for registry keys or configuration paths.
- Easy uninstallation procedure -- just delete the folder.
- Easy to run multiple simultaneous instances of the program, even of different versions.
- Easy to back up with confidence -- just zip the folder. No worries about missing important files anywhere else.

There is even a website, [portableapps.com](https://portableapps.com/apps), dedicated to promoting portable software and preparing portable-ized versions of software that isn't normally available as portable. In the second case, however, you rely on portableapps being trustworthy.

Ostensibly, the benefits of installers over portables is they can set file associations, integrate with the right-click menu, and so forth. Well, I can handle file associations myself (`HKCR\.ext\shell\open\command\(Default)`), and even the most well-meaning context menu items really just contribute to an ever-growing list of junk so I'd rather not have those anyway. I can write those myself, too, if I really need them (`HKCR\.ext\shell\mycommandname\command\(Default)`). Then I'll know exactly where they're defined should I ever decide to remove them. This is in contrast to properties set by installers which are always in crazy places and mapped through GUIDs and whatnot.

## With installers, always choose your directory

Some software isn't available as a portable download, so you've got to suffer through the installer. If it gives you the opportunity to change the install directory, always take that chance. Software installers on Windows have a nasty habit of scattering themselves throughout `C:\Program Files`, `C:\Program Files (x86)`, `C:\ProgramData`, and `%appdata%`. I'm king of this county and I hereby declare that I'm not gonna go on a wild goose chase looking for MY software on MY computer -- they'll go where I tell them to go.

If I have to install a program from an installer, I'll usually try to zip up the resulting folder and keep that as my own portable copy for later. A lot of installers are nothing more than extractors, so as long as the program doesn't rely on some system changes during install, keeping the portable copy works fine (besides, system changes are often anti-user anyway). And I really don't need an installer acting as a glorified file extractor, I can do that myself from a zip.

Some software authors take this [Lèse-majesté](https://en.wikipedia.org/wiki/L%C3%A8se-majest%C3%A9) a step further by not even offering a chance to change the install directory. There is no justifiable reason for this. I operate on a two or three strikes policy depending on how important the software is: I expect simply moving the installed folder, possibly leaving a junction in its place, to work properly. But now that the program is on my bad side it takes a lot less for me to uninstall.

The worst offenders are the likes of Adobe. A search on my computer right now shows:

```
C:\Program Files\Adobe
C:\Program Files\Common Files\Adobe
C:\Program Files (x86)\Adobe
C:\Program Files (x86)\Common Files\Adobe
C:\ProgramData\Adobe
C:\Users\All Users\Adobe
C:\Users\voussoir\AppData\Local\Adobe
C:\Users\voussoir\AppData\LocalLow\Adobe
C:\Users\voussoir\AppData\Roaming\Adobe
C:\Users\voussoir\AppData\Roaming\Adobe\Adobe
C:\Users\voussoir\Documents\Adobe
C:\Users\Public\Documents\Adobe
```

You're not the lord of this manor, Adobe!

## Separate subdirectories for each version

My Software folder looks like this, with a subdirectory for each version of every program:

```
D:\Software\Git\2.25.0
D:\Software\Inkscape\0.92.3
D:\Software\QuiteRSS\0.19.4
D:\Software\WinSCP\5.17.8
```

This way, I can maintain multiple versions of the software at the same time, which makes updating totally stress-free because I can stick with the old version as long as I want if the update has a regression. Contrast that with an in-place updater where you might regret the update after finding a new bug. My Android phone has several apps that I simply don't bother to update because I don't want to deal with reverting the .apks by hand through adb should I regret the update [footnote_link].

The only problem occurs when multiple versions expect `%appdata%\Program` to belong to themselves alone. If there is no commandline switch to change the appdata directory, I am somewhat out of luck on that point. One thing I had never though of until now is modifying the environment variables before running the program to manipulate `%appdata%` to a separate directory, similar to [this SE thread](https://superuser.com/q/424001). However, that solution didn't work for me, but I'll keep an eye out for something similar. This seems fragile since the program might (wrongfully) construct appdata from `%userprofile%\appdata\roaming`, or cache the value of `%appdata%` during install to a registry key, etc.

[footnote_text] [F-Droid](https://f-droid.org/) offers historical apks for download so I've got no concern there, but Google doesn't. [Raccoon](https://raccoon.onyxbits.de/) can help you download present-day apks from Google for your future benefit, though.

## Use 'latest' junctions for program shortcuts

Here's a fantastic trick I started using just recently. Since all my software is separated by version number, when I download the newest version of a program, all of my shortcuts or scripts which call that program will still be using the old path, and I'd have to update them manually. I came up with this solution: just `mklink /j __latest X.Y.Z` inside the program folder, and have all your shortcuts point to the exe inside `__latest`. Since it's a filesystem junction, it will behave transparently to any calling program. In the past I had tried to achieve this by making a single shorcut and pointing any future shortcuts to that one, but that didn't work because when you assign a shortcut to a shortcut it resolves to the real path and saves that path forever instead of folowing the link every time.

When I download a new version of a program, I just delete that junction and make it again with the new version number, and all linked paths work as normal, as long as the name of the .exe itself hasn't changed.

I don't like filling up my desktop or start menu with shortcuts, so I wrote [PGUI](https://github.com/voussoir/cmd/blob/master/PGUI.pyw) which acts as a launcher for any .lnk files located inside my PGUI folder. Each of these shortcuts actually point to the `__latest\program.exe` path. As a bonus, my PGUI folder is one of the few folders to enjoy the honor of being on my PATH, which means I can just start them from the command line or Win+R -- that's all possible without a gui launcher of course, but it's a great symbiosis.

![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/master_of_my_domain/latest_junction_1.png)

![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/master_of_my_domain/latest_junction_2.png)

## Reserve PATH for nobility only

The entire contents of my PATH are:

```
C:\Windows
C:\Windows\system32
D:\cmd
D:\git\cmd
D:\git\cmd\PGUI
```

Two folders for system executables, and three folders owned by ME, because this is a monarchy and I'll appoint whoever I want. No application, under any circumstance, gets to put its own install directory on the PATH. If I need global commandline access to that program, I'll put an .lnk or symlink in \cmd.

At one point, I had some issues with programs that I wanted to subprocess from Python. `subprocess.run(shutil.which('ffmpeg'))` was breaking because `subprocess.run` wants to receive executable files and of course the only thing on my path was an .lnk. So, I wrote [winwhich.py](https://github.com/voussoir/voussoirkit/blob/master/voussoirkit/winwhich.py) and now that problem is solved. The software bends to my will, not the other way around.


## Use junctions to reign in appdata

I've mentioned that even portable software has a tendency to leave a few traces in `%appdata%`. Sometimes it's inconsequential stuff like log files, but sometimes it's config, and that I want to keep in the program folder.

The solution here is in three steps:

1. Move `%appdata%\Program` into `D:\Software\Program`.
2. Rename that folder to e.g. "appdata" so you don't have Program\Program like some kind of Adobe.
3. `mklink /j "%appdata%\Program" appdata`.

Now you are closer to portable enlightenment and can zip up the program folder without losing your appdata files.

## Back up your software

Although I run regular backups, I don't include my whole Software folder in the backup routine because I already keep all the portable zips and installers backed up separately. The only items of value in the install directory are config files, most of which are not highly personalized and I don't mind losing either.

But, there are a few programs which I've heavily configured and I'd hate to start from scratch with them. Sublime, Putty, and WinSCP for example. For those I wrote a script [backup_folder.py](https://github.com/voussoir/cmd/blob/master/backup_folder.py) which uses [rarpar.py](https://github.com/voussoir/cmd/blob/master/rarpar.py) to create highly compressed archives with a datestamp in the filename. Because the `__latest` files will be included in duplicate, you might think it'd waste a lot of space, but with a Solid archive and a very high dictionary size, that duplication causes no extra disk usage.

## Dealing with uncooperative software

If you find that one of your programs isn't cooperating with the above techniques, consider these more delicate approaches:

- Say in a loud, commanding, and controlled voice, "***YOU WORK FOR ME***" (requires microphone).
- Spawn several child processes. Kill them.
- Reduce process priority to Below Normal and insist, "You can have your cycles back after you've cleaned up your act".
