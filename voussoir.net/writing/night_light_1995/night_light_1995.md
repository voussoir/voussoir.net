Night Light (1995)
==================

## Introduction

When I was a kid, one of the computer games I played was Night Light, by GTE Entertainment. It's about Pandora the cat and Pixel the dog exploring the house in the dark after all the people have gone out for the night.

![](cover.jpg)

This game stuck in my memory in the way that only a formative childhood game can. There is something about the game mechanic of using the mouse as a flashlight that's very appealing to me, though of course I don't know if this is cause or effect.

For the past several years, I have occasionally been reminded of the game and tried to search for it online, only to come up empty handed. Finally, in 2018, a youtuber named Vulnerose Plays [did a playthrough](https://www.youtube.com/watch?v=KYDoBcFcGM8) and also [uploaded the ISO](https://archive.org/details/NightLight_201809) to the Internet Archive. The majority of comments on that video are from other people saying they'd been searching high and low for the game, too.

At the time of this writing, I have not actually played the game using the provided iso, as it would require me to emulate an older version of Windows and I haven't gotten around to doing it yet. But, I [recently](/writing/browser_in_the_dark) had the inspiration to reproduce the basic mechanic using javascript canvas, and that brings us to today.

## Extracting the assets

I think some readers might be interested to know how I got the images out of the game without playing it, so I'll walk you through a bit of that here.

I used [7-zip](https://www.7-zip.org/) to open the .iso file and browse the contents. Sometimes, you'll find that a game's assets are embedded into the .exe itself, and that makes things more difficult. Graciously, this game has the majority of its assets laid out in folders as separate files, which is great. It's not too hard to find a LIGHT.BMP and DARK.BMP for each level.

![](7z_bmp.png)

These images are 512x344, and they've got a hardcoded shadow underneath the game's HUD. But what are those megabyte-sized .mov files?

<center><video controls src="garg_dark_tiles.mp4"/></center>

These video files contain 80 frames, each a tile of a larger image. I used ffmpeg to take the video frames apart, with `ffmpeg -i DARK.MOV %03d.png`.

![](ffmpeg_mov_to_png.png)

![](frames.png)

The first 16 frames can be stitched together in a 4x4 grid to produce a 1024x688 image, and the last 64 frames can be stitched 8x8 to produce a 2048x1376 image. It's quite astonishing to see these levels in such high resolution after all these years.

I deleted 01-16 from each folder, then updated my [stitch.py](https://github.com/voussoir/cmd/blob/master/stitch.py) to take a `--grid` argument, and stitched the remaining 64 images together for each level.

![](stitch_8x8.png)

![](all_stitching.png)

I also extracted the audio clues and converted them to flac. Unfortunately, lots of the source files were corrupted, with an excess of zero bytes making them impossible to decode.

![](hxd.png)

I wrote [ffdecodetest.py](https://github.com/voussoir/cmd/blob/master/ffdecodetest.py) to help me with this sort of task. The backyard and living room levels got particularly rekt, with only three and one clue passing the test, respectively. If by some very lucky chance you have a copy of this CD, perhaps you could try re-ripping it for us.

![](ffdecodetest.png)

So, all I had to do next was copy the canvas code I wrote [last time](/writing/browser_in_the_dark) and start shedding some light on things!

## Turn on your night light

<style>
.nightlight_game
{
    width: 100%;
    margin-block-start: 1em;
    aspect-ratio: 2048/1376;
    cursor: none;
}
</style>

Double-click on each game to go fullscreen. Just to be clear, I haven't recreated any of the actual puzzle gameplay, I'm just demoing the flashlight mechanic.

Your browser might prevent the clue audios from playing if you haven't clicked on anything in the document yet. Now's a good time to click something. How about this:

<audio id="theme_audio" controls src="night_light_theme.flac" style="width: 100%"/>

<audio id="clue_audio"/>

<canvas class="nightlight_game" data-prefix="ATTC"></canvas>

<canvas class="nightlight_game" data-prefix="BATH"></canvas>

<canvas class="nightlight_game" data-prefix="BEDR"></canvas>

<canvas class="nightlight_game" data-prefix="BKYD"></canvas>

<canvas class="nightlight_game" data-prefix="GARG"></canvas>

<canvas class="nightlight_game" data-prefix="KITC"></canvas>

<canvas class="nightlight_game" data-prefix="LIVR"></canvas>

<canvas class="nightlight_game" data-prefix="NURS"></canvas>

## The missing menu files

I'm glad that the level images were easy to extract, since those were the most important parts for me. However, I really would like to get the main menu images and the staff credit portraits out as well.

I looked through all the files with 7z, expecting to find a .bmp or a tiled .mov representing the menu, and I'm simply stumped. I don't see them anywhere. The closest thing I could find was MMCHOICE.MOV, where Pixel and Pandora discuss the level options.

<center><video controls src="mmchoice.mp4"/></center>

The game has several of these overlays for each of the levels too, so this file isn't unique in that regard. What I mean is, it's tempting to think mmchoice.mov would contain the full menu art if only we could zoom out somehow, and the other pixels are hiding just out of frame, but I don't think that's the case. The background art should be a separate file like the levels.

Perhaps I simply missed something, or perhaps they are embedded somewhere else. The game's NIGHTMPC.EXE is 7.7 MB, which seems big enough to hold some secrets. I searched through the binary to find any BMP or MOV headers but didn't have any luck. My understanding is that the game is supposed to work on both Windows and Mac: many of the game resources are provided in duplicate (BMP/PIC, WAV/AIF), but as far as binaries go I only see exe. Is there more somewhere that I'm not seeing? Are some files missing, and would that include the menu art?

If you discover anything, send me an email!

Along the way, I also found these image masks which give a hint as to how some of the click detection was done, which I think is very clever.

<center><img src="menu_mask.png"/> <img src="credits_mask.png"/></center>

## Conclusion

If you watch Tom Scott, you may have seen his video about [Need for Speed](https://www.youtube.com/watch?v=juRkaqkDfCM "I drove my childhood favorite racing game in real life"), a sentimental visit to the real life location after which a level from the game was modeled.

> All the things that we create, whether you have a big audience or whether you're just making stuff for the folks close to you, sure, maybe those things you make will be forgotten. Or maybe those things you create will get laid down as someone's long term memory, and affect them a lot later in their life. So, make nice things. Try to give people something they'll be nostalgic about. You never know what impressions you might be making for the future.

A kind thank you to all of these people:

<audio id="credits_audio" controls src="credits.flac" style="width: 100%"/>

Have fun!

<script>
IMAGE_WIDTH = 2048;
IMAGE_HEIGHT = 1376;
ASPECT_RATIO = IMAGE_WIDTH / IMAGE_HEIGHT;

clues = {}
clues["ATTC"] = [
"ATTC_FA01BIRD.flac", "ATTC_FA02COAT.flac", "ATTC_FA03ZMAN.flac", "ATTC_FA04BANA.flac",
"ATTC_FA05SUMO.flac", "ATTC_FA06ZAPE.flac", "ATTC_FA07TRAN.flac", "ATTC_FA08BELL.flac",
"ATTC_FA09ZFOX.flac", "ATTC_FA10BLOK.flac", "ATTC_FA11WIMP.flac", "ATTC_FA12FALL.flac",
"ATTC_FA13ROBT.flac", "ATTC_FA14FREK.flac", "ATTC_FA15CHIP.flac", "ATTC_FA16ZBUG.flac",
"ATTC_FA17MSTR.flac", "ATTC_FA18OCTO.flac", "ATTC_FA19ZBOX.flac", "ATTC_FA20CROK.flac",
"ATTC_FA21UNIC.flac", "ATTC_FA22CRRT.flac", "ATTC_FA23ZBEE.flac", "ATTC_FA24BIRD.flac",
"ATTC_FA25RBBT.flac", "ATTC_FA26SURF.flac", "ATTC_FA27ZEGG.flac", "ATTC_FA28TRTL.flac",
"ATTC_FA29DUCK.flac", "ATTC_FA30ZDOG.flac", "ATTC_FB01LGHT.flac", "ATTC_FB02STCK.flac",
"ATTC_FB03DEAD.flac", "ATTC_FB04KITE.flac", "ATTC_FB05RAQT.flac", "ATTC_FB06SQRL.flac",
"ATTC_FB07ROPE.flac", "ATTC_FB08BALL.flac", "ATTC_FB09CLUB.flac", "ATTC_FB10BOOM.flac",
"ATTC_FB11SCCR.flac", "ATTC_FB12GOLF.flac", "ATTC_FB13BATN.flac", "ATTC_FB14HMMR.flac",
"ATTC_FB15ZNUT.flac", "ATTC_FB16ZBAT.flac", "ATTC_FB18ZBAG.flac", "ATTC_FB19SQRL.flac",
"ATTC_FB20BORD.flac", "ATTC_FB21SOCK.flac", "ATTC_FB22STAR.flac", "ATTC_FB23ZHAT.flac",
"ATTC_FB24PCHR.flac"
]
clues["BATH"] = [
"BATH_AA01GOST.flac", "BATH_AA02DRGN.flac", "BATH_AA03CLAW.flac", "BATH_AA04FACE.flac",
"BATH_AA05BSNK.flac", "BATH_AA06OCTO.flac", "BATH_AA07RSNK.flac", "BATH_AA08ZRAT.flac",
"BATH_AA09SNAL.flac", "BATH_AA10SHRF.flac", "BATH_AA11BADG.flac", "BATH_AA12EELL.flac",
"BATH_AA13SHRK.flac", "BATH_AA14SWNG.flac", "BATH_AA15MSTR.flac", "BATH_AA16ELPH.flac",
"BATH_AA17WEZL.flac", "BATH_AA18BTNG.flac", "BATH_AA19EYEZ.flac", "BATH_AA20TETH.flac",
"BATH_AA21LMAN.flac", "BATH_AA22SMAN.flac", "BATH_AA23JROG.flac", "BATH_AA24GRML.flac",
"BATH_AA25FISH.flac", "BATH_AA26ZSUB.flac", "BATH_AA27TBD1.flac", "BATH_AA28FSTR.flac",
"BATH_AA29GSTR.flac", "BATH_AA30ZEYE.flac", "BATH_AB01GOST.flac", "BATH_AB01ZCAT.flac",
"BATH_AB02TBSH.flac", "BATH_AB03TREE.flac", "BATH_AB04OLET.flac", "BATH_AB05FACT.flac",
"BATH_AB06SHOT.flac", "BATH_AB07ZCAP.flac", "BATH_AB08CLNZ.flac", "BATH_AB09TBSH.flac",
"BATH_AB10SHRT.flac", "BATH_AB11TOWL.flac", "BATH_AB12PFSH.flac", "BATH_AB13TSSU.flac",
"BATH_AB14BRSH.flac", "BATH_AB15TROL.flac", "BATH_AB16SHOE.flac", "BATH_AB17BBSH.flac",
"BATH_AB18SDRP.flac", "BATH_AB19RSOP.flac", "BATH_AB20SDPD.flac", "BATH_AB21COLD.flac",
"BATH_AB22ZRAG.flac", "BATH_AB23SUDZ.flac", "BATH_AB24FLAG.flac", "BATH_AB25PAI1.flac",
"BATH_AB25PAIL.flac", "BATH_AB26BBAL.flac", "BATH_AB27SPNG.flac", "BATH_AB28DUCK.flac",
"BATH_AB29BAL1.flac", "BATH_AB29BALL.flac", "BATH_AB30KFSH.flac", "BATH_AB31SHRK.flac",
"BATH_AB32TPST.flac"
]
clues["BEDR"] = [
"BEDR_CA01JSTR.flac", "BEDR_CA02FMAN.flac", "BEDR_CA02MAN.flac", "BEDR_CA03FPOT.flac",
"BEDR_CA04WTCH.flac", "BEDR_CA05PMAN.flac", "BEDR_CA06PLNE.flac", "BEDR_CA07ZSUB.flac",
"BEDR_CA08MSTR.flac", "BEDR_CA09MSTR.flac", "BEDR_CA10MSTR.flac", "BEDR_CA11MSTR.flac",
"BEDR_CA12TRAN.flac", "BEDR_CA13HPPO.flac", "BEDR_CA14MUMY.flac", "BEDR_CA15RCKT.flac",
"BEDR_CB23BBAL.flac", "BEDR_CB24ZBAT.flac", "BEDR_CB25PLNE.flac", "BEDR_CB26ZCAP.flac",
"BEDR_CB27TBER.flac", "BEDR_CB28TCAN.flac", "BEDR_CB29HORS.flac", "BEDR_CB30FBAL.flac",
"BEDR_CB31SNKR.flac", "BEDR_CB32PILO.flac"
]
clues["BKYD"] = [
"BKYD_GB12FINN.flac", "BKYD_GB13BIGW.flac", "BKYD_GB16STCK.flac"
]
clues["GARG"] = [
"GARG_EA04GRFF.flac", "GARG_EA05FISH.flac", "GARG_EA06JAIL.flac", "GARG_EA07DRVR.flac",
"GARG_EA08KROO.flac", "GARG_EA09MUMY.flac", "GARG_EA10MSTR.flac", "GARG_EA11ROBT.flac",
"GARG_EA12BRED.flac", "GARG_EA13ZJAR.flac", "GARG_EA14FFLY.flac", "GARG_EA15SNKE.flac",
"GARG_EA16CPLR.flac", "GARG_EA17ZBAT.flac", "GARG_EA18BRNG.flac", "GARG_EA19ELPH.flac",
"GARG_EA20MSTR.flac", "GARG_EA21DUDE.flac", "GARG_EA22ZCAR.flac", "GARG_EA23APPL.flac",
"GARG_EA24SNKE.flac", "GARG_EA25MSTR.flac", "GARG_EA26CNON.flac", "GARG_EA27ZEYE.flac",
"GARG_EA28DNUT.flac", "GARG_EA29CLWN.flac", "GARG_EA30HSTK.flac", "GARG_EA31LIPS.flac",
"GARG_EB01BTTL.flac", "GARG_EB02NOTE.flac", "GARG_EB03ZSAW.flac", "GARG_EB04ZSAW.flac",
"GARG_EB05HMMR.flac", "GARG_EB07SDRV.flac", "GARG_EB08CHSL.flac", "GARG_EB09SCSR.flac",
"GARG_EB10WRCH.flac", "GARG_EB11SCKT.flac", "GARG_EB12DRVR.flac", "GARG_EB13VENT.flac",
"GARG_EB14SOAP.flac", "GARG_EB15KNOB.flac", "GARG_EB16BSKT.flac", "GARG_EB17BALL.flac",
"GARG_EB18BEAR.flac", "GARG_EB19GRSE.flac", "GARG_EB20BBAT.flac", "GARG_EB21BBAL.flac",
"GARG_EB22TIRE.flac", "GARG_EB23MOUS.flac", "GARG_EB24ZHAT.flac", "GARG_EB25SEAT.flac",
"GARG_EB26RLLR.flac", "GARG_EB27PCAN.flac", "GARG_EB28BRSH.flac", "GARG_EB29BUCT.flac"
]
clues["KITC"] = [
"KITC_BA01EYEZ.flac", "KITC_BA02EYEZ.flac", "KITC_BA03OWLI.flac", "KITC_BA04MSTR.flac",
"KITC_BA05EYEZ.flac", "KITC_BA06FORT.flac", "KITC_BA07MSTR.flac", "KITC_BA08OCTO.flac",
"KITC_BA09DILO.flac", "KITC_BA10SNKE.flac", "KITC_BA11MAN1.flac"
]
clues["LIVR"] = [
"LIVR_DA18DEER.flac"
]
clues["NURS"] = [
"NURS_HA12CHST.flac", "NURS_HA16TRIO.flac", "NURS_HB17ZFOX.flac", "NURS_HB20BALL.flac"
]
const theme_audio = document.getElementById("theme_audio");
const clue_audio = document.getElementById("clue_audio");
const credits_audio = document.getElementById("credits_audio");
let active_prefix;

let clue_timeout;

function clue_loop()
{
    let delay;
    const do_play = (
        active_prefix &&
        document.hasFocus() &&
        theme_audio.paused &&
        clue_audio.paused &&
        credits_audio.paused &&
        clues[active_prefix].length > 0
    );
    if (do_play)
    {
        const options = clues[active_prefix];
        const index = Math.floor(Math.random() * options.length);
        const clue = options.splice(index, 1)[0];
        clue_audio.src = "clues/" + clue;
        delay = (Math.random() * 10000) + 7000;
        clue_audio.play();
    }
    else
    {
        delay = 2000;
    }
    clue_timeout = setTimeout(clue_loop, delay);
}

function draw_game(game, light_x, light_y)
{
    const ctx = game.getContext("2d");
    ctx.clearRect(0, 0, game.width, game.height);

    const region = new Path2D();
    // // A little padding off screen helps reduce slivers of light.
    // region.rect(-10, -10, game.width+20, game.height+20);
    // ctx.fill(region);

    let draw_width;
    let draw_height;
    const game_aspect = game.width / game.height;
    if (game_aspect > ASPECT_RATIO)
    {
        draw_height = game.height;
        draw_width = ASPECT_RATIO * draw_height;
    }
    else
    {
        draw_width = game.width;
        draw_height = draw_width / ASPECT_RATIO;
    }

    const offset_left = (game.width - draw_width) / 2;
    const offset_top = (game.height - draw_height) / 2;

    if (light_x === null || light_y === null)
    {
        ctx.globalCompositeOperation = "source-over";
        ctx.drawImage(game.image_dark, offset_left, offset_top, draw_width, draw_height);
    }
    else
    {
        ctx.globalCompositeOperation = "source-over";
        ctx.beginPath();
        const light_radius = draw_height / 6;
        ctx.ellipse(light_x, light_y, light_radius, light_radius, Math.PI / 4, 0, 2 * Math.PI);
        ctx.closePath();
        ctx.fill();

        ctx.globalCompositeOperation = "source-in";
        ctx.drawImage(game.image_light, offset_left, offset_top, draw_width, draw_height);

        ctx.globalCompositeOperation = "destination-over";
        ctx.drawImage(game.image_dark, offset_left, offset_top, draw_width, draw_height);
    }
}

function nightlight_dblclick(event)
{
    const game = event.target.closest(".nightlight_game");
    if (document.fullscreenElement === null)
    {
        game.requestFullscreen();
    }
    else
    {
        document.exitFullscreen();
    }
    event.preventDefault();
    event.stopPropagation();
    document.getSelection().removeAllRanges();
    return false;
}

function nightlight_mouseenter(event)
{
    const game = event.target.closest(".nightlight_game");
    active_prefix = game.dataset.prefix;
    clearTimeout(clue_timeout);
    clue_timeout = setTimeout(clue_loop, 3000);
}

function nightlight_mouseleave(event)
{
    active_prefix = null;
    const game = event.target.closest(".nightlight_game");
    showdark(game);
    clearTimeout(clue_timeout);
}

function nightlight_mousemove(event)
{
    const game = event.target.closest(".nightlight_game");
    if (! (game.image_dark.complete && game.image_light.complete))
    {
        return;
    }
    draw_game(game, event.offsetX, event.offsetY);
}

function resize_nightlights(event)
{
    for (const game of document.getElementsByClassName("nightlight_game"))
    {
        game.width = game.offsetWidth;
        game.height = game.offsetHeight;
        showdark(game);
    }
}

function showdark(game)
{
    if (! game.image_dark.complete)
    {
        setTimeout(() => {showdark(game);}, 100);
    }
    draw_game(game, null, null)
}

function on_pageload()
{
    for (const game of document.getElementsByClassName("nightlight_game"))
    {
        game.image_dark = new Image();
        game.image_dark.src = game.dataset.prefix + "_DARK.png";
        game.image_light = new Image();
        game.image_light.src = game.dataset.prefix + "_LIGHT.png";

        game.addEventListener("dblclick", nightlight_dblclick);
        game.addEventListener("mouseenter", nightlight_mouseenter);
        game.addEventListener("mouseleave", nightlight_mouseleave);
        game.addEventListener("mousemove", nightlight_mousemove);
    }
    window.addEventListener("resize", resize_nightlights);

    resize_nightlights();
}
document.addEventListener("DOMContentLoaded", on_pageload);
</script>
