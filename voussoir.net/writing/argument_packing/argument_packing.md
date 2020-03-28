[tag:programming.python] [tag:tutorial]

Argument Packing and Unpacking
==============================

## Background

As you know, functions can accept arguments positionally:

```Python
>>> def example(a, b, c):
...     print(f'a={a}, b={b}, c={c}')
...
>>> example(4, 'hello', [0])
a=4, b=hello, c=[0]
```

or by name (aka keyword arguments):

```Python
>>> example(c=[0], a=4, b='hello')
a=4, b=hello, c=[0]
```

or both, as long as all the keyword arguments come after all the positional arguments:

```Python
>>> example(4, c=[0], b='hello')
a=4, b=hello, c=[0]
```

## Problem

It would be nice if we could have a function which can accept any number of arguments. For example, a function that adds multiple numbers at once:

```Python
>>> add(1, 2)
3
>>> add(10, 8, 12)
30
```

You could achieve this by giving the function a single parameter, an iterable. Then you can just pass in a list of whatever length you need:

```Python
>>> def add(numbers):
...     total = 0
...     for number in numbers:
...         total += number
...     return total
...
>>> add([1, 2])
3
>>> add([10, 8, 12])
30
```

But this is Python we're talking about, so surely there's a better solu--

## Solution

Right, a better solution. Python offers:

- **argument packing**: providing additional arguments into a function call, where they will be packed into a data structure.

- **argument unpacking**: providing a data structure into a function call, where the elements will be unpacked to fulfill the parameters.

### Positional Packing

With positional packing, we can pass as many positional arguments as we want into the function, and they will be packed into a tuple under a single name:

```Python
>>> def example(*args):
...     print(args)
...
>>> example(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
```

The asterisk on `*args` indicates that `args` is the packing parameter. In this context, [Ruby](<https://en.wikipedia.org/wiki/Ruby_(programming_language)>) refers to that asterisk as the "splat" operator, or you can just call it "star".

There is not very much magic going on here, it's just a regular tuple:

```Python
>>> def example(*args):
...     print(args)
...     print(type(args))
...     print(len(args))
...
>>> example(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
<class 'tuple'>
5
```

We can use this to write our addition function:

```Python
>>> def add(*numbers):
...     total = 0
...     for number in numbers:
...         total += number
...     return total
...
>>> add(1, 2)
3
>>> add(10, 8, 12)
30
```

Notice that the star is not part of the variable's name. You don't call it `*numbers` during the body of the function, only in the header.

Star-args must come after all of the other positional parameters in the definition:

```Python
>>> def example(a, b, *c):
...     print(f'a={a}, b={b}, c={c}')
...
>>> example(1, 2, 3, 4, 5)
a=1, b=2, c=(3, 4, 5)
```

```Python
>>> class Scalar:
...     def __init__(self, value):
...         self.value = value
...     def scale(self, *numbers):
...         return [self.value * x for x in numbers]
...
>>> Scalar(2).scale(4, 5, 6)
[8, 10, 12]
```

If you place any more parameters after star-args, they must be passed in by name (because if you tried to pass them in positionally, they would get lumped into the star-args):

```Python
>>> def example(a, b, *c, d):
...     print(f'a={a}, b={b}, c={c}, d={d}')
...
>>> example(1, 2, 3, 4, 5, d=6)
a=1, b=2, c=(3, 4, 5), d=6
```

```Python
>>> def scale(*numbers, scalar):
...     return [scalar * x for x in numbers]
...
>>> scale(1, 2, 3, scalar=8)
[8, 16, 24]
```

### Positional Unpacking

With positional unpacking, we can use the elements of an iterable as the arguments of a function call:

```Python
>>> def example(a, b, c):
...     print(f'a={a}, b={b}, c={c}')
...
>>> my_args = [1, 2, 3]
>>> example(*my_args)
a=1, b=2, c=3

>>> example(*[1, 2, 3])
a=1, b=2, c=3

>>> example(*range(1, 4))
a=1, b=2, c=3
```

```Python
>>> def double_sides(width, height):
...     return (width * 2, height * 2)
...
>>> a = double_sides(3, 4)
>>> a
(6, 8)
>>> a = double_sides(*a)
>>> a
(12, 16)
```

You can pass arguments in normally on either side:

```Python
>>> example(1, *[2, 3])
a=1, b=2, c=3
>>> example(*[1, 2], 3)
a=1, b=2, c=3
```

If the iterable is not long enough, you can also specify the rest by name:

```Python
>>> example(*[1, 2], c=3)
a=1, b=2, c=3
```

If the iterable is too long, you will of course get a TypeError for passing in too many arguments. But if the function has a star-args, what do you think will happen?

```Python
>>> def example(a, b, *c):
...     print(f'a={a}, b={b}, c={c}')
...
>>> example(*[1, 2, 3, 4, 5, 6])
a=1, b=2, c=(3, 4, 5, 6)
```

Did you know that the splat operator can take the elements of a nested list and make them elements of the parent list?

```Python
>>> [1, *[2, 3]]
[1, 2, 3]
```

Therefore:

```Python
>>> def example(a, b, c, d):
...     print(f'a={a}, b={b}, c={c}, d={d}')
...
>>> example(*[*[1, 2], *[3, 4]])
a=1, b=2, c=3, d=4
```

(I'm not saying you should actually do this)

### Keyword Packing

With keyword packing, we can pass as many keyword arguments as we want into the function, and they will be placed into a dictionary with the argument names as strings. We use two stars for this:

```Python
>>> def example(**kwargs):
...     print(kwargs)
...
>>> example(a=1, b=2, c=3)
{'a': 1, 'b': 2, 'c': 3}
```

Star-star-kwargs must come after all the other named arguments in the definition. The kwargs dict will only be used for arguments that aren't explicitly defined:

```Python
>>> def example(a, b, **kwargs):
...     print(f'a={a}, b={b}, kwargs={kwargs}')
...
>>> example(a=1, b=2, c=3)
a=1, b=2, kwargs={'c': 3}
```

In [Argument Forwarding](#argument_forwarding) I will show the most common usage of kwargs. Until then, there are not very many situations where I use it. I guess you could have a "secret menu" of arguments that are supported but not shown in the function's parameter list:

```Python
>>> def unassuming_storefront(**order):
...     if 'wink_wink_nudge_nudge' in order:
...         print('Say no more')
...
>>> unassuming_storefront(wink_wink_nudge_nudge=True)
Say no more
```

### Keyword Unpacking

With keyword unpacking, we can use the (key, value) pairs of a dictionary as the arguments of a function call:

```Python
>>> def example(a, b):
...     print(f'a={a}, b={b}')
...
>>> my_args = {'a': 1, 'b': 2}
>>> example(**my_args)
a=1, b=2
```

And if the function also has a kwargs?

```Python
>>> def example(a, b, **kwargs):
...     print(f'a={a}, b={b}, kwargs={kwargs}')
...
>>> example(**{'a': 1, 'b': 2, 'c': 3, 'd': 4})
a=1, b=2, kwargs={'c': 3, 'd': 4}
```

Once again, I don't typically use this feature on its own, and I'm assuming you understand how this works by now. So let's move on to the most common usage for `*args` and `**kwargs`.

### Argument Forwarding

Consider an API wrapper which makes web requests. Behind the scenes there is probably a `request` function:

```Python
def request(url):
    # does some Internet magic.

def get_comments(user):
    url = f'https://example.com/user/{user}/comments.json'
    return request(url)

def get_submissions(user):
    url = f'https://example.com/user/{user}/submissions.json'
    return request(url)
```

One day we decide to add a new argument on the core `request` function. Suppose we want to give our requests a timeout:

```Python
def request(url, timeout=None):
    # does some Internet magic.

def get_comments(user):
    url = f'https://example.com/user/{user}/comments.json'
    return request(url)

def get_submissions(user):
    url = f'https://example.com/user/{user}/submissions.json'
    return request(url)
```

Of course, when people use our API wrapper, they don't call `request` directly, they call the other functions. So in order to use the new timeout feature, we'll have to add a `timeout` parameter to all the functions which call `request` so they can pass it along:

```Python
def request(url, timeout=None):
    # does some Internet magic.

def get_comments(user, timeout=None):
    url = f'https://example.com/user/{user}/comments.json'
    return request(url, timeout=timeout)

def get_submissions(user, timeout=None):
    url = f'https://example.com/user/{user}/submissions.json'
    return request(url, timeout=timeout)
```

Great, now every time we add a new parameter to `request` we have to go copy-paste it to every other function in the entire library. Not to mention it seriously clutters up all the function definitions and may distract you from the important parameters those functions have.

It works, but it ain't cool. And why would I want to do anything that's not cool?

Instead, let's take advantage of args and kwargs:

```Python
def request(url, timeout=None):
    # does some Internet magic.

def get_comments(user, *request_args, **request_kwargs):
    url = f'https://example.com/user/{user}/comments.json'
    return request(url, *request_args, **request_kwargs)

def get_submissions(user, *request_args, **request_kwargs):
    url = f'https://example.com/user/{user}/submissions.json'
    return request(url, *request_args, **request_kwargs)
```

In this case, the end result is a little longer. But now, no matter how many new positional or keyword parameters we add to `request`, we don't have to touch the other functions ever again. Any arguments that aren't part of their own definition will simply be forwarded along to `request`.

If `request` uses any other internal functions behind the scenes (probably `urllib`), it might even forward some arguments there.

Argument forwarding is a staple of writing decorators. The wrapped function needs to support all of the args and kwargs of the original function without even knowing what they are!

```Python
import functools
import time

def timed(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        start = time.time()
        return_value = function(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(function, 'took %s' % elapsed)
        return return_value
    return wrapped
```

```Python
>>> import hashlib
>>> @timed
... def hash_it(data):
...     return hashlib.sha256(data).hexdigest()
...
>>> hash_it(b'hello')
<function hash_it at 0x04BF58E8> took 0.0005013942718505859
'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
```

It's also very useful for object inheritance, where the child class has some specific parameters and the rest of them get used in the super constructor:

```Python
class DatabaseObject:
    def __init__(self, db_connection):
        self.connection = db_connection

class User(DatabaseObject):
    def __init__(self, username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
```

```Python
>>> u = User(db_connection='just pretend!', username='exampleman')
>>> u.username
'exampleman'
>>> u.connection
'just pretend!'
```
