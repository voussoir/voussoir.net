[tag:programming.python] [tag:tutorial]

Continue
========

## What is it

`continue` is a keyword used to control `for` and `while` loops. It skips the rest of the current iteration, and starts the next one. This is different from `break` which ends the entire loop.

## Using it

This loop skips the number 3:

```Python
>>> for x in range(6):
...     if x == 3:
...             continue
...     print(x)
...
0
1
2
4
5
```

Here, a bit more verbose:

```Python
>>> for x in range(6):
...     print(f'{x} is above the continue')
...     if x == 3:
...             print(f'{x} is getting skipped')
...             continue
...     print(f'{x} is below the continue')
...
0 is above the continue
0 is below the continue
1 is above the continue
1 is below the continue
2 is above the continue
2 is below the continue
3 is above the continue
3 is getting skipped
4 is above the continue
4 is below the continue
5 is above the continue
5 is below the continue
```

This loop skips any directories that can't be `listdir`'ed:

```Python
for directory in directories:
    try:
        filenames = os.listdir(directory)
    except PermissionError:
        continue

    for filename in filenames:
        ...
```


### Continue is great for cleaning code with lots of conditions

If you're trying to perform an action on items that meet multiple criteria, you will either have to nest the conditions:

```Python
for submission in submissions:
    if submission.author is not None:
        if not submission.over_18:
            if 'suggestion' in submission.title.lower():
                print('Found:', submission.id)
```

or group all of the conditions into a single statement or boolean variable:

```Python
for submission in submissions:
    if (
        submission.author is not None
        and not submission.over_18
        and 'suggestion' in submission.title.lower()
    ):
        print('Found:', submission.id)
```

But, with continue, we can achieve the same result in a more simple way:

```Python
for submission in submissions:
    if submission.author is None:
        continue

    if submission.over_18:
        continue

    if 'suggestion' not in submission.title.lower():
        continue

    print('Found:', submission.id)
```
        
Notice that all of the conditions are the opposite of the originals. The mentality changes from "keep only the items with the right properties" to "discard the items with the wrong properties". This usage of continue is often called a "guard clause".
