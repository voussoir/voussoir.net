Sublime Text as EDITOR
======================

I use Sublime Text as my `EDITOR` environment variable and as my git editor. I used ST2 for many years and recently jumped to ST4, skipping 3. But something has changed along the way, or maybe it was always a little imperfect.

Between Sublime's workspaces and project sessions and hot-exit files that allow you to close with unsaved changes, there is quite a lot of state saved to disk. I found myself getting frustrated at the various incantations of `sublime_text.exe -n`, `sublime_text.exe -n -w`, `subl.exe -n -w` because they recalled the previous state and opened a bunch of tabs or windows when I just wanted to do a single git rebase.

![](bad1.png)

![](bad2.png)

[Here is a forum thread](https://forum.sublimetext.com/t/disable-automatic-loading-of-last-session/4132/10 "Disable automatic loading of last session") where other people have the same problem, and they mostly discuss workarounds through config files. I didn't want to make any of those changes because I like having all my tabs restored in 99% of cases, just not for temporary `EDITOR` purposes.

Then I realized something that I should have realized a long time ago because I'm the one who's always going on about it: Sublime is [portable software](/writing/master_of_my_domain). I can just make a copy of the folder. And I did. And it's great.

Now, I have `C:\Software\Sublime Text\4133` and `C:\Software\Sublime Text\4133_EDITOR`, and I can configure them independently. For the EDITOR copy, I can remove all project folders, disable a lot of UI elements, turn off state-saving, and uninstall unnecessary packages.

![](good1.png)

![](good2.png)

My `EDITOR` environment variable is `C:/software/sublime text/4113_EDITOR/subl.exe -n -w`.

My .gitconfig contains:

```
[core]
    editor = 'C:/software/sublime text/4113_EDITOR/subl.exe' -n -w
```

My WinSCP editor is `C:/software/sublime text/4113_EDITOR/sublime_text.exe -n !.!`.

Use portable software, folks.

P.S. I found that the `-w` flag only waits if you also provide a filename to edit on the command line. `subl -w` does not block, but `subl -w myfile.txt` does block. This made me confused while I was testing everything.
