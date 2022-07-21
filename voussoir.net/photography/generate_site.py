import PIL.Image
import jinja2

from voussoirkit import dotdict
from voussoirkit import imagetools
from voussoirkit import pathclass
from voussoirkit import spinal

PHOTOGRAPHY_ROOTDIR = pathclass.Path(__file__).parent
DOMAIN_ROOTDIR = PHOTOGRAPHY_ROOTDIR.parent
CSS_CONTENT = PHOTOGRAPHY_ROOTDIR.with_child('dark.css').read('r', encoding='utf-8')

class Photo:
    def __init__(self, filepath):
        self.filepath = filepath
        self.thumbnail = make_thumbnail(filepath)
        self.article_id = filepath.replace_extension('').basename
        self.link = f'#{self.article_id}'
        self.published = imagetools.get_exif_datetime(filepath)

    def render_web(self, relative_directory=None):
        if relative_directory is None:
            basename = self.filepath.basename
            thumb = self.thumbnail.basename
        else:
            basename = self.filepath.relative_to(relative_directory, simple=True).replace('\\', '/')
            thumb = self.thumbnail.relative_to(relative_directory, simple=True).replace('\\', '/')
        return f'''
        <article id="{self.article_id}" class="photograph">
        <a href="{basename}" target="_blank"><img src="{thumb}" loading="lazy"/></a>
        </article>
        '''

    def render_atom(self):
        href = f'https://voussoir.net/photography{self.link}'
        imgsrc = 'https://voussoir.net/photography/' + self.thumbnail.relative_to(PHOTOGRAPHY_ROOTDIR, simple=True)
        return f'''
        <id>{self.article_id}</id>
        <title>{self.article_id}</title>
        <link rel="alternate" type="text/html" href="https://voussoir.net/photography{self.link}"/>
        <updated>{self.published.isoformat()}</updated>
        <content type="html">
        <![CDATA[
        <a href="{href}"><img src="{imgsrc}"/></a>
        ]]>
        </content>
        '''

class Album:
    def __init__(self, path):
        self.path = path
        self.article_id = path.basename
        self.link = f'/{self.article_id}'
        self.published = imagetools.get_exif_datetime(sorted(path.glob_files('*.jpg'))[0])
        self.photos = list(spinal.walk(
            self.path,
            glob_filenames={'*.jpg'},
            exclude_filenames={'*_small*'},
            recurse=False,
            yield_directories=False,
        ))
        self.photos.sort(key=lambda file: file.basename)
        self.photos = [Photo(file) for file in self.photos]

    def render_web(self):
        firsts = self.photos[:5]
        remaining = self.photos[5:]
        if remaining:
            next_after_more = remaining[0]
        else:
            next_after_more = None

        return jinja2.Template('''
        <article id="{{article_id}}" class="album">
        <h1><a href="{{album_path}}">{{directory.basename}}</a></h1>
        {% for photo in firsts %}
        {{photo.render_web(relative_directory=directory.parent)}}
        {% endfor %}

        {% if remaining > 0 %}
        <p class="morelink"><a href="{{album_path}}{{next_after_more.link}}">{{remaining}} more</a></p>
        {% endif %}
        </article>
        ''').render(
            article_id=self.article_id,
            directory=self.path,
            album_path=self.path.basename,
            next_after_more=next_after_more,
            firsts=firsts,
            remaining=len(remaining),
        )

    def render_atom(self):
        photos = []
        for photo in self.photos:
            href = 'https://voussoir.net/photography/' + photo.filepath.relative_to(PHOTOGRAPHY_ROOTDIR, simple=True)
            imgsrc = 'https://voussoir.net/photography/' + photo.thumbnail.relative_to(PHOTOGRAPHY_ROOTDIR, simple=True)
            line = f'<article><a href="{href}"><img src="{imgsrc}"/></a>'.replace('\\', '/')
            photos.append(line)
        photos = '\n'.join(photos)

        return f'''
        <id>{self.article_id}</id>
        <title>{self.article_id}</title>
        <link rel="alternate" type="text/html" href="https://voussoir.net/photography{self.link}"/>
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
    f = path.open('w', encoding='utf-8')
    f.write(content)
    f.close()

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

    items2 = []
    for item in items:
        if item.is_file:
            items2.append(Photo(item))
        else:
            items2.append(Album(item))

    items = items2
    items.sort(key=lambda item: item.published, reverse=sort_reverse)

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
    <div id="keyboardhint">hint: <kbd>←</kbd> / <kbd>→</kbd></div>
    {% if do_rss %}
    <a href="/photography/photography.atom">Atom</a>
    {% endif %}

    {% if do_back %}
    <a href="/photography">Back</a>
    {% endif %}
    </header>

    {% for item in items %}
    {{item.render_web()}}
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
        const new_distance = desired_scroll_position - document.body.scrollTop;
        if (Math.abs(new_distance / distance) < 0.97)
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
        hide_cursor_timeout = setTimeout(hide_cursor, 5000);
    }
    function on_pageload()
    {
        document.documentElement.addEventListener("keydown", arrowkey_listener);
        document.documentElement.addEventListener("mousemove", mousemove_handler);
        mousemove_handler();
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
            {{item.render_atom()}}
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
    image.save(small_name.absolute_path, quality=85)
    print(small_name)
    return small_name

write_directory_index(PHOTOGRAPHY_ROOTDIR)
for directory in PHOTOGRAPHY_ROOTDIR.walk_directories():
    write_directory_index(directory)
