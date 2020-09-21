[tag:today_i_did_this]

Mobile homepage.html
====================

I'm not satisfied with the new tab page on Android Chrome. So, I put together an html file that I can use as my own homepage. Here's a comparison:

![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/mobile_homepage_html/comparison.png "left: new tab page; right: my home page")

I don't like the new tab page because:

- You only get eight links.
- You can't rename the links.
- You can't rearrange the links.
- I will never ever ever ever click to view the suggested content.
- The web servers I run on my PC are on different ports, but they keep fighting for the same spot on the new tab page.

Unfortunately, new tabs still always go to the new tab page and I have to hit the home button. So while it's not as seamless as I'd like, I can live with the one extra tap.

Here's what I did:

1. Create the html file, which is as follows:

    ```html
    <!DOCTYPE html5>
    <html>
    <head>
        <title>Homepage</title>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style>
    body
    {
        display: flex;
        flex-direction: column;
    }
    a
    {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 8px 0;
        width: 100%;
        height: 50px;
        background-color: pink;
        border-radius: 8px;
        font-weight: bold;
        font-family: sans-serif;
    }
    div
    {
        display: grid;
        grid-auto-flow: column;
        grid-gap: 8px;
    }
    </style>
    </head>

    <body>
        <a href="https://example.com">Example</a>
        <div>
            <a href="https://example.com">Example</a>
            <a href="https://example.com">Example</a>
        </div>
        <div>
            <a href="https://example.com">Example</a>
            <a href="https://example.com">Example</a>
            <a href="https://example.com">Example</a>
        </div>
    </body>
    </html>
    ```

2. Sync it between PC and phone with the amazing [Syncthing](https://syncthing.net).

3. Set it as the homepage using the url `file:///mnt/sdcard/<path>/homepage.html`. Despite the name `/sdcard/`, this is the location for Android's internal storage.

Recently, I have been trying to use Android Firefox more, since it has extension support and thus uBlock. Astonishingly, Mozilla has [removed the ability to set a homepage](https://old.reddit.com/r/firefox/comments/i5nom6/how_to_edit_homepage_on_android/), which I believe occurred as part of the [2020-08-25 update](https://blog.mozilla.org/blog/2020/08/25/introducing-a-new-firefox-for-android-experience/). And [their new tab page](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/mobile_homepage_html/firefox_ntp.png) has an even bigger thing that I won't ever ever ever click on. I'm not sure what's going on over there.
