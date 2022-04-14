Browser in the Dark: flashlights with CSS and canvas
====================================================

<style>
@keyframes filmgrain
{
    from
    {
        background-position: -20px -20px;
        transform: rotate(0deg);
    }
    33%
    {
        background-position: 20px 20px;
        transform: rotate(-45deg);
    }
    66%
    {
        background-position: -20px 20px;
        transform: rotate(111deg);
    }
    to
    {
        background-position: 20px -20px;
        transform: rotate(-265deg);
    }
}
@keyframes party
{
    from
    {
        filter: hue-rotate(0deg);
        transform: rotate(0deg);
    }
    50%
    {
        filter: hue-rotate(180deg);
        transform: rotate(360deg);
    }
    to
    {
        filter: hue-rotate(360deg);
        transform: rotate(720deg);
    }
}

body .hide_when_light { display: none; }
body .hide_when_dark { display: initial; }
body.canvas_active .hide_when_light { display: initial; }
body.canvas_active .hide_when_dark { display: none; }

/******************************************************************************/

#flashlight
{
    position: fixed;
    z-index: 1;
    pointer-events: none;

    width: 250px;
    height: 250px;
    border-radius: 100%;
}
#flashlight.grayscale
{
    background-color: gray;
    mix-blend-mode: saturation;
}
#flashlight.white
{
    background-color: white;
    mix-blend-mode: overlay;
}
#flashlight.soft_light
{
    background-color: white;
    mix-blend-mode: soft-light;
    filter: blur(20px);
}
#flashlight.invert
{
    background-color: white;
    mix-blend-mode: difference;
}
#flashlight.party
{
    background-color: red;
    mix-blend-mode: color;

    border-radius: 0;
    animation-name: party;
    animation-duration: 5s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}
#flashlight.wild_west
{
    background-color: goldenrod;
    background-image: url("whitenoise.png");
    background-blend-mode: luminosity;
    mix-blend-mode: color;

    animation-name: filmgrain;
    animation-duration: 0.2s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

/******************************************************************************/

#fullpage_canvas
{
    position: fixed;
    z-index: 1;
    pointer-events: none;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    /* On android chrome, scrolling the page causes the nav bar to recede,
    and that creates visible space below the canvas before the resize event
    is called. We intentionally oversize it to keep everything hidden. */
    height: 150%;
}

/******************************************************************************/

.nightlight_game_dom
{
    position: relative;
    width: 100%;
    overflow: hidden;
    margin-block-start: 1em;
    margin-block-end: 1em;
}
.nightlight_game_dom .layer1,
.nightlight_game_dom .layer2
{
    position: absolute;
}
.nightlight_game_dom .layer1
{
    width: 100%;
    aspect-ratio: inherit;
    background-size: contain;
    background-repeat: no-repeat;
}
.nightlight_game_dom .layer2
{
    display: none;

    pointer-events: none;
    border-radius: 100%;
    background-repeat: no-repeat;
    aspect-ratio: 1/1;
}

#nightlight_bedroom_dom
{
    aspect-ratio: 512/344;
}
#nightlight_bedroom_dom .layer1
{
    background-image: url("nightlight_1.png");
}
#nightlight_bedroom_dom .layer2
{
    background-image: url("nightlight_2.png");
    height: 30%;
}

#nightlight_theylive_obey_dom
{
    aspect-ratio: 1920/816;
}
#nightlight_theylive_obey_dom .layer1
{
    background-image: url("theylive_obey_1.jpg");
}
#nightlight_theylive_obey_dom .layer2
{
    background-image: url("theylive_obey_2.jpg");
    height: 50%;
}

#nightlight_theylive_consume_dom
{
    aspect-ratio: 1920/816;
}
#nightlight_theylive_consume_dom .layer1
{
    background-image: url("theylive_consume_1.jpg");
}
#nightlight_theylive_consume_dom .layer2
{
    background-image: url("theylive_consume_2.jpg");
    height: 50%;
}

/******************************************************************************/

.nightlight_game_canvas
{
    width: 100%;
    margin-block-start: 1em;
    margin-block-end: 1em;
}
#nightlight_bedroom_canvas
{
    aspect-ratio: 512/344;
}
#nightlight_theylive_obey_canvas
{
    aspect-ratio: 1920/816;
}
#nightlight_theylive_consume_canvas
{
    aspect-ratio: 1920/816;
}
</style>

Note: this article will make more sense if you are using a mouse or other pointing device. Requires javascript.

Warning: things can get a little spooky in the dark!

You can read the source code for this document [here](https://github.com/voussoir/voussoir.net/raw/master/voussoir.net/writing/browser_in_the_dark/browser_in_the_dark.md) (or by pressing Ctrl+U in chrome / firefox).

## mix-blend-mode

<div id="flashlight"></div>

I really like the "dark mode" switch on https://tonsky.me [footnote_link]. It's a fun subversion of expectations and reminds me of [Night Light (1995)](/writing/night_light_1995), a PC game for kids about using a flashlight in the dark.

One of the splash texts I put on [my homepage](/?justthesplash) a while back says "looks better in black and white". Yesterday, while hypnotized by my own pulsating creation [footnote_link], I had the idea to put the two together and create a grayscale "flashlight", or perhaps a lens. I learned that the CSS property `mix-blend-mode` allows me to make a div that turns everything below it gray. The other mix-blend-mode options are cool too.

The results don't look exactly like a light source, but it's a nice toy. Here are some different flashlights and photos with which to admire them:

<p>
<button onclick="return set_flashlight_mode('grayscale');">Grayscale</button>
<button onclick="return set_flashlight_mode('white');">Bright White</button>
<button onclick="return set_flashlight_mode('soft_light');">Soft light</button>
<button onclick="return set_flashlight_mode('invert');">Invert</button>
<button onclick="return set_flashlight_mode('party');">Party</button>
<button onclick="return set_flashlight_mode('wild_west');">Wild West</button>
<button onclick="return set_flashlight_mode('');">Off</button>
</p>

<img class="spooky_image" src="the_bear.jpg" data-dark-src="the_bear_spooky.jpg"/>

<img class="spooky_image" src="shining.jpg" data-dark-src="shining_spooky.jpg"/>

<img class="spooky_image" src="all_american_murder.jpg" data-dark-src="all_american_murder_spooky.jpg"/>

<span class="hide_when_dark">It applies to all elements on the page. <font color="ivysaur">sample</font> <font color="charmeleon">sample</font> <font color="squirtle">sample</font> <font color="chucknorris">sample</font> <font color="cabs">sample</font>. <!-- https://stackoverflow.com/questions/8318911/why-does-html-think-chucknorris-is-a-color --></span>

<span class="hide_when_light"><font color="red">♫ It's just your imagination<br/>♫ night time fascination</font></span>

<img class="spooky_image" src="dancer_in_the_dark.jpg" data-dark-src="dancer_in_the_dark_spooky.jpg"/>

<img class="spooky_image" src="the_tracker.jpg" data-dark-src="the_tracker_spooky.jpg"/>

<img class="spooky_image" src="hellraiser.jpg" data-dark-src="hellraiser_spooky.jpg"/>

## Canvas

<canvas id="fullpage_canvas"></canvas>

I think those effects are fun, but they don't really give you the feeling of being in the dark like tonsky's flashlight switch. His works by setting the background color to black, so all the black text "disappears" even though it's still there. I wanted to come up with a flashlight that really works for all elements on the page, but I don't think any combination of DOM elements and mix-blend-modes would do it.

I've never used HTML canvas before, but I realized that would be the correct solution. I was able to get a basic flashlight effect working by covering the entire screen in a black rectangle, and punching a hole in it.

<p>
<button onclick="return enable_fullpage_canvas(event);">Canvas on</button>
<button onclick="return disable_fullpage_canvas(event);">Canvas off</button>
</p>

<span class="hide_when_light">If at any time you need to come back, all you must do is open your eyes.</span>

This works great in conjunction with the mix-blend-mode lights:

<p>
<button onclick="return set_flashlight_mode('grayscale');">Grayscale</button>
<button onclick="return set_flashlight_mode('white');">Bright White</button>
<button onclick="return set_flashlight_mode('soft_light');">Soft light</button>
<button onclick="return set_flashlight_mode('invert');">Invert</button>
<button onclick="return set_flashlight_mode('party');">Party</button>
<button onclick="return set_flashlight_mode('wild_west');">Wild West</button>
<button onclick="return set_flashlight_mode('');">Off</button>
</p>

Go back up and look at the images again!

## Night Light with CSS

I also wanted to try making a Night Light game effect. The player who recorded the above video also uploaded the game .iso to the Internet Archive. Thank you Vulnerose!

https://archive.org/details/NightLight_201809

I was able to open the iso in 7-zip, extract the level artwork as bmp files, produce the toy below. I've made a [followup article](/writing/night_light_1995) with the other assets.

I first tried to approach it with mix-blend-mode, but I don't think you can use those effects to produce arbitrary image masks. I got it done with a more traditional method of translating a background-image property. The only jank fix I'm not really happy about is the background-size property for the flashlight layer, which I had to set using px values in javascript to match the rendered size of the parent. All the other background-size options created ill effects when I wanted to change the size of the flashlight to anything other than 100%. But I'm not that good with CSS and there might be a better answer.

Please turn off your flashlight first. Or don't, and enjoy the two effects together!

<p>
<button onclick="return enable_fullpage_canvas(event);">Canvas on</button>
<button onclick="return disable_fullpage_canvas(event);">Canvas off</button>
</p>

<p>
<button onclick="return set_flashlight_mode('grayscale');">Grayscale</button>
<button onclick="return set_flashlight_mode('white');">Bright White</button>
<button onclick="return set_flashlight_mode('soft_light');">Soft light</button>
<button onclick="return set_flashlight_mode('invert');">Invert</button>
<button onclick="return set_flashlight_mode('party');">Party</button>
<button onclick="return set_flashlight_mode('wild_west');">Wild West</button>
<button onclick="return set_flashlight_mode('');">Off</button>
</p>

<div id="nightlight_bedroom_dom" class="nightlight_game_dom">
    <div class="layer1"></div>
    <div class="layer2"></div>
</div>

And, I couldn't help it:

<div id="nightlight_theylive_obey_dom" class="nightlight_game_dom">
    <div class="layer1"></div>
    <div class="layer2"></div>
</div>

<div id="nightlight_theylive_consume_dom" class="nightlight_game_dom">
    <div class="layer1"></div>
    <div class="layer2"></div>
</div>

## Night Light with canvas

The background-image version of Night Light works okay, but the revealed image is sometimes a few pixels out of alignment, which weakens the illusion. This depends on how much you've resized your browser and is especially noticeable with the vertical lines on the "close out sale" window.

This was a good opportunity for me to get practice with canvas, and I find the results look a lot smoother, so here's the same game again.

<p>
<button onclick="return enable_fullpage_canvas(event);">Canvas on</button>
<button onclick="return disable_fullpage_canvas(event);">Canvas off</button>
</p>

<p>
<button onclick="return set_flashlight_mode('grayscale');">Grayscale</button>
<button onclick="return set_flashlight_mode('white');">Bright White</button>
<button onclick="return set_flashlight_mode('soft_light');">Soft light</button>
<button onclick="return set_flashlight_mode('invert');">Invert</button>
<button onclick="return set_flashlight_mode('party');">Party</button>
<button onclick="return set_flashlight_mode('wild_west');">Wild West</button>
<button onclick="return set_flashlight_mode('');">Off</button>
</p>

<canvas id="nightlight_bedroom_canvas" class="nightlight_game_canvas"></canvas>

<canvas id="nightlight_theylive_obey_canvas" class="nightlight_game_canvas"></canvas>

<canvas id="nightlight_theylive_consume_canvas" class="nightlight_game_canvas"></canvas>

Have fun!

[footnote_text] [Archived here](tonsky_me.html) in case it gets changed.

[footnote_text] A little vanity goes a long way!

<script>
function set_flashlight_mode(mode)
{
    light = document.getElementById("flashlight");
    light.className = mode;
}
function move_flashlight(event)
{
    light = document.getElementById("flashlight");
    light.style.left = `${event.clientX - 125}px`;
    light.style.top = `${event.clientY - 125}px`;
}

////////////////////////////////////////////////////////////////////////////////////////////////////

const fullpage_canvas = document.getElementById("fullpage_canvas");
let fullpage_canvas_enabled = false;

function preload_spooky_images()
{
    for (const img of document.getElementsByClassName("spooky_image"))
    {
        img.dataset.lightSrc = img.src;

        const spooky = new Image();
        spooky.src = img.dataset.darkSrc;
        window[Math.random()] = spooky;
    }
}
function move_canvas_flashlight(event)
{
    // console.log(event);
    if (! fullpage_canvas_enabled)
    {
        return;
    }
    const ctx = fullpage_canvas.getContext('2d');
    ctx.clearRect(0, 0, fullpage_canvas.width, fullpage_canvas.height);
    const region = new Path2D();
    // A little padding off screen helps ensure no slivers of light.
    region.rect(-10, -10, fullpage_canvas.width+20, fullpage_canvas.height+20);
    region.ellipse(event.clientX, event.clientY, 125, 125, Math.PI / 4, 0, 2 * Math.PI);
    ctx.fill(region, "evenodd");
}
function enable_fullpage_canvas(event)
{
    const ctx = fullpage_canvas.getContext("2d");
    ctx.rect(0, 0, fullpage_canvas.width, fullpage_canvas.height);
    ctx.fill()
    fullpage_canvas_enabled = true;

    document.body.classList.add("canvas_active");

    for (const img of document.getElementsByClassName("spooky_image"))
    {
        img.src = img.dataset.darkSrc;
        img.onload = null;
    }

    move_canvas_flashlight(event);
}
function disable_fullpage_canvas(event)
{
    // I want to wait for all the images to switch back before hiding the canvas.
    let wait_count = 0;
    function onload(event)
    {
        wait_count -= 1;
        if (wait_count > 0)
        {
            return;
        }
        const ctx = fullpage_canvas.getContext('2d');
        ctx.clearRect(0, 0, fullpage_canvas.width, fullpage_canvas.height);
        fullpage_canvas_enabled = false;
        document.body.classList.remove("canvas_active");
    }
    for (const img of document.getElementsByClassName("spooky_image"))
    {
        img.src = img.dataset.lightSrc;
        img.onload = onload;
        wait_count += 1;
    }

}
function resize_fullpage_canvas(event)
{
    fullpage_canvas.width = fullpage_canvas.offsetWidth;
    fullpage_canvas.height = fullpage_canvas.offsetHeight;
    move_canvas_flashlight(event);
}

////////////////////////////////////////////////////////////////////////////////////////////////////

function move_nightlight(event)
{
    const game = event.target.closest(".nightlight_game_dom");
    const l2 = game.querySelector(".layer2");
    const middle = l2.offsetWidth / 2;
    const x = event.offsetX - middle;
    const y = event.offsetY - middle;
    l2.style.left = x + "px";
    l2.style.top = y + "px";
    l2.style.backgroundPosition = `${x * -1}px ${y * -1}px`;
}
function enable_nightlight(event)
{
    const game = event.target.closest(".nightlight_game_dom");
    const l2 = game.querySelector(".layer2");
    l2.style.display = "block";
}
function disable_nightlight(event)
{
    const game = event.target.closest(".nightlight_game_dom");
    const l2 = game.querySelector(".layer2");
    l2.style.display = "";
}
function resize_nightlight(event)
{
    for (const game of document.getElementsByClassName("nightlight_game_dom"))
    {
        // console.log(game);
        const l1 = game.querySelector(".layer1");
        const l2 = game.querySelector(".layer2");

        const x = l1.offsetWidth;
        const y = l1.offsetHeight;
        l2.style.backgroundSize = `${x}px ${y}px`;
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////

const nightlight_bedroom_canvas = document.getElementById("nightlight_bedroom_canvas");
nightlight_bedroom_canvas.image_dark = new Image();
nightlight_bedroom_canvas.image_dark.src = "nightlight_1.png";
nightlight_bedroom_canvas.image_light = new Image();
nightlight_bedroom_canvas.image_light.src = "nightlight_2.png";

const nightlight_theylive_obey_canvas = document.getElementById("nightlight_theylive_obey_canvas");
nightlight_theylive_obey_canvas.image_dark = new Image();
nightlight_theylive_obey_canvas.image_dark.src = "theylive_obey_1.jpg";
nightlight_theylive_obey_canvas.image_light = new Image();
nightlight_theylive_obey_canvas.image_light.src = "theylive_obey_2.jpg";

const nightlight_theylive_consume_canvas = document.getElementById("nightlight_theylive_consume_canvas");
nightlight_theylive_consume_canvas.image_dark = new Image();
nightlight_theylive_consume_canvas.image_dark.src = "theylive_consume_1.jpg";
nightlight_theylive_consume_canvas.image_light = new Image();
nightlight_theylive_consume_canvas.image_light.src = "theylive_consume_2.jpg";

function nightlight_canvas_justdark(game)
{
    if (! game.image_dark.complete)
    {
        setTimeout(() => {nightlight_canvas_justdark(game);}, 100);
    }
    const ctx = game.getContext("2d");
    ctx.clearRect(0, 0, game.width, game.height);

    ctx.globalCompositeOperation = "source-over";
    ctx.drawImage(game.image_dark, 0, 0, game.width, game.height);
}

function move_nightlight_canvas(event)
{
    const game = event.target.closest(".nightlight_game_canvas");
    if (! (game.image_dark.complete && game.image_light.complete))
    {
        return;
    }
    const ctx = game.getContext("2d");
    ctx.clearRect(0, 0, game.width, game.height);

    ctx.globalCompositeOperation = "source-over";
    ctx.drawImage(game.image_light, 0, 0, game.width, game.height);

    ctx.globalCompositeOperation = "destination-in";
    ctx.beginPath();
    const light_size = game.height / 6;
    ctx.ellipse(event.offsetX, event.offsetY, light_size, light_size, Math.PI / 4, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill();

    ctx.globalCompositeOperation = "destination-over";
    ctx.drawImage(game.image_dark, 0, 0, game.width, game.height);
}

function resize_nightlight_canvas(event)
{
    for (const game of document.getElementsByClassName("nightlight_game_canvas"))
    {
        game.width = game.offsetWidth;
        game.height = game.offsetHeight;
        nightlight_canvas_justdark(game);
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////

function on_pageload()
{
    // mix flashlight

    document.body.addEventListener("mousemove", move_flashlight);

    // fullpage flashlight

    preload_spooky_images();
    document.body.addEventListener("mousemove", move_canvas_flashlight);
    window.addEventListener("resize", resize_fullpage_canvas);
    resize_fullpage_canvas();

    // dom nightlight

    for (const game of document.getElementsByClassName("nightlight_game_dom"))
    {
        game.addEventListener("mousemove", move_nightlight);
        game.addEventListener("mouseenter", enable_nightlight);
        game.addEventListener("mouseleave", disable_nightlight);
    }
    window.addEventListener("resize", resize_nightlight);
    resize_nightlight();

    // canvas nightlight

    for (const game of document.getElementsByClassName("nightlight_game_canvas"))
    {
        game.addEventListener("mousemove", move_nightlight_canvas);
        game.addEventListener("mouseleave", () => {nightlight_canvas_justdark(game);});
    }
    window.addEventListener("resize", resize_nightlight_canvas);
    resize_nightlight_canvas();
}
document.addEventListener("DOMContentLoaded", on_pageload);
</script>
