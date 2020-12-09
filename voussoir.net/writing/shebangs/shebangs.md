\#!shebangs
===========

## Introduction

### Windows file extensions

On Windows, the file extension of a filename is used to automatically determine how the file should be opened when you double-click on it or run it on the command line. .exe are the kings, because they are Windows's native executables. For other extensions, the shell checks the registry to find the exe associated with the extension, and runs that program with your file as the first argument, plus the rest of your arguments. For example:

- `> ipconfig.exe` → runs directly
- `> whatsmyip.py` → `python.exe whatsmyip.py`
- `> dns.py www.example.com` → `python.exe dns.py www.example.com`
- `> clock.pyw` → `pythonw.exe clock.pyw`
- `> report.doc` → `winword.exe report.doc`

If you remove the .exe extension from an executable file's name, the shell won't know what to do with it (but deeper APIs can still invoke it ([one](https://stackoverflow.com/questions/12655314/open-an-executable-file-without-an-exe-extension-with-shellexecute), [two](https://www.reddit.com/r/explainlikeimfive/comments/3iyn9a/eli5_how_do_computer_extensions_work_exe_inf_iso/culk1z9/))). That is to say, Windows does not inspect the content of files to determine their type for the purpose of double-click launching. Every file is either an exe or has an extension which maps to an exe, or has no extension and can't be associated to a program. [footnote_link]

At no time does this prevent you from using any other executable to open a file. You can always `pythonw.exe dns.py` or `winword.exe clock.pyw`. Extensions are not restrictions, they are just shortcuts to launching your executable of choice.

[footnote_text] There is also .com, a [legacy executable format](https://en.wikipedia.org/wiki/COM_file) which is natively executable, yet has a passthrough HKCR entry anyway, presumably because the shell is programmed to consult HKCR for anything that's not .exe. `HKCR\comfile\shell\open\command\(Default)="%1" %*`

### Unix shebangs

On Unix operating systems, the extension is not used to help execute the file. Instead,

1. The file must have the `x` permission, aka "executable bit", enabled by `chmod +x filename`.
2. If the file is a native executable, it will run directly. Otherwise, the system will look for the shebang. The system reads the first few bytes of the file to figure this out.

The [shebang](<https://en.wikipedia.org/wiki/Shebang_(Unix)>) is a line which must be at the very top of the file and must start with `#!`. Then, a path to an executable is given, which will actually interpret and run the remainder of the file. A Python file with a shebang might look like this:

```Python
#!/usr/bin/env python
import sys
print(sys.executable, sys.argv)
```

You can save this file using any extension you want, or no extension at all, and run it by calling `chmod +x ./filename` and then `./filename`. As always, you're welcome to pass the file as an argument to any other executable if you need to use a different interpreter.

One of the principles here is that executables become abstractions, black boxes. The idea is that as a user, when you run some `program` on the command line, you shouldn't need to know or care whether `program` is a shell builtin, or an alias, or an executable on the PATH; and you shouldn't need to care what language it's written in. You could swap out a `dns` program written in bash with one written in Python, and your callers won't know the difference.

But...

## I don't like shebangs

And you won't find a shebang on any of the code I write.

For these arguments, suppose that the file in question is checked into version control (e.g. git), or is seeding on IPFS, or is otherwise being hash-validated, or is restored to factory condition on every software/OS update, such that "just change the shebang" is not an appropriate solution. The file is handcuffed to the interpreter specified by the shebang.

My dislike for shebangs is part principle and part practical. Principles like:

- As a user, why should I be expected to agree with the developer's choice of interpreter and pathing (`/bin/x` vs `/usr/bin/x` vs `/usr/bin/env x` ...)? You can search stackoverflow and find [plenty](https://stackoverflow.com/questions/16365130/what-is-the-difference-between-usr-bin-env-bash-and-usr-bin-bash) of [discussions](https://unix.stackexchange.com/questions/29608/why-is-it-better-to-use-usr-bin-env-name-instead-of-path-to-name-as-my) about the pros and cons of each technique. But I'm the user and I'll do what I want, stop subjecting me to your chosen set of pros and cons when I'm the one running the program.

- As a developer, why should I add this boilerplate to every file I write? Why should I be encoding "this is how you run my program" in the file, when the user can simply configure their system to do it however they like best?

And practicals like:

- My `python` is really not the same as your `python`, so stop assuming `/usr/bin/env python` is the right thing.

- The shebang handcuffs also apply to hardlinks / symlinks which I might intentionally want to behave differently.

I will continue to use Python as the example language for this argument because that's what I'm most familiar with, but you may extend these issues to any case where there are alternative interpreters -- even if the alternatives haven't been invented yet!

### Developer over user (or else bye-bye checksums)

Back in the day, Python code was written in Python 2, and it was fair to assume that the executable named `python` on the PATH was the Python 2 interpreter, so people wrote shebangs pointing to `python` expecting P2. Now, code is written in Python 3 and systems are shipping with `python` referring to P3, but some P2 tools are still around and in use. So now their shebang is wrong, and will be wrong for the rest of time, and the user will always need to explicitly call `python2 program.py` for as long as they hang on to that file. Great, thanks.

On an extension-based system, the solution is easy. Although the `program.py` file might be checked into version control, there's nothing stopping me from creating a symlink or hardlink on my PATH called `program.py2` that points to the file, and an extension mapping from `.py2` to `python2.exe`. This requires no changes to the file content itself, so it won't interfere with the file's hash.

To be clear, the file layout I would use for maintaining a Python2 and Python3 program simultaneously is:

```
D:\
├───cmd\ on the PATH
│   ├───a_program.py2 => D:\software\a_program\a_program.py
│   └───b_program.py => D:\software\b_program\b_program.py
└───software\
    ├───a_program\
    │   └───a_program.py
    └───b_program\
        └───b_program.py
```

So even if `a_program.py` was written when `.py` implied Python2 instead of Python3, it doesn't matter because the names I actually execute are those in \cmd on my PATH. I can name my links any way I want to take advantage of the file extension mapping, while the real software is not affected whatsoever. See [Master of my domain](/writing/master_of_my_domain) for more about my software management practices.

Sure, you can say that nobody should be using P2 programs any more, but that's moving the goalposts. Let's say someone wants to run some particular set of Python scripts through [PyPy](https://www.pypy.org/) or [any other implementation](https://www.python.org/download/alternatives/). What then? To give one non-Python example, here is an SO thread about [the right shebang for bash](https://stackoverflow.com/questions/10376206/what-is-the-preferred-bash-shebang). To my eyes it's a disaster:

- Some people use `/bin/sh` under the assumption that all people have that symlinked to bash, which is wrong.
- `/bin/bash` or `/usr/bin/bash` might be ok, but there's no guarantee that's the path for `bash`.
- `/usr/bin/env bash` is probably most common, but there's *still* no guarantee that's the path for `env`!

On a shebang-based system, the choices are:

- Edit the shebang in the file, thus changing its hash.
- Create a symlink for the interpreter executable that matches the developer's shebang but actually points to the the user's preferred interpreter. E.g. the program expects `/usr/bin/python` so I create a symlink `/usr/bin/python => /.../python3`
- Create a separate launcher script, a one-liner shell file that calls the preferred interpreter with the script as an argument -- essentially a handwritten symlink. This option is most similar to the extension-based solution, except that if the preferred interpreter changes you've got to update all of the launcher files manually.

### Anti-Windows dogmatism

I don't like shebangs, but it's not such a big deal -- all I have to do is not use them and that's that. They pose no restrictions upon me as long as I call the interpreter myself.

What actually bothers me are the Unix elitists who in a single breath will mock Windows users as being stupid, helpless [lusers](https://en.wikipedia.org/wiki/Luser), pushed around by the Big Bad File Extension Who Dictates How Files Are Executed... then write a shebang that handcuffs their file to the name of the anticipated interpreter executable. A .rose by any other extension would smell as sweet.

To demonstrate this isn't a strawman, here are some actual quotes gathered from around the 'net:

> I know that files are identified by an identifier on their first line, which is why Linux files don't have file endings. But I liked file endings a lot. Isn't it nice to be able to tell what a file is/does without having to open it? In Windows I could open up a folder and immediately have a lot of information about the folder and the files within it, just from the file endings.

> > If you're asking if there's some kind of setting that will "show" file extensions on system files, no, that is not a thing.
> > You seem really hung up on the idea that filename extensions are a superior method of associating type information with files. Most Linux applications just don't use this method, but have other ways of determining that information. Your question is based on the assumption that this is some kind of feature which has been disabled and can be re-enabled, which is fundamentally untrue.

-

> I will not: I will not allow the ignorance that spews from Redmond to infect my software.

> I will not: I will not cater to users with a broken OS.

> I will not: I will not bother because it represents the minimal technical hurdle for Windows users.

-

> [A developer renames his `readme` to `readme.txt`]

> > While it may make logical sense to some people, the ultimate implication when you see a .txt file is that the developer uses Windows. I'm not sure a lot of developers are comfortable with that.

> -

> > No. File extensions are stupid and broken.

> > > Why? What's wrong with encoding metadata about the content in the filename?

> > > > Because it then prevents me from changing the filename the way I want to. Because legacy garbage.

> -

> > Interesting... most commenters here (so far) seem to be against the extension. Can someone explain why? "README" doesn't tell me if it's text, or markdown, or HTML, or anything. Having ".txt" lets me know the format without opening it first to see.

> > > I hate them because they're an abstraction leak. The type of a file's content is different from the application that I want to use to manipulate it, which both are in turn different from the name I chose to give the file. That current file systems and the GUI representations on top of them are so badly designed as to confuse three unrelated concepts is a failing of software and as clear an indication as you could ask for of the triumph of Worse Is Better.

These two in particular point out a problem that's already solved on Windows:

> You should not use an extension for executables, as they they are not interchangeable. Imagine that you have a shell script a.sh, then re-write in python a.py, you now have to change every program that calls your script, you have leaked an implementation detail.

-

> If you give a shell script a .sh extension, you'll have to type that .sh as part of the command name when starting it. That's the main reason why I don't like putting that extension in.

We need to talk about PATHEXT.

### PATHEXT

On Windows, there is an environment variable called PATHEXT. It contains a semicolon-separated list of file extensions that you **don't** have to type when running programs on the command line. For example, if .py is on PATHEXT, then you can just ask for `dns` on the commandline and `dns.py` will be a valid candidate. On the other hand, if PATHEXT is blank, then you must type the file extension for every executable, even .exe. At that point, the shell builtins will be the only extensionless commands you can run.

The order of extensions on PATHEXT indicates the order of preference for candidate files.

```
C:\anywhere>set PATH=C:\cmd;C:\Windows\System32
C:\anywhere>set PATHEXT=.py;.bat;.exe
C:\anywhere>where dns
C:\cmd\dns.bat
C:\cmd\dns.exe
C:\cmd\dns.py
C:\anywhere>dns
You ran dns.py!
```

```
C:\anywhere>set PATHEXT=.bat;.py;.exe
C:\anywhere>dns
You ran dns.bat!
```

```
C:\anywhere>set PATHEXT=.exe;.bat;.py
C:\anywhere>dns
You ran dns.exe!
```

```
C:\anywhere>set PATHEXT=.py
C:\anywhere>where.exe dns
C:\cmd\dns.py
C:\anywhere>where.exe dns.bat
C:\cmd\dns.bat
C:\anywhere>dns
You ran dns.py!
```

Notice I am now calling `where.exe`, since .exe is no longer on PATHEXT, thus `where` no longer matches `C:\Windows\System32\where.exe`.

```
C:\anywhere>set PATHEXT=
C:\anywhere>where.exe dns
INFO: Could not find files for the given pattern(s).
C:\anywhere>where.exe dns.py
C:\cmd\dns.py
C:\anywhere>dns.py
You ran dns.py!
```

Regardless of the value of PATHEXT, you are always allowed to specify the full name of the file, like `dns.py`. Even if `.py` is not on PATHEXT, `dns.py` itself is still on the PATH. PATHEXT only affects the evaluation of the bare name, `dns`.

And just like that, we've achieved the black box principle of executables. You can rewrite a .bat program in .py, or you can supercede a System32 exe with a script of your own. The only thing you can't do is supercede the shell builtins -- `dir` always does `dir` even if you have a candidate in the cwd or on the PATH -- you'll have to call those files by their extensioned names.

Between my public [cmd](https://github.com/voussoir/cmd) repository and my non-public cmd folder, I've got more than 180 .py and .bat files making up my command line toolkit. Of course I'm not specifying the extensions when I run them, guys.

## Hedges

It's time for me to bat for the other team and explain why Windows's solution is also bad.

### The registry

The Windows registry is not a beautiful place, and the mapping of extensions to executables is not as easy as one would hope. With Windows 10, Microsoft has introduced some new APIs for dealing with extension associations, mostly because with the old APIs, inconsiderate software developers would non-optionally dive into the registry and set their program as the default for a bunch of filetypes during install, leaving the average user without a clear understanding of how to revert. However, I haven't learned these new systems because Windows refers to them as "default apps" and I have a vendetta against the word "app" so I avoid that whole interface at all costs. When I need to edit extensions, I always just open the registry and do it myself.

The most straightforward technique that I'm familiar with is to create a key `HKEY_CLASSES_ROOT\.ext`. You can give it a `(Default)` value containing the name of another HKCR key, and this will act as a redirect for the remainder of the process. Then, beneath either the `.ext` or the redirect destination, you create `shell\open\command\(Default)="C:\myprogram.exe" "%L" %*` for the most simple invocation.

Beyond that, it's all a little confusing with keys like OpenWithList, OpenWithProgids, and values like Content Type and PerceivedType (do they do anything for files without an explicit `shell\open\command`?), and if you want to make two extensions that run the same program but have different icons (.txt, .srt, .css → text editor) you wind up duplicating the whole shell command for each of them because you can't do multiple-inheritance style mappings. Unless I'm missing something, which is also likely.

Also, there are *even more* keys in `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.ext\UserChoice`. When dealing with extensions that I didn't make myself, NirSoft's [filetypesman](https://www.nirsoft.net/utils/file_types_manager.html) helps me locate their hodgepodge of keys.

The point is that while I prefer extension-executable systems over shebang systems, that does not mean I'm praising the registry as it exists today.

### .mp3.exe

A common criticism of Windows is that non-savvy users can be tricked into downloading some file called "Hotel California.mp3.exe" and running it because they think it's an mp3 file. This is made 1,000 times worse by the unfathomable, unforgiveable, bone-headed decision by Microsoft to hide file extensions of "known file types" by default, hiding the `.exe` but leaving the `.mp3`. It boggles the mind and stupefies the senses that this default is still in place after all these years, but it is.

On Unix, the downloaded file would not be executable until you `chmod +x`, which is something you can't trick most people into doing. On Windows, the .exe requires no activation and is ready to detonate as soon as you double-click on it.

That's why UAC was added to Windows, but users will Accept any dialog box that stands between them and their mp3 without reading it, so that hasn't changed much.

## Conclusion

Let me re-quote two of the comments I shared above:

> Because it then prevents me from changing the filename the way I want to.

-

> The type of a file's content is different from the application that I want to use to manipulate it, which both are in turn different from the name I chose to give the file

These comments make a good point, that it would be nice to have the ability to associate files to programs without having to name them a certain way. Computing is still a relatively young field, and I wouldn't mind seeing new ways of solving this problem. I mentioned that I'd like to see some multiple-inheritance, which would simplify icon management, default programs, and human-friendly type names. But, by my insistence on maintaining file hashes, you can infer that I'd like a solution out-of-band from the file content itself. Current implementations of [alternate data streams](<https://en.wikipedia.org/wiki/NTFS#Alternate_data_streams_(ADS)>) are not ready to steal this stage because they aren't transmitted when sharing the file over the internet, for better and worse.

For now, I am satisfied with file extensions (as long as I wrangle the registry myself), and I want the Unix elitists to see how I use them in my favor; that they impose no friction on my workflow at all. inb4 Stockholm syndrome.
