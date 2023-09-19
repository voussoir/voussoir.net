Night Light (1995)
==================

## Introduction

When I was a kid, one of the computer games I played was Night Light, by GTE Entertainment. It's about Pandora the cat and Pixel the dog exploring the house in the dark after all the people have gone out for the night.

![](cover.jpg)

This game stuck in my memory in the way that only a formative childhood game can. There is something about the game mechanic of using the mouse as a flashlight that's very appealing to me, though of course I don't know if this is cause or effect.

For the past several years, I have occasionally been reminded of the game and tried to search for it online, only to come up empty handed. Finally, in 2018, a youtuber named Vulnerose Plays [did a playthrough](https://www.youtube.com/watch?v=KYDoBcFcGM8) and also [uploaded the ISO](https://archive.org/details/NightLight_201809) to the Internet Archive. The majority of comments on that video are from other people saying they'd been searching high and low for the game, too [footnote_link].

At the time of this writing, I have not actually played the game using the provided iso, as it would require me to emulate an older version of Windows and I haven't gotten around to doing it yet. But, I [recently](/writing/browser_in_the_dark) had the inspiration to reproduce the basic mechanic using javascript canvas, and that brings us to today.

[footnote_text] spoiler alert, but there's a better copy here: https://archive.org/details/night-light_202208

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

I deleted 01-16 from each folder, then updated my [stitch.py](https://git.voussoir.net/voussoir/cmd/src/branch/master/stitch.py) to take a `--grid` argument, and stitched the remaining 64 images together for each level.

![](stitch_8x8.png)

![](all_stitching.png)

I also extracted the audio clues and converted them to flac. Unfortunately, lots of the source files were corrupted, with an excess of zero bytes making them impossible to decode.

![](hxd.png)

I wrote [ffdecodetest.py](https://git.voussoir.net/voussoir/cmd/src/branch/master/ffdecodetest.py) to help me with this sort of task. The backyard and living room levels got particularly rekt, with only three and one clue passing the test, respectively.

![](ffdecodetest1.png)

## A second copy

When I originally published this article in April, the next sentence was:

> If by some very lucky chance you have a copy of this CD, perhaps you could try re-ripping it for us.

And that's what happened!

I got an email from Josh Henderson who also has a CD of the game. He kindly extracted the ISO and uploaded it to archive.org: https://archive.org/details/night-light_202208

Thank you again Josh!

I popped this one open with 7-zip and got all 471 clues in mint condition.

![](ffdecodetest2.png)

So, all I had to do next was copy the canvas code I wrote [last time](/writing/browser_in_the_dark) and start shedding some light on things.

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

I'm glad that the level images were easy to extract, since those were the most important parts for me. I'm also glad we recovered all of the clues. However, I really would like to get the main menu images and the staff credit portraits out as well.

![](mainmenu_screenshot.png)

I looked through all the files with 7z, expecting to find a .bmp or a tiled .mov representing the menu, and I'm simply stumped. I don't see them anywhere. The closest thing I could find was MMCHOICE.MOV, where Pixel and Pandora discuss the level options, but it's cropped in on them.

<center><video controls src="mmchoice.mp4"/></center>

The game uses this kind of video file as an overlay whenever it needs to put the talking characters in front of the game. If you look through the QTPUZZLE folder you'll find many more of these.

<center><video controls src="attc_01.mp4"/></center>

So, it's not like mmchoice.mov is damaged, or cropped accidentally. But, like the puzzles, I expect to find the loading screen, the main menu art, and the credits photos in their own files. I just don't see any more tiled movs or bitmaps. There are 18 .pic files, but those are just BACKMASK.PIC, FOREMASK.PIC, and a set of LIGHT.PIC and DARK.PIC for each of the eight levels.

Perhaps I simply missed something, or perhaps they are embedded somewhere else, though I don't know why that would be. The game's NIGHTMPC.EXE is 7.7 MB, which seems big enough to hold some secrets. I searched through the binary for BMP and MOV headers but didn't have any luck, and 7-zip doesn't open it the way it does with some executables.

My understanding is that the game is supposed to work on both Windows and Mac: many of the game resources are provided in duplicate (BMP/PIC, WAV/AIF), but as far as binaries go I only see exe. What's up with that?

If you discover anything, send me an email!

Along the way, I also found these image masks which give a hint as to how some of the click detection was done, which I think is very clever. Each of these cells has a unique RGB color -- so the programmers could make each color represent a choice for the user to click on.

<center><img src="menu_mask.png"/> <img src="credits_mask.png"/></center>

## Conclusion

If you watch Tom Scott, you may have seen his video about [Need for Speed](https://www.youtube.com/watch?v=juRkaqkDfCM "I drove my childhood favorite racing game in real life"), a sentimental visit to the real life location after which a level from the game was modeled.

> All the things that we create, whether you have a big audience or whether you're just making stuff for the folks close to you, sure, maybe those things you make will be forgotten. Or maybe those things you create will get laid down as someone's long term memory, and affect them a lot later in their life. So, make nice things. Try to give people something they'll be nostalgic about. You never know what impressions you might be making for the future.

A kind thank you to all of these people:

<audio id="credits_audio" controls src="credits.flac" style="width: 100%"/>

![](credits_screenshot.png)

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
"BEDR_CA16DRGN.flac", "BEDR_CA17ELPH.flac", "BEDR_CA18HAND.flac", "BEDR_CA19TERY.flac",
"BEDR_CA20MSTR.flac", "BEDR_CA21ZASP.flac", "BEDR_CA22HOSE.flac", "BEDR_CA23FLWR.flac",
"BEDR_CA24TPEE.flac", "BEDR_CA25SNKE.flac", "BEDR_CB01RABT.flac", "BEDR_CB02LAMB.flac",
"BEDR_CB03TRIC.flac", "BEDR_CB04RIBN.flac", "BEDR_CB05SMCP.flac", "BEDR_CB06CLWN.flac",
"BEDR_CB07HSTK.flac", "BEDR_CB08BLDZ.flac", "BEDR_CB09ROBT.flac", "BEDR_CB10PLNE.flac",
"BEDR_CB11ZCAR.flac", "BEDR_CB12BANK.flac", "BEDR_CB13BRON.flac", "BEDR_CB14TREX.flac",
"BEDR_CB15TRUK.flac", "BEDR_CB16SOCK.flac", "BEDR_CB17VITC.flac", "BEDR_CB18CLDS.flac",
"BEDR_CB19BOOK.flac", "BEDR_CB20GLBZ.flac", "BEDR_CB21SHRT.flac", "BEDR_CB22DRWR.flac",
"BEDR_CB23BBAL.flac", "BEDR_CB24ZBAT.flac", "BEDR_CB25PLNE.flac", "BEDR_CB26ZCAP.flac",
"BEDR_CB27TBER.flac", "BEDR_CB28TCAN.flac", "BEDR_CB29HORS.flac", "BEDR_CB30FBAL.flac",
"BEDR_CB31SNKR.flac", "BEDR_CB32PILO.flac", "BEDR_CB33LADR.flac", "BEDR_CB34GMBD.flac",
"BEDR_CB35DLMP.flac", "BEDR_CB36BRSH.flac", "BEDR_CB37NKTY.flac", "BEDR_CB38SOCK.flac"
]
clues["BKYD"] = [
"BKYD_GA01DINO.flac", "BKYD_GA02DINO.flac", "BKYD_GA03DINO.flac", "BKYD_GA04DINO.flac",
"BKYD_GA05DINO.flac", "BKYD_GA06DINO.flac", "BKYD_GA07DINO.flac", "BKYD_GA08DINO.flac",
"BKYD_GA09DINO.flac", "BKYD_GA10DINO.flac", "BKYD_GA11DINO.flac", "BKYD_GA12DINO.flac",
"BKYD_GA13DINO.flac", "BKYD_GA14CRAK.flac", "BKYD_GA15EGGS.flac", "BKYD_GA16DUDE.flac",
"BKYD_GB01SQRL.flac", "BKYD_GB02TIRE.flac", "BKYD_GB03SCCR.flac", "BKYD_GB05BALL.flac",
"BKYD_GB06SAIL.flac", "BKYD_GB07FOAT.flac", "BKYD_GB08DUCK.flac", "BKYD_GB09BBAL.flac",
"BKYD_GB10GOFR.flac", "BKYD_GB10MASK.flac", "BKYD_GB11TRTL.flac", "BKYD_GB12FINN.flac",
"BKYD_GB13BIGW.flac", "BKYD_GB14ZCAP.flac", "BKYD_GB15FBAL.flac", "BKYD_GB16STCK.flac",
"BKYD_GB17APPL.flac", "BKYD_GB18BALL.flac", "BKYD_GB20SHVL.flac", "BKYD_GB21FLAG.flac",
"BKYD_GB22HOSE.flac", "BKYD_GB23ZHOW.flac", "BKYD_GB24RAKE.flac", "BKYD_GB25TRWL.flac"
]
clues["GARG"] = [
"GARG_EA01EYEZ.flac", "GARG_EA03BRD2.flac", "GARG_EA04GRFF.flac", "GARG_EA05FISH.flac",
"GARG_EA06JAIL.flac", "GARG_EA07DRVR.flac", "GARG_EA08KROO.flac", "GARG_EA09MUMY.flac",
"GARG_EA10MSTR.flac", "GARG_EA11ROBT.flac", "GARG_EA12BRED.flac", "GARG_EA13ZJAR.flac",
"GARG_EA14FFLY.flac", "GARG_EA15SNKE.flac", "GARG_EA16CPLR.flac", "GARG_EA17ZBAT.flac",
"GARG_EA18BRNG.flac", "GARG_EA19ELPH.flac", "GARG_EA20MSTR.flac", "GARG_EA21DUDE.flac",
"GARG_EA22ZCAR.flac", "GARG_EA23APPL.flac", "GARG_EA24SNKE.flac", "GARG_EA25MSTR.flac",
"GARG_EA26CNON.flac", "GARG_EA27ZEYE.flac", "GARG_EA28DNUT.flac", "GARG_EA29CLWN.flac",
"GARG_EA30HSTK.flac", "GARG_EA31LIPS.flac", "GARG_EB01BTTL.flac", "GARG_EB02NOTE.flac",
"GARG_EB03ZSAW.flac", "GARG_EB04ZSAW.flac", "GARG_EB05HMMR.flac", "GARG_EB07SDRV.flac",
"GARG_EB08CHSL.flac", "GARG_EB09SCSR.flac", "GARG_EB10WRCH.flac", "GARG_EB11SCKT.flac",
"GARG_EB12DRVR.flac", "GARG_EB13VENT.flac", "GARG_EB14SOAP.flac", "GARG_EB15KNOB.flac",
"GARG_EB16BSKT.flac", "GARG_EB17BALL.flac", "GARG_EB18BEAR.flac", "GARG_EB19GRSE.flac",
"GARG_EB20BBAT.flac", "GARG_EB21BBAL.flac", "GARG_EB22TIRE.flac", "GARG_EB23MOUS.flac",
"GARG_EB24ZHAT.flac", "GARG_EB25SEAT.flac", "GARG_EB26RLLR.flac", "GARG_EB27PCAN.flac",
"GARG_EB28BRSH.flac", "GARG_EB29BUCT.flac"
]
clues["KITC"] = [
"KITC_BA01EYEZ.flac", "KITC_BA02EYEZ.flac", "KITC_BA03OWLI.flac", "KITC_BA04MSTR.flac",
"KITC_BA05EYEZ.flac", "KITC_BA06FORT.flac", "KITC_BA07MSTR.flac", "KITC_BA08OCTO.flac",
"KITC_BA09DILE.flac", "KITC_BA09DILO.flac", "KITC_BA10SNKE.flac", "KITC_BA11MAN1.flac",
"KITC_BA12MAN2.flac", "KITC_BA13MAN3.flac", "KITC_BA14PRNA.flac", "KITC_BA15SNKE.flac",
"KITC_BA16BFLY.flac", "KITC_BA17SCER.flac", "KITC_BA17SCSR.flac", "KITC_BA18ZHAT.flac",
"KITC_BA19FRTH.flac", "KITC_BA20ANT1.flac", "KITC_BA21MSTR.flac", "KITC_BA22ANTZ.flac",
"KITC_BA23ZPAW.flac", "KITC_BA24NITE.flac", "KITC_BA25HARY.flac", "KITC_BA26SPDR.flac",
"KITC_BA27SHRK.flac", "KITC_BB01BBAL.flac", "KITC_BB02GRPZ.flac", "KITC_BB03RBBT.flac",
"KITC_BB04ZBAT.flac", "KITC_BB05CHOW.flac", "KITC_BB06FDG1.flac", "KITC_BB07FDG2.flac",
"KITC_BB08FDG3.flac", "KITC_BB09FDG4.flac", "KITC_BB10FDG5.flac", "KITC_BB11ZCUP.flac",
"KITC_BB12OUCH.flac", "KITC_BB13BITE.flac", "KITC_BB14NOTE.flac", "KITC_BB15FORK.flac",
"KITC_BB16GLOV.flac", "KITC_BB17P.flac", "KITC_BB17TSTR.flac", "KITC_BB18APPL.flac",
"KITC_BB19PEPR.flac", "KITC_BB20SALT.flac", "KITC_BB21PBTR.flac", "KITC_BB22WATR.flac",
"KITC_BB23TSSL.flac", "KITC_BB24SPTL.flac", "KITC_BB25DUCK.flac", "KITC_BB26TULP.flac",
"KITC_BB27ZOWL.flac", "KITC_BB28RATL.flac", "KITC_BB29BNAS.flac", "KITC_BB30ZRAG.flac"
]
clues["LIVR"] = [
"LIVR_DA01NARK.flac", "LIVR_DA02LAMP.flac", "LIVR_DA02SQRL.flac", "LIVR_DA03LAMB.flac",
"LIVR_DA04FISH.flac", "LIVR_DA04PRNA.flac", "LIVR_DA05BEAR.flac", "LIVR_DA06PRQU.flac",
"LIVR_DA06TBA2.flac", "LIVR_DA07DRUM.flac", "LIVR_DA07TBA3.flac", "LIVR_DA08TELE.flac",
"LIVR_DA08TRT1.flac", "LIVR_DA08TRTL.flac", "LIVR_DA09MOUS.flac", "LIVR_DA10PICT.flac",
"LIVR_DA10PNGN.flac", "LIVR_DA11MUSH.flac", "LIVR_DA12YARN.flac", "LIVR_DA12ZUFO.flac",
"LIVR_DA13BRED.flac", "LIVR_DA14COON.flac", "LIVR_DA14PCCN.flac", "LIVR_DA15MUSH.flac",
"LIVR_DA16BTIE.flac", "LIVR_DA16QULT.flac", "LIVR_DA17SEAL.flac", "LIVR_DA18BONE.flac",
"LIVR_DA18DEER.flac", "LIVR_DA19RCKT.flac", "LIVR_DA20BOOK.flac", "LIVR_DA20DRGN.flac",
"LIVR_DA21FACE.flac", "LIVR_DA22GLAS.flac", "LIVR_DA22ZFOX.flac", "LIVR_DA23SQRL.flac",
"LIVR_DA24FACE.flac", "LIVR_DA25CBAR.flac", "LIVR_DA26TANR.flac", "LIVR_DA27TRAN.flac",
"LIVR_DA28FRRY.flac", "LIVR_DA28MAGZ.flac", "LIVR_DA30BALL.flac", "LIVR_DA32ZRED.flac",
"LIVR_DA34COKI.flac", "LIVR_DB01HOME.flac", "LIVR_DB02LAMP.flac", "LIVR_DB03PICT.flac",
"LIVR_DB04FISH.flac", "LIVR_DB05TBA1.flac", "LIVR_DB06TBA2.flac", "LIVR_DB07TBA3.flac",
"LIVR_DB08TELE.flac", "LIVR_DB09ZVCR.flac", "LIVR_DB10PICT.flac", "LIVR_DB11BEAR.flac",
"LIVR_DB12YARN.flac", "LIVR_DB13FONE.flac", "LIVR_DB14PCCN.flac", "LIVR_DB15JCKT.flac",
"LIVR_DB16QULT.flac", "LIVR_DB17SODA.flac", "LIVR_DB18BONE.flac", "LIVR_DB19SHOZ.flac",
"LIVR_DB20BOOK.flac", "LIVR_DB21SHOE.flac", "LIVR_DB22GLAS.flac", "LIVR_DB23DOLL.flac",
"LIVR_DB25REMT.flac", "LIVR_DB27BLUE.flac", "LIVR_DB28MAGZ.flac", "LIVR_DB29BOOK.flac",
"LIVR_DB30BALL.flac", "LIVR_DB31GAME.flac", "LIVR_DB32ZRED.flac", "LIVR_DB33GLAS.flac",
"LIVR_DB34COKI.flac"
]
clues["NURS"] = [
"NURS_HA01CTHZ.flac", "NURS_HA02JELY.flac", "NURS_HA03VLAG.flac", "NURS_HA04LAVA.flac",
"NURS_HA05CHCK.flac", "NURS_HA06STAR.flac", "NURS_HA07FACE.flac", "NURS_HA08BABE.flac",
"NURS_HA09FROG.flac", "NURS_HA10BIRD.flac", "NURS_HA11HRSE.flac", "NURS_HA12CHST.flac",
"NURS_HA13TREE.flac", "NURS_HA14JWEL.flac", "NURS_HA15CHMP.flac", "NURS_HA16TRIO.flac",
"NURS_HA17WOLF.flac", "NURS_HA18BOKZ.flac", "NURS_HA19SKLZ.flac", "NURS_HA20CROK.flac",
"NURS_HA21EEGG.flac", "NURS_HA22LION.flac", "NURS_HA23ELPH.flac", "NURS_HA24THNG.flac",
"NURS_HA25ZBUG.flac", "NURS_HA27FLWR.flac", "NURS_HA28FROG.flac", "NURS_HA29SWRD.flac",
"NURS_HA30CUPL.flac", "NURS_HA31ZSUB.flac", "NURS_HA32ZBRA.flac", "NURS_HB01LAMP.flac",
"NURS_HB02PICT.flac", "NURS_HB04ZCAT.flac", "NURS_HB05PICT.flac", "NURS_HB06DUCK.flac",
"NURS_HB07BUNY.flac", "NURS_HB08BUNY.flac", "NURS_HB10ZCOW.flac", "NURS_HB11MOON.flac",
"NURS_HB12QULT.flac", "NURS_HB13LAMB.flac", "NURS_HB14SHEZ.flac", "NURS_HB15BEAR.flac",
"NURS_HB16BUNY.flac", "NURS_HB17ZFOX.flac", "NURS_HB18PASS.flac", "NURS_HB19SOCK.flac",
"NURS_HB20BALL.flac", "NURS_HB21CRRT.flac", "NURS_HB22ZBRA.flac", "NURS_HB23BTTL.flac",
"NURS_HB24BBAL.flac", "NURS_HB25CLCK.flac"
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
