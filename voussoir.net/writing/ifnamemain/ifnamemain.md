[tag:programming.python] [tag:tutorial]

Python's `if __name__ == '__main__'`
===========================

This is a construct that is confusing the first time you encounter it. `if __name__ == '__main__'` is used to make a Python file that is importable by other Python files, as well as executable on its own.

## Understanding if name == main

In order to understand how it works and how to use it, there are a few background pieces of information you need to know.

1. When you are writing a program `A.py` that imports another module `B.py`, the code inside `B.py` is executed just like if you ran `B.py` by itself.

    I know that sounds simple, but it's something people don't usually think about when practicing imports for the first time. Here is an example:

    ```Python
    # hextools.py
    '''
    This library provides functions for converting to and from hex.
    '''
    def int_to_hex(x):
        '''
        Python automatically starts it with 0x which we'll strip.
        '''
        return hex(x)[2:]

    def hex_to_int(h):
        return int(h, 16)

    print(int_to_hex(4000))
    ```

    ```Python
    # myprogram.py
    import hextools

    x = int(input('Please type a number: '))
    print(x, 'in hex is', hextools.int_to_hex(x))
    ```

    Now let's run that program.

    ```
    >python myprogram.py
    fa0
    Please type a number:
    ```

    Notice that the print statement inside `hextools` is executed, and shows fa0 before `myprogram` even asks for input. Well, that's because all the code inside hextools is executed simply by importing it. When I say "all the code", I'm not saying that it calls the functions defined within that file, but I mean the `def` statements which make those functions exist in the first place and, clearly, anything else on the global scope.

2. Python modules have some special variables in the global scope that are created automatically.

    Try starting a python interpreter and calling `dir`.

    ```
    >python
    >>> dir()
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
    '__package__', '__spec__']
    >>> __name__
    '__main__'
    ```

    Ok so `__name__` is `'__main__'` but let's keep going.

    Let's start an interpreter with the `-i` flag which runs everything in the file and then gives you the repl afterward.

    ```
    >python -i hextools.py
    fa0
    >>> dir()
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__loader__',
    '__name__', '__package__', '__spec__', 'hex_to_int', 'int_to_hex']
    >>> __doc__
    '\nThis library provides functions for converting to and from hex.\n'
    >>> __name__
    '__main__'
    ```

    Well, there's that fa0 again. As you can see, there is a magical variable called `__doc__` which automatically took the docstring that I wrote at the top of the file. I'm showing that to prove that this is exactly what the variables look like while Python is executing this file. And we see the variable `__name__` which again says `'__main__'`.

    One more demonstration. Let's check that name variable again, but with an imported module:

    ```
    >python
    >>> import hextools
    fa0
    >>> __name__
    '__main__'
    >>> hextools.__doc__
    '\nThis library provides functions for converting to and from hex.\n'
    >>> hextools.__name__
    'hextools'
    ```

    Aha. So the `__name__` of my Python repl is `'__main__'`, but the `__name__` of an imported module is it's name.

Now let's combine these two lessons together. Any code that you write on the global scope will be executed when you import that file into another. But, the magic variable `__name__` will **only** say `'__main__'` when you are running that file directly, otherwise it will just say the name of the module.

Therefore, by putting code inside an `if __name__ == '__main__'`, it will only run when you are running that file directly, and it will be skipped if the module is being imported by something else. There's nothing surprising about how this works. It's just an if statement!

Let's apply that change:

```Python
# hextools.py
'''
This library provides functions for converting to and from hex.
'''
import sys

def int_to_hex(x):
    '''
    Python automatically starts it with 0x which we'll strip.
    '''
    return hex(x)[2:]

def hex_to_int(h):
    return int(h, 16)

if __name__ == '__main__':
    x = int(sys.argv[1])
    print(int_to_hex(x))
```

```Python
# myprogram.py
import hextools

x = int(input('Please type a number: '))
print(x, 'in hex is', hextools.int_to_hex(x))
```

```
>myprogram.py
Please type a number: 42
42 in hex is 2a

>hextools.py 42
2a
```

Now, `hextools.py` can be run on its own with an argument on the commandline, and `myprogram.py` can import hextools and use its functions without interruption.

Great job!

## Why doesn't Python use a main function

In some languages, like C or Java, all you have to do is define a function called `main` and it will be run when you execute the file. Why does Python use this somewhat awkward magic string variable instead?

In my opinion it's for a few reasons. Firstly, Python spans a broad range of "program formality" levels. If you just write all your code on the global scope:

```Python
# someprogram.py
import os
for filename in os.listdir():
    if os.path.isfile(filename) and filename.endswith('.temp'):
        os.remove(filename)
```

Then you're basically treating Python like bash/batch (except a million times better). In order to allow for this kind of programming, Python is already predisposed to treat files as a list of instructions to execute in order. Compare that with Java where files are more like baskets full of methods and the order doesn't matter because `main` is where things actually start running.

Consider also that in Python you can do this:

```Python
def f():
    print('hello')

f()

def f():
    print('world')

f()
```

```
hello
world
```

Which you can't do in a language like C or Java.

```C
int f()
{
    return 1;
}
int f()
{
    return 2;
}
```

```
main.c:7:5: error: redefinition of 'f'
int f()
    ^
main.c:3:5: note: previous definition is here
int f()
    ^
```

```Java
class Main {
    public static int f()
    {
        return 1;
    }
    public static int f()
    {
        return 2;
    }
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

```
Main.java:6: error: method f() is already defined in class Main
    public static int f()
```

And then there's Javascript, which I guess must do a parsing pass before running but doesn't complain about redefines.

```Javascript
function f()
{
    console.log("hello");
}

f();

function f()
{
    console.log("world");
}

f();
```

```
world
world
```

But anyway. On the opposite end of the formality spectrum, you can write Python files where everything is tucked away into classes and functions and the file is designed as an import with no regard for command-line usage of that particular file. Well, if Python already has the predisposition to just run all the code on the global scope, why should there be a separate parsing mode, and how would it know which one to use?

That's not to say I love `if __name__ == '__main__'`. I would prefer to have a separate `__main__` magic variable that is True or False, then you can just `if __main__:`. The `__name__` string is still fine for other purposes, like printing the module to the screen.


As a matter of fact, whenever I upgrade a Python script from quick prototype to reusable code, I always move the main code into a C-like function called `main` via this template:

```Python
def main(argv):
    # At this point I usually do my argparse
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
```

That's because if you make any variables inside `if __name__ == '__main__'`, they will be part of the global scope which may have accidental side effects. For example:

```Python
# bad.py
import sys

def int_to_hex():
    return hex(x)[2:]

if __name__ == '__main__':
    x = int(sys.argv[1])
    print(int_to_hex())

# Great, everything's ready to ship!
```

Spot the error.

Whereas by creating a main function, any variables in `main` are local variables and are not accessible outside of it.

## Real-life examples.

I understand that the examples shown here are very simplistic. Here are some links to my other programs which use ifmain in a purposeful way.

- [bytestring](https://github.com/voussoir/voussoirkit/blob/417c14a02338d10a34fdf4875761c9e4a92aef1c/voussoirkit/bytestring.py#L127) is imported by many of my other programs, but also is very useful on its own.
- [epubfile](https://github.com/voussoir/epubfile/blob/4f44cd642f04f1dc94b1d65c5a52f5f639460276/epubfile.py#L1657) can be imported into any program that wants to modify epubs, but has a number of builtin utilities that run from ifmain.

In a very large project with many files, it's more likely that you'll have a main launcher file, and none of the internals are very useful to run on their own. ifmain essentially bridges the gap to make single Python files useful as imports and standalone utilities.