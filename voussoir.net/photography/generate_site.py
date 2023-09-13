import boto3
import io
import jinja2
import PIL.Image
import sys
import urllib.parse

import etiquette
import r2_credentials

from voussoirkit import dotdict
from voussoirkit import imagetools
from voussoirkit import pathclass
from voussoirkit import spinal
from voussoirkit import vlogging

log = vlogging.get_logger(__name__, 'photography_generate')

pdb = etiquette.photodb.PhotoDB('D:\\Documents\\Photos\\_etiquette')

s3 = boto3.resource('s3',
  endpoint_url = f'https://{r2_credentials.get_account_id()}.r2.cloudflarestorage.com',
  aws_access_key_id = r2_credentials.get_access_key(),
  aws_secret_access_key = r2_credentials.get_access_secret(),
)

bucket = s3.Bucket('voussoir')

S3_EXISTING_FILES = set(item.key for item in bucket.objects.filter(Prefix="photography/"))
PUBLISH_TAGNAME = 'voussoir_net_publish'
HEADLINER_TAGNAME = 'voussoir_net_headliner'
PHOTOGRAPHY_ROOTDIR = pathclass.Path(__file__).parent
ATOM_FILE = PHOTOGRAPHY_ROOTDIR.with_child('photography.atom')
DOMAIN_ROOTDIR = PHOTOGRAPHY_ROOTDIR.parent
DOMAIN_WEBROOT = 'https://voussoir.net'
PHOTOGRAPHY_WEBROOT = 'https://voussoir.net/photography'
S3_WEBROOT = 'https://files.voussoir.net'

SIZE_SMALL = 1440
SIZE_TINY = 360

def webpath(path, anchor=None):
    path = path.relative_to(DOMAIN_ROOTDIR, simple=True).replace('\\', '/').lstrip('/')
    path = DOMAIN_WEBROOT.rstrip('/') + '/' + path
    if anchor is not None:
        path += '#' + anchor.lstrip('#')
    return path

class Photo:
    def __init__(self, etq_photo, etq_album=None):
        self.etq_photo = etq_photo
        self.article_id = self.etq_photo.real_path.replace_extension('').basename

        if etq_album is None:
            parent_key = 'photography'
        else:
            parent_key = f'photography/{etq_album.title}'

        self.s3_key = f'{parent_key}/{self.etq_photo.real_path.basename}'
        self.small_key = f'{parent_key}/small_{self.etq_photo.real_path.basename}'
        self.tiny_key = f'{parent_key}/tiny_{self.etq_photo.real_path.basename}'

        self.color_class = 'monochrome' if self.etq_photo.has_tag('monochrome') else ''

        self.s3_exists = self.s3_key in S3_EXISTING_FILES;
        self.img_url = f'{S3_WEBROOT}/{self.s3_key}'
        self.small_url = f'{S3_WEBROOT}/{self.small_key}'
        self.tiny_url = f'{S3_WEBROOT}/{self.tiny_key}'
        self.anchor_url = f'{DOMAIN_WEBROOT}/{parent_key}#{self.article_id}'
        self.published = imagetools.get_exif_datetime(self.etq_photo.real_path)

    def prepare(self):
        if not self.s3_exists:
            self.s3_upload()

    def make_thumbnail(self, size):
        image = PIL.Image.open(self.etq_photo.real_path.absolute_path)
        icc = image.info.get('icc_profile')
        (image_width, image_height) = image.size
        exif = image.getexif()
        (width, height) = imagetools.fit_into_bounds(image_width, image_height, size, size)
        image = image.resize((width, height), PIL.Image.LANCZOS)
        bio = io.BytesIO()
        image.save(bio, format='jpeg', quality=75, exif=exif, icc_profile=icc)
        bio.seek(0)
        return bio

    def s3_upload(self):
        log.info('Uploading %s as %s', self.etq_photo.real_path.absolute_path, self.s3_key)
        bucket.upload_fileobj(self.make_thumbnail(SIZE_SMALL), self.small_key)
        bucket.upload_fileobj(self.make_thumbnail(SIZE_TINY), self.tiny_key)
        bucket.upload_fileobj(self.etq_photo.real_path.open('rb'), self.s3_key)
        self.s3_exists = True

    def render_web(self, index=None, totalcount=None):
        if totalcount is not None:
            number_tag = f'<span class="number_tag">#{index}/{totalcount}</a>'
        else:
            number_tag = ''

        return f'''
        <article id="{self.article_id}" class="photograph {self.color_class}">
        <a href="{self.img_url}" target="_blank"><img src="{self.small_url}" loading="lazy"/></a>
        {number_tag}
        </article>
        '''

    def render_atom(self):
        return f'''
        <id>{self.article_id}</id>
        <title>{self.article_id}</title>
        <link rel="alternate" type="text/html" href="{self.anchor_url}"/>
        <updated>{self.published.isoformat()}</updated>
        <content type="html">
        <![CDATA[
        <a href="{self.img_url}"><img src="{self.small_url}"/></a>
        ]]>
        </content>
        '''

class Album:
    def __init__(self, etq_album):
        self.etq_album = etq_album
        self.article_id = self.etq_album.title
        self.photos = list(self.etq_album.get_photos())
        self.photos = [p for p in self.photos if p.has_tag(PUBLISH_TAGNAME)]
        self.photos = [Photo(etq_photo=photo, etq_album=self.etq_album) for photo in self.photos]
        self.photos.sort(key=lambda p: p.published)
        # self.link = webpath(path)
        self.web_url = f'{PHOTOGRAPHY_WEBROOT}/{self.article_id}'
        self.published = self.photos[0].published

    def prepare(self):
        for photo in self.photos:
            photo.prepare()

    def render_web(self, index=None, totalcount=None):
        headliners = [p for p in self.photos if p.etq_photo.has_tag(HEADLINER_TAGNAME)]

        return jinja2.Template('''
        <article id="{{article_id}}" class="album">
        <h1><a href="{{web_url}}">{{article_id}}</a></h1>
        <div class="albumphotos">
        {% for photo in headliners %}
        {{photo.render_web()}}
        {% endfor %}

        <div class="album_tinies">
        {% for photo in photos %}
        <a class="tiny_thumbnail {{photo.color_class}}" href="{{photo.anchor_url}}"><img src="{{photo.tiny_url}}" loading="lazy"/></a>
        {% endfor %}
        </div>
        </div>
        </article>
        ''').render(
            article_id=self.article_id,
            web_url=self.web_url,
            photos=self.photos,
            headliners=headliners,
        )

    def render_atom(self):
        photos = []
        for photo in self.photos:
            line = f'<article><a href="{photo.anchor_url}"><img src="{photo.small_url}" loading="lazy"/></a>'.replace('\\', '/')
            photos.append(line)
        photos = '\n'.join(photos)

        return f'''
        <id>{self.article_id}</id>
        <title>{self.article_id}</title>
        <link rel="alternate" type="text/html" href="{self.web_url}"/>
        <updated>{self.published.isoformat()}</updated>
        <content type="html">
        <![CDATA[
        {photos}
        ]]>
        </content>
        '''

def write(path, content):
    '''
    open() and write the file, with validation that it is in the writing dir.
    '''
    path = pathclass.Path(path)
    if path not in PHOTOGRAPHY_ROOTDIR:
        raise ValueError(path)
    print(path.absolute_path)
    path.write('w', content, encoding='utf-8')

def make_webpage(items, is_root, doctitle):
    rss_link = f'{PHOTOGRAPHY_WEBROOT}/{ATOM_FILE.basename}' if is_root else None
    back_link = None if is_root else PHOTOGRAPHY_WEBROOT
    sort_reverse = is_root

    html = jinja2.Template('''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    {% if rss_link %}
    <link rel="alternate" type="application/atom+xml" href="{{rss_link}}"/>
    {% endif %}
    <title>{{doctitle}}</title>

    <style>
    :root
    {
        --color_bodybg: #272822;
        --color_htmlbg: #1b1c18;
        --color_link: #ae81ff;
        --color_maintext: #ddd;

        --img_borderradius: 16px;
        --img_borderradius_tiny: 4px;
        --img_sepia: 0%;
        --img_huerotate: 0deg;
        --img_saturate: 100%;
        --img_blur: 0px;
        --img_mixblendmode: normal;
    }

    *, *:before, *:after
    {
        box-sizing: inherit;
        margin: 0;
    }

    .hidden
    {
        display: none !important;
    }

    html
    {
        height: 100vh;
        box-sizing: border-box;

        background-color: var(--color_htmlbg);
        color: var(--color_maintext);

        font-family: Verdana, sans-serif;
        font-size: 10pt;
    }

    body
    {
        width: 100em;
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 0;
        margin-bottom: 0;
        padding: 8px;
        padding-bottom:8vh;

        display: grid;
        grid-auto-flow: row;
        grid-row-gap: 12vh;
    }
    body.noscrollbar::-webkit-scrollbar
    {
        display: none;
    }
    body.noscrollbar
    {
        scrollbar-width: none;
    }

    a
    {
        color: var(--color_link);
        cursor: pointer;
    }

    h1
    {
        text-align: center;
    }

    article *
    {
        max-width: 100%;
        word-wrap: break-word;
    }

    header
    {
        width: 100%;
        max-width: 120em;
        margin-left: auto;
        margin-right: auto;
        text-align: end;
    }
    header > *
    {
        display: inline-block;
        padding: 16px;
        background-color: var(--color_bodybg);
    }

    .album,
    .photograph,
    .album_tinies
    {
        position: relative;
        margin-left: auto;
        margin-right: auto;
    }

    .album
    {
        width: 100%;
    }
    .album .albumphotos
    {
        width: 100%;
        display: grid;
        grid-auto-flow: row;
        grid-row-gap: 12vh;
    }
    .photograph
    {
        width: fit-content;
    }
    .photograph img
    {
        display: block;
        max-height: 92vh;
        border-radius: var(--img_borderradius);
        border: 1.25vh solid var(--color_bodybg);
        filter: hue-rotate(var(--img_huerotate)) saturate(var(--img_saturate)) blur(var(--img_blur));
        mix-blend-mode: var(--img_mixblendmode);
    }
    .photograph.monochrome img,
    .tiny_thumbnail.monochrome img
    {
        filter: sepia(var(--img_sepia)) hue-rotate(var(--img_huerotate)) saturate(var(--img_saturate)) blur(var(--img_blur));
    }
    .photograph .number_tag
    {
        position: absolute;
        bottom: 8px;
        right: 8px;
        text-align: center;
        background-color: white;
        padding: 1px;
        color: black;
        text-decoration: none;
        font-family: sans-serif;
        border-radius: 4px;
        font-weight: bold;
        opacity: 50%;
    }
    .album .album_tinies
    {
        max-width: 80em;
        text-align: justify;
    }
    .tiny_thumbnail
    {
        vertical-align: middle;
        display:inline-block;
        margin: 8px;
    }
    .tiny_thumbnail img
    {
        aspect-ratio: auto;
        border-radius: var(--img_borderradius_tiny);
        outline: 4px solid var(--color_bodybg);
        filter: hue-rotate(var(--img_huerotate)) saturate(var(--img_saturate)) blur(var(--img_blur));
        mix-blend-mode: var(--img_mixblendmode);
    }

    @media not print
    {
        .photograph img
        {
            box-shadow: #000 0px 0px 40px -10px;
        }
    }

    @media screen and (min-width: 600px)
    {
        .tiny_thumbnail img
        {
            height: 128px;
        }
    }

    @media screen and (max-width: 600px)
    {
        .tiny_thumbnail img
        {
            height: 64px;
        }
        .photograph
        {
            box-shadow: none;
        }
    }

    @media not all and (pointer: fine)
    {
        #keyboardhint,
        #scrollbartoggle
        {
            display: none;
        }
    }

    h1 {font-size: 2.00em;} h1 * {font-size: inherit;}
    h2 {font-size: 1.75em;} h2 * {font-size: inherit;}
    h3 {font-size: 1.50em;} h3 * {font-size: inherit;}
    h4 {font-size: 1.25em;} h4 * {font-size: inherit;}
    h5 {font-size: 1.00em;} h5 * {font-size: inherit;}

    #a_new_perspective
    {
        background-color: var(--color_bodybg);
        position: fixed;
        left: 8px;
        padding: 8px;
        border-radius: 8px;
    }

    </style>
    </head>

    <body>
    <header>
    <div id="keyboardhint">hint: <kbd>←</kbd> / <kbd>→</kbd></div>
    <a id="scrollbartoggle" onclick="return toggle_scrollbar();">scrollbar on/off</a>
    {% if rss_link %}
    <a href="{{rss_link}}">Atom</a>
    {% endif %}

    {%- if back_link -%}
    <a href="{{back_link}}">Back</a>
    {%- endif -%}
    </header>

    {% if not is_root %}
    <h1>{{doctitle}}</h1>
    {% endif %}

    {% for item in items %}
    {{item.render_web(index=loop.index, totalcount=none if is_root else (items|length))}}
    {% endfor %}


    <footer>
        <p>Ethan Dalool</p>
        <p>Contact me: photography@voussoir.net</p>
    </footer>

    <p><button id="new_perspective_button" onclick="return new_perspective_button_onclick(event);">👁️ Try a different perspective</button></p>

    <form id="a_new_perspective" class="hidden">
        <div><label>Background color: <input type="color" value="#1b1c18" oninput="return backgroundcolor_onchange(event);"/></label></div>
        <div><label>Border radius: <input type="range" min="0" value="16" max="500" oninput="return border_radius_onchange(event);"/></label> <span id="border_radius_value">16px</span></div>
        <div><label>Saturation: <input type="range" min="0" value="100" max="500" oninput="return saturate_onchange(event);"/></label> <span id="saturate_value">100%</span></div>
        <div><label>Hue rotate: <input type="range" min="0" value="0" max="360" oninput="return hue_rotate_onchange(event);"/></label> <span id="hue_rotate_value">0deg</span></div>
        <div><label>Blur: <input type="range" min="0" value="0" max="50" oninput="return blur_onchange(event);"/></label> <span id="blur_value">0%</span></div>
        <div><label>Mix blend mode: <select onchange="return mixblendmode_onchange(event);">
            <option selected>normal</option>
            <option>multiply</option>
            <option>screen</option>
            <option>overlay</option>
            <option>darken</option>
            <option>lighten</option>
            <option>color-dodge</option>
            <option>color-burn</option>
            <option>hard-light</option>
            <option>soft-light</option>
            <option>difference</option>
            <option>exclusion</option>
            <option>hue</option>
            <option>saturation</option>
            <option>color</option>
            <option>luminosity</option>
        </select></label></div>
    </form>
    </body>

    <script type="text/javascript">
    let desired_scroll_position = null;

    function toggle_scrollbar()
    {
        if (document.body.classList.contains("noscrollbar"))
        {
            document.body.classList.remove("noscrollbar");
            localStorage.setItem("show_scrollbar", "yes");
        }
        else
        {
            document.body.classList.add("noscrollbar");
            localStorage.setItem("show_scrollbar", "no");
        }
    }

    function load_scrollbar_setting()
    {
        if (localStorage.getItem("show_scrollbar") === "no")
        {
            document.body.classList.add("noscrollbar");
        }
        else
        {
            document.body.classList.remove("noscrollbar");
        }
    }

    const SCROLL_STOPS = Array.from(document.querySelectorAll("article.photograph img, .album_tinies"));
    function get_center_stop()
    {
        let center_x = window.innerWidth / 2;
        let center_y = window.pageYOffset + (window.innerHeight / 2);
        let final;
        for (const stop of SCROLL_STOPS)
        {
            const stop_top = stop.getBoundingClientRect().top + window.pageYOffset;
            const stop_bottom = stop_top + stop.offsetHeight;
            console.log("-----");
            console.log(stop);
            console.log(`${center_y} versus ${stop_top}--${stop_bottom}`);
            console.log("-----");
            if (center_y > stop_top)
            {
                final = stop;
            }
            else
            {
                break;
            }
        }
        if (final)
        {
            return final;
        }
    }
    function next_img(img)
    {
        const this_index = SCROLL_STOPS.indexOf(img);
        if (this_index === SCROLL_STOPS.length-1)
        {
            return img;
        }
        return SCROLL_STOPS[this_index + 1];
    }
    function previous_img(img)
    {
        const this_index = SCROLL_STOPS.indexOf(img);
        if (this_index === 0)
        {
            return img;
        }
        return SCROLL_STOPS[this_index - 1];
    }
    function scroll_step()
    {
        const distance = desired_scroll_position - document.documentElement.scrollTop;
        const jump = (distance * 0.25) + (document.documentElement.scrollTop < desired_scroll_position ? 1 : -1);
        document.documentElement.scrollTop = document.documentElement.scrollTop + jump;
        //console.log(`${document.documentElement.scrollTop} ${desired_scroll_position}`);
        const new_distance = desired_scroll_position - document.documentElement.scrollTop;
        if (Math.abs(new_distance / distance) < 0.97)
        {
            window.requestAnimationFrame(scroll_step);
        }
    }
    function scroll_to_stop(stop)
    {
        if (stop.offsetHeight > window.innerHeight)
        {
            desired_scroll_position = stop.getBoundingClientRect().top + window.pageYOffset;
        }
        else
        {
            const img_centerline = stop.getBoundingClientRect().top + window.pageYOffset + (stop.offsetHeight / 2);
            // document.documentElement.scrollTop = img_centerline - (window.innerHeight / 2);
            desired_scroll_position = Math.round(img_centerline - (window.innerHeight / 2));
        }
        scroll_step();
    }
    function scroll_to_next_img()
    {
        const current_stop = get_center_stop();
        if (current_stop)
        {
            scroll_to_stop(next_img(current_stop));
        }
    }
    function scroll_to_previous_img()
    {
        const current_stop = get_center_stop();
        if (current_stop)
        {
            scroll_to_stop(previous_img(current_stop));
        }
    }
    function arrowkey_listener(event)
    {
        if (event.keyCode === 37)
        {
            scroll_to_previous_img();
        }
        else if (event.keyCode === 39)
        {
            scroll_to_next_img();
        }
    }

    let hide_cursor_timeout = null;
    function hide_cursor()
    {
        document.documentElement.style.cursor = "none";
    }
    function show_cursor()
    {
        document.documentElement.style.cursor = "";
    }
    function mousemove_handler()
    {
        show_cursor();
        clearTimeout(hide_cursor_timeout);
        hide_cursor_timeout = setTimeout(hide_cursor, 3000);
    }

    function new_perspective_button_onclick(event)
    {
        const p = event.target.parentElement;
        document.getElementById("a_new_perspective").classList.remove("hidden");
        p.parentElement.removeChild(p);
    }

    function backgroundcolor_onchange(event)
    {
        document.documentElement.style.setProperty("--color_htmlbg", event.target.value);
    }

    function border_radius_onchange(event)
    {
        if (event.target.value == "500")
        {
            const value = "100%";
            document.documentElement.style.setProperty("--img_borderradius", value);
            document.documentElement.style.setProperty("--img_borderradius_tiny", value);
            document.getElementById("border_radius_value").textContent = value;
        }
        else
        {
            const value = event.target.value + "px";
            document.documentElement.style.setProperty("--img_borderradius", value);
            document.documentElement.style.setProperty("--img_borderradius_tiny", (event.target.value / 4) + "px");
            document.getElementById("border_radius_value").textContent = value;
        }
    }

    function saturate_onchange(event)
    {
        const value = event.target.value + "%";
        document.documentElement.style.setProperty("--img_saturate", value);
        if (event.target.value == "0")
        {
            document.getElementById("saturate_value").textContent = "Artistic";
        }
        else
        {
            document.getElementById("saturate_value").textContent = value;
        }
    }

    function hue_rotate_onchange(event)
    {
        const value = event.target.value + "deg";
        if (event.target.value === "0")
        {
            document.documentElement.style.setProperty("--img_sepia", "0");
        }
        else
        {
            document.documentElement.style.setProperty("--img_sepia", "100%");
        }
        document.documentElement.style.setProperty("--img_huerotate", value);
        document.getElementById("hue_rotate_value").textContent = value;
    }

    function blur_onchange(event)
    {
        const value = event.target.value + "px";
        document.documentElement.style.setProperty("--img_blur", value);
        document.getElementById("blur_value").textContent = value;
    }

    function mixblendmode_onchange(event)
    {
        document.documentElement.style.setProperty("--img_mixblendmode", event.target.value);
    }

    function on_pageload()
    {
        document.documentElement.addEventListener("keydown", arrowkey_listener);
        document.documentElement.addEventListener("mousemove", mousemove_handler);
        mousemove_handler();
        load_scrollbar_setting();
    }
    document.addEventListener("DOMContentLoaded", on_pageload);
    </script>
    </html>
    ''').render(
        is_root=is_root,
        doctitle=doctitle,
        rss_link=rss_link,
        back_link=back_link,
        items=items,
    )
    return html

def write_atom(items):
    atom = jinja2.Template('''
    <?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
        <title>voussoir.net/photography</title>
        <link href="https://voussoir.net/photography"/>
        <id>voussoir.net/photography</id>

        {% for item in items %}
        <entry>
            {{item.render_atom()}}
        </entry>
        {% endfor %}
    </feed>
    '''.strip()).render(items=items)
    write(ATOM_FILE, atom)

# write_directory_index(PHOTOGRAPHY_ROOTDIR)
# for directory in PHOTOGRAPHY_ROOTDIR.walk_directories():
#     write_directory_index(directory)

@vlogging.main_decorator
def main(argv):
    singlephotos = list(pdb.search(tag_mays=[PUBLISH_TAGNAME], has_albums=False, yield_albums=False, yield_photos=True).results)
    singlephotos += list(pdb.search(tag_mays=['voussoir_net_publish_single'], yield_albums=False, yield_photos=True).results)
    singlephotos = [Photo(p) for p in singlephotos]
    singlephotos.sort(key=lambda i: i.published, reverse=True)

    albums = list(pdb.search(tag_musts=[PUBLISH_TAGNAME], tag_forbids=['voussoir_net_publish_single'], has_albums=True, yield_albums=True, yield_photos=False).results)
    albums = [Album(a) for a in albums]
    albums.sort(key=lambda i: i.published, reverse=True)

    items = singlephotos + albums
    items.sort(key=lambda i: i.published, reverse=True)

    for item in items:
        item.prepare()

    log.info('Writing homepage')
    homepage_html = make_webpage(items, is_root=True, doctitle='photography')
    homepage_file = PHOTOGRAPHY_ROOTDIR.with_child('photography.html')
    homepage_file.write('w', homepage_html)

    for album in albums:
        album_html = make_webpage(album.photos, is_root=False, doctitle=album.article_id)
        album_file = PHOTOGRAPHY_ROOTDIR.with_child(album.article_id).replace_extension('html')
        log.info('Writing %s', album_file.absolute_path)
        album_file.write('w', album_html)

    write_atom(items)

    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
