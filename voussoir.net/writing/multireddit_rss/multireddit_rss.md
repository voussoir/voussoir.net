RSS from private multireddits
=============================

The RSS URL for a multireddit is `https://www.reddit.com/user/username/m/multiname/new.rss`. But, putting this into your RSS client without making the multi public will yield a 404.

On [reddit.com/prefs/feeds](https://old.reddit.com/prefs/feeds/) you'll find some RSS links that use a static token in the URL to act as the authentication, so you don't have to provide login credentials in your client. It turns out, the token is the same for all of the feeds, and you can use it on the multireddit feed too.

Just use `https://www.reddit.com/user/username/m/multiname/new.rss?feed=XXXXXXX&user=username` and you're good to go.

Since a single multireddit can aggregate up to 100 subreddits, you can save yourself and reddit up to 99 web requests per refresh by doing it this way.
