git.voussoir.net
================

Github has been bothering me. I don't like their [drunk-on-buzzwords marketing copy](lets_build_from_here.html) or the [advertisements they're placing above my work](copilot.png). If I give someone a link to my work, I want to feel proud of it.

So, I installed [Gitea](https://gitea.com) on my server and uploaded everything to [git.voussoir.net](https://git.voussoir.net). This was easy because I have no investment or dependency on github's issue tracker, project tracker, wiki, pages, CI, Actions, or whatever other proprietary lock-ins they offer. I will need to move some image assets eventually and that's about it.

I had tried [Gogs](https://gogs.io/) at first, but it was failing on every push with a [502 error](gogs_502.png) that I couldn't diagnose.

I followed Gitea's [installation from binary](https://docs.gitea.com/installation/install-from-binary) instructions and updated my nginx settings. From start to finish, the process took maybe an hour and a half, which was a little longer than it should have been because gitea was trying to do some mkdir in `/usr/local/bin/data/tmp` even though I asked it to use a different path. I had to manually set `APP_DATA_PATH` in the `.ini` file to make it stop doing that, and now it's fine. Even if I accidentally explode the whole server somehow, I can just reinstall gitea from scratch and push it back again. I *still* don't plan to use the issue tracker or whatever CI they come up with. I am deliberately calling it git.voussoir.net instead of gitea.voussoir.net in case I change the backing software.

...

Just a week after setting up Gitea, I learned that Gitea made a controversial move last year in forming a for-profit entity, and a new non-profit fork called [Forgejo](https://forgejo.org/faq/#why-was-forgejo-created) has started. I haven't personally being slighted. I just got here. But the words "non-profit" are like catnip to me so it looks like git.voussoir.net runs Forgejo now. Wow, my foresight paid off!

I won't delete my github account in the foreseeable future, because it's free and easy to keep pushing to all remotes. But github is losing my favor, and that's great for them too because I'm a nobody and I wasn't paying them anyway. So long, and thanks for all the fetch.

Note: If you want to keep it even simpler than this, git does have a web UI built in. See [gitweb](https://git-scm.com/book/en/v2/Git-on-the-Server-GitWeb).
