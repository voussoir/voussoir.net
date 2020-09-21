[tag:git] [tag:meta] [tag:today_i_did_this]

Lying git history
=================

## Introduction

When I started writing these articles (you know, 2 weeks ago), I decided to put them into subdirectories for broad categories: `python`, `life`, and `computers` are what I had so far. For example, `/writing/life/friction`.

Because this site is statically generated from the directory tree, moving files and folders around would change their URL, so once I put an article into a category it would be stuck there unless I was willing to break the link. The reasoning for making category folders was:

- Keeps the main /writing directory cleaner.
- If I write an article about Python's `continue` statement as `python/continue`, I could later create `java/continue` if need be. I wouldn't have to cautiously prefix every article like `python_continue`.

Today, however, I decided that the cons outweighed the pros because:

- I already have a tag system, with which I can add and remove tags freely [footnote_link].
- The chance of me reusing names like that is low. For life articles, I could amend the original or come up with a new name; for programming articles, why would I need anything other than Python?
- If I make categories too broad and want to split them, I won't do so for fear of breaking links.
- If I make categories too narrow and only have a single article in them, I may want to lump it into a bigger one but won't do so for fear of breaking links.
- I don't want to waste time with nginx rewrite rules or generating duplicates of the output files so that articles can be read with and without the category in the url.

So I decided to move everything out of the category dirs. Since this site is new and nobody has any links to it yet, it's better to break them now and get it over with. But because git history and commit timestamps are central to my publishing model, I needed to keep that intact or else lose all this soon-to-be-nostalgic early history.

There are plenty of tutorials on the internet for modifying git history. This is just a short description of what I did today in case I needed to do it again sometime so I'll have a reference.

[footnote_text] I do think category systems can have a place alongside tags. Will expand on this in the future.

## Backup

I zipped up the repository so even if I mess everything up I could extract it back and start over.

## Windows users, use git bash

The commands used in the following steps will use `sed` and linux style environment variables and linux style single quotes around some commands, so Windows users should run `bash.exe` which is located alongside `git.exe` in your git installation folder.

## filter-branch to modify paths

The original paths were like `/writing/life/friction/friction.md` and I needed to turn them into `/writing/friction/friction.md`. Just needed to replace /life/, /python/, and /computers/ with /.

I found [this stackoverflow answer](https://stackoverflow.com/a/3063008) which quotes a premade snippet from the docs:

> To move the whole tree into a subdirectory, or remove it from there:

> ```
> git filter-branch --index-filter \
>         'git ls-files -s | sed "s-\t\"*-&newsubdir/-" |
>                 GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
>                         git update-index --index-info &&
>          mv "$GIT_INDEX_FILE.new" "$GIT_INDEX_FILE"' HEAD
> ```

The SO comments mention that using hyphen as the sed separator is flaky so I went ahead and used `#` instead without even trying `-`. I assume the escaped `\"` is for filepaths with spaces, but it didn't help in my case so I removed it. For me, the command was was:

```
git filter-branch --index-filter \
        'git ls-files -s | sed "s#/life/#/#" | sed "s#/python/#/#" | sed "s#/computers/#/#" |
                GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
                        git update-index --index-info &&
        mv "$GIT_INDEX_FILE.new" "$GIT_INDEX_FILE"' HEAD
```

**Since filter-branch is dangerous, make sure to test out the `git ls-files -s | sed` commands separately first.**

However this was raising an error during the final `mv` step because the index.new file referenced by the variable didn't exist. I'm not sure if it was supposed to exist already since the snippet from the docs doesn't mention it. I found [this SO answer](https://stackoverflow.com/a/46677910) saying to just add `; /bin/true` to just ignore that, so the final error value is 0 and git doesn't abort.

```
git filter-branch --index-filter \
        'git ls-files -s | sed "s#/life/#/#" | sed "s#/python/#/#" | sed "s#/computers/#/#" |
                GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
                        git update-index --index-info &&
        mv "$GIT_INDEX_FILE.new" "$GIT_INDEX_FILE"; /bin/true' HEAD
```

This worked and now all the paths were correct. But the articles themselves contained links that I needed to fix.

## rebase -i to edit existing links

I used `git rebase -i commithash` where commithash was just before the earliest case of an article that contained a link. I set commits to `e` if they involved an article that had a link.

Rebase `e` performed the commits in question -- adding or editing the article -- and then paused the rebase so that I could edit the link in the article to just `/writing/friction`, then do a `git commit --amend` so the change became part of the commit as if it was correct all along.

This left authorship dates intact but set commit dates to be the current time.

## rebase again to reset commit dates

Rebase has a flag called `--committer-date-is-author-date` to copy the author date to the commit date, which is what I needed. For some reason this cannot be used with `-i` simultaneously, but simply running a new rebase with this flag and no other changes fixed it up.

```
git rebase --committer-date-is-author-date commithash
```

Then to publish,

On my side:

```
git push origin master --force
```

and on the server side:

```
git fetch --all
git reset --hard origin/master
```
