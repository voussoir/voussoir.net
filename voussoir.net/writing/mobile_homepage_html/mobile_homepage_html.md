[tag:today_i_did_this]

Mobile homepage.html
====================

I'm not satisfied with the new tab page on Android Chrome. So, I put together an html file that I can use as my own homepage. Here's a comparison:

![](comparison.png "left: new tab page; right: my home page")

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

3. Set it as the homepage using either `file:///storage/emulated/0/<path>/homepage.html` or `file:///mnt/sdcard/<path>/homepage.html`. Despite the name `/sdcard/`, this path should correspond to internal storage.

  **Note:** With Android 10's new scoped storage permissions, you may get a permission denied error while opening the page. Your first option is to place the file inside the `Android/data/com.android.chrome` folder. E.g., an absolute path of `file:///storage/emulated/0/Android/data/com.android.chrome/homepage.html`.

  Alternatively, I was able to bypass the scoped storage system altogether with this [ADB](https://developer.android.com/studio/command-line/adb) command: `adb shell sm set-isolated-storage off` which **rebooted the phone immediately** and may have other consequences. I am not sure how it fares on Android 11.

Recently, I have been trying to use Android Firefox more, since it has extension support and thus uBlock. Astonishingly, Mozilla has [removed the ability to set a homepage](https://old.reddit.com/r/firefox/comments/i5nom6/how_to_edit_homepage_on_android/), which I believe occurred as part of the [2020-08-25 update](https://blog.mozilla.org/blog/2020/08/25/introducing-a-new-firefox-for-android-experience/). And [their new tab page](firefox_ntp.png) has an even bigger thing that I won't ever ever ever click on. I'm not sure what's going on over there.
