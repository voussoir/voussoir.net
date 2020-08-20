[tag:python] [tag:tutorial]

Running Python scripts
======================

In this document, `C:\python` is the folder where you installed Python to. That's where `python.exe` lives. `C:\code` is a folder you created where you put all the `.py` files that you make. Lastly, `C:\anywhere` is anywhere else on your computer that is not one of these two locations.

I am using Windows style prompts with `cwd>`. For Linux users, this is the same as your `user:cwd$ `.

## Level 0: `python.exe myfile.py`

In this level, you are specifying the exact location of the Python executable and the exact location of the script.

`C:\python> python.exe C:\code\myfile.py`

`C:\code> C:\python\python.exe myfile.py`

`C:\anywhere> C:\python\python.exe C:\code\myfile.py`

## Level 1: `python myfile.py`

In this level, you are letting the system find Python, but specifying the exact location of the script.

When you install Python, there is an option to add Python to your PATH. The PATH is a list of directories that your computer will search every time you type a command on the command prompt. This means that when you type `python`, it will automatically find the python.exe in your installation folder. Windows users, type "environment variable" into your Windows search bar to open the settings menu and find the variable called PATH, or `echo %PATH%` on the cmd to see what it looks like. Linux users, `echo $PATH`.

`C:\code> python myfile.py`

`C:\anywhere> python C:\code\myfile.py`

## Level 2: `myfile.py`

In this level, you are specifying the exact location of the script, but do not mention Python at all, because the system knows it is a Python file.

**Windows:** Ensure that `.py` file extensions are associated with the python.exe or py.exe that you installed. This should happen automatically when you install Python, and you can always re-run the Python installer to reset these associations if they become broken.

`C:\code> myfile.py`

`C:\anywhere> C:\code\myfile.py`

**Linux:** Add a shebang for your Python executable to the top of the script file, and mark the file as executable with `chmod +x myfile.py`.

`/code$ ./myfile.py`

`/anywhere$ /code/myfile.py`

## Level 3: `myfile.py` on the PATH

In this level, you do not need to specify the exact path of the script ever.

Add the directory that contains the script, `C:\code`, to your PATH. Remember that PATH is a list of directories, not files. If you add `C:\code\myfile.py`, it won't work. You have to add the directory.

`C:\anywhere> myfile.py`

## Level 4: `myfile`

The final level is to run Python scripts without specifying Python, or the extension, or the file's location. At this level, Python scripts feel like native commands such as `dir`, `ls`, and `cd`.

**Both**: Add the directory that contains the script to your PATH.

**Windows**: Add `.py` to your PATHEXT variable, so Windows will understand that when you type `myfile`, it should also search the PATH for `myfile.py`. Use `where myfile` to double check that your file appears, and there is not another program with the same name taking priority.

**Linux**: Keep the shebang at the top of the file, and rename the file to remove the `.py` extension. Use `which myfile` to double check that it is the top result.

`C:\anywhere> myfile`

The only way to get better than this is to have a mind-controlled computer where you don't have to type anything.
