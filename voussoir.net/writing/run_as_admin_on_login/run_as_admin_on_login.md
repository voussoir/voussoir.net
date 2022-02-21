[tag:windows]

Run as Administrator on login
=============================

I have a few long-running / daemon programs that I would like to "run as administrator" automatically when I start my computer, without UAC prompts. The programs are not available as Windows Services.

First, I tried placing an lnk shortcut in the Startup folder [footnote_link] with the "Run this program as an administrator" box checked. However, this didn't work, and I found that the program simply didn't start at all.

![](lnk_properties.png)

My next attempt was to use the Task Scheduler:

![](tasksched_1a.png)

![](tasksched_1b.png)

![](tasksched_1c.png)

This worked, but the problem was that the task would be permanently stuck in the "task is currently running (0x41301)" state. So, I instead told the task scheduler to start cmd.exe with a command that immediately launches the real target program:

![](tasksched_2.png)

This solved the state problem because the cmd.exe finishes immediately, and that's all the task cares about.

The final problem was that the program would become slower and slower and slower over time. After a day of computer uptime, the program would be unusably slow. I found the solution to this problem [here](https://vnote42.net/2021/04/29/windows-scheduled-tasks-get-slower-over-time/), which explains that scheduled tasks are started with below normal process priority. The fix (copied here for preservation) was:

1. Export the task to an xml file.
2. In that xml file, replace `<Priority>7</Priority>` with `<Priority>4</Priority>` and save it.
3. Delete the task from the Task Scheduler UI.
4. Re-import the task from the xml file.

[footnote_text] `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`
