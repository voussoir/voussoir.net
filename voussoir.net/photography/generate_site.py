import PIL.Image
import jinja2

from voussoirkit import dotdict
from voussoirkit import imagetools
from voussoirkit import pathclass
from voussoirkit import spinal

PHOTOGRAPHY_ROOTDIR = pathclass.Path(__file__).parent
DOMAIN_ROOTDIR = PHOTOGRAPHY_ROOTDIR.parent
CSS_CONTENT = PHOTOGRAPHY_ROOTDIR.with_child('dark.css').read('r', encoding='utf-8')

def write(path, content):
    '''
    open() and write the file, with validation that it is in the writing dir.
    '''
    path = pathclass.Path(path)
    if path not in PHOTOGRAPHY_ROOTDIR:
        raise ValueError(path)
    print(path.absolute_path)
    f = path.open('w', encoding='utf-8')
    f.write(content)
    f.close()

def render_photo(photo, d):
    small_name = make_thumbnail(photo)
    basename = '/' + photo.relative_to(DOMAIN_ROOTDIR, simple=True)
    thumb = '/' + small_name.relative_to(DOMAIN_ROOTDIR, simple=True)
    article_id = photo.replace_extension('').basename

    return f'''
    <article class="photograph" id="{article_id}">
    <a href="{basename}"><img src="{thumb}" loading="lazy"/></a>
    </article>
    '''

def render_album_preview(directory):
    photos = list(spinal.walk(
        directory,
        glob_filenames={'*.jpg'},
        exclude_filenames={'*_small*'},
        recurse=False,
        yield_directories=False,
    ))
    article_id = directory.basename
    photos.sort(key=lambda file: file.basename)
    firsts = photos[:5]
    remaining = photos[5:]
    if remaining:
        next_after_more = remaining[0].replace_extension('').basename
    else:
        next_after_more = None
    firsts = [render_photo(photo, pathclass.cwd()) for photo in firsts]

    return jinja2.Template('''
    <article id="{{article_id}}">
    <h1><a href="{{album_path}}">{{directory.basename}}</a></h1>
    {% for photo in firsts %}
    {{photo}}
    {% endfor %}

    {% if remaining > 0 %}
    <p class="morelink"><a href="{{album_path}}#{{next_after_more}}">{{remaining}} more</a></p>
    {% endif %}
    </article>
    ''').render(
        article_id=article_id,
        directory=directory,
        album_path='/photography/' + directory.relative_to(PHOTOGRAPHY_ROOTDIR, simple=True),
        next_after_more=next_after_more,
        firsts=firsts,
        remaining=len(remaining),
    )

def write_directory_index(directory):
    do_rss = directory == PHOTOGRAPHY_ROOTDIR
    do_back = directory != PHOTOGRAPHY_ROOTDIR
    sort_reverse = directory == PHOTOGRAPHY_ROOTDIR

    items = list(spinal.walk(
        directory,
        glob_filenames={'*.jpg'},
        exclude_filenames={'*_small*'},
        recurse=False,
        yield_directories=False,
    )) + list(directory.listdir_directories())
    items.sort(key=lambda p: p.basename, reverse=sort_reverse)

    items2 = []
    for item in items:
        article_id = item.replace_extension('').basename
        if item.is_file:
            ren = render_photo(item, directory)
            link = f'#{article_id}'
            published = imagetools.get_exif_datetime(item)
        else:
            ren = render_album_preview(item)
            link = f'/{article_id}'
            published = imagetools.get_exif_datetime(sorted(item.listdir_files())[0])
        if published is None:
            print(f'{item} lacks exif date')
        item = dotdict.DotDict(
            article_id=article_id,
            rendered=ren,
            link=link,
            published=published.isoformat(),
        )
        items2.append(item)
    items = items2

    page = jinja2.Template('''
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="alternate" type="application/atom+xml" href="/photography/photography.atom"/>
    <title>{{directory.basename}}</title>

    <style>
    {{css_content}}
    </style>
    </head>

    <body>
    <header>
    <span>hint: <kbd>←</kbd> / <kbd>→</kbd></span>
    {% if do_rss %}
    <a href="/photography/photography.atom">Atom</a>
    {% endif %}

    {% if do_back %}
    <a href="/photography">Back</a>
    {% endif %}
    </header>

    {% for item in items %}
    {{item.rendered}}
    {% endfor %}
    </body>

    <script type="text/javascript">
    let desired_scroll_position = null;

    function get_center_img()
    {
        let center_x = window.innerWidth / 2;
        let center_y = window.innerHeight / 2;
        while (true)
        {
            const element = document.elementFromPoint(center_x, center_y);
            if (element.tagName === "IMG")
            {
                return element;
            }
            center_y -= 20;
            if (center_y <= 0)
            {
                return null;
            }
        }
    }
    function next_img(img)
    {
        const images = Array.from(document.images);
        const this_index = images.indexOf(img);
        if (this_index === images.length-1)
        {
            return img;
        }
        return images[this_index + 1];
    }
    function previous_img(img)
    {
        const images = Array.from(document.images);
        const this_index = images.indexOf(img);
        if (this_index === 0)
        {
            return img;
        }
        return images[this_index - 1];
    }
    function scroll_step()
    {
        const distance = desired_scroll_position - document.body.scrollTop;
        const jump = (distance * 0.25) + (document.body.scrollTop < desired_scroll_position ? 1 : -1);
        document.body.scrollTop = document.body.scrollTop + jump;
        console.log(`${document.body.scrollTop} ${desired_scroll_position}`);
        if (document.body.scrollTop !== desired_scroll_position)
        {
            window.requestAnimationFrame(scroll_step);
        }
    }
    function scroll_to_img(img)
    {
        const img_centerline = img.offsetTop + (img.offsetHeight / 2);
        // document.body.scrollTop = img_centerline - (window.innerHeight / 2);
        desired_scroll_position = Math.round(img_centerline - (window.innerHeight / 2));
        scroll_step();
    }
    function scroll_to_next_img()
    {
        scroll_to_img(next_img(get_center_img()));
    }
    function scroll_to_previous_img()
    {
        scroll_to_img(previous_img(get_center_img()));
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
    function on_pageload()
    {
        document.documentElement.addEventListener("keydown", arrowkey_listener);
    }
    document.addEventListener("DOMContentLoaded", on_pageload);
    </script>
    </html>
    ''').render(
        css_content=CSS_CONTENT,
        directory=directory,
        do_rss=do_rss,
        do_back=do_back,
        items=items,
    )
    write(directory.with_child('index.html'), page)

    if do_rss:
        write_atom(items)

def write_atom(items):
    atom = jinja2.Template('''
    <?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
        <title>voussoir.net/photography</title>
        <link href="https://voussoir.net/photography"/>
        <id>voussoir.net/photography</id>

        {% for item in items %}
        <entry>
            <id>{{item.article_id}}</id>
            <title>{{item.article_id|e}}</title>
            <link rel="alternate" type="text/html" href="https://voussoir.net/photography{{item.link}}"/>
            <updated>{{item.published}}</updated>
            <content type="html">
            <![CDATA[
            {{item.rendered}}
            ]]>
            </content>
        </entry>
        {% endfor %}
    </feed>
    '''.strip()).render(items=items)
    write(PHOTOGRAPHY_ROOTDIR.with_child('photography.atom'), atom)

def make_thumbnail(photo):
    small_name = photo.replace_extension('').basename + '_small'
    small_name = photo.parent.with_child(small_name).add_extension(photo.extension)
    if small_name.is_file:
        return small_name
    image = PIL.Image.open(photo.absolute_path)
    (image_width, image_height) = image.size
    (width, height) = imagetools.fit_into_bounds(image_width, image_height, 1440, 1440)
    image = image.resize((width, height), PIL.Image.ANTIALIAS)
    image.save(small_name.absolute_path, quality=90)
    print(small_name)
    return small_name

write_directory_index(PHOTOGRAPHY_ROOTDIR)
for directory in PHOTOGRAPHY_ROOTDIR.walk_directories():
    write_directory_index(directory)
