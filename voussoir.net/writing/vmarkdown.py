import argparse
import base64
import bs4
import copy
import html
import mimetypes
import mistune
import os
import pygments
import pygments.formatters
import pygments.lexers
import pygments.token
import re
import regex
import requests
import string
import sys
import traceback
import warnings

from voussoirkit import betterhelp
from voussoirkit import pathclass

HTML_TEMPLATE = '''
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>

<style>
{css}
</style>
</head>

<body>
<article>
{body}
</article>
</body>
</html>
'''.strip()

SLUG_CHARACTERS = string.ascii_lowercase + string.digits + '_'

session = requests.Session()

class SyntaxHighlighting:
    def block_code(self, text, lang):
        inlinestyles = self.options.get('inlinestyles') or False
        linenos = self.options.get('linenos') or False
        return self._block_code(text, lang, inlinestyles, linenos)

    @staticmethod
    def _block_code(text, lang, inlinestyles=False, linenos=False):
        if not lang:
            text = text.strip()
            text = re.sub(r'^((?: {4})*) {1,2}([^\s]|$)', r'\1\2', text, flags=re.MULTILINE)
            return f'<pre><code>{mistune.escape(text)}</code></pre>\n'
        try:
            lexer = pygments.lexers.get_lexer_by_name(lang.lower(), stripall=True)
            # if isinstance(lexer, pygments.lexers.PythonLexer):
            #     lexer = pygments.lexers.PythonConsoleLexer()

            # But wait! Why aren't you doing this:
            #     formatter = pygments.formatters.HtmlFormatter(
            #         noclasses=inlinestyles,
            #         linenos=linenos,
            #         cssclass='highlight ' + (lang.lower() if lang else ''),
            #     )
            #     code = pygments.highlight(text, lexer, formatter).decode('utf-8')
            # ??
            did_newline = True
            elements = []
            for (token, text) in lexer.get_tokens(text):
                # print(token, repr(text))
                # This replacement is meant to deal with the strange +1 or +2
                # spaces that appear when a code block is inside a list.
                # As far as I can tell at the moment, the origin of these extra
                # spaces is somewhere beyond my control. So as long as I always
                # indent with 4 spaces (which I will), it should be sufficient
                # to truncate newline-then-whitespace to multiples of 4 spaces.
                if did_newline or '\n' in text:
                    # print('Replacing!!', re.findall(r'^((?: {4})*) {1,2}', text))
                    text = re.sub(r'^((?: {4})*) {1,2}([^\s]|$)', r'\1\2', text, flags=re.MULTILINE)
                    did_newline = False
                # print(token, repr(text))
                if '\n' in text:
                    did_newline = True
                if text.isspace():
                    elements.append(text)
                    continue
                css_class = pygments.token.STANDARD_TYPES.get(token, '')
                element = f'<span class="{css_class}">{html.escape(text)}</span>'
                elements.append(element)
            code = ''.join(elements)

            divclass = ['highlight']
            if lang:
                divclass.append(lang.lower())
            divclass = ' '.join(divclass)

            code = f'<div class="{divclass}"><pre>{code}</pre></div>'
            # if lang:
            #     code = code.replace('div class="highlight"', f'div class="highlight {lang.lower()}"')
            # if linenos:
            #     return f'<div class="highlight-wrapper">{code}</div>\n'
            return code
        except Exception:
            traceback.print_exc()
            return f'<pre class="{lang}"><code>{mistune.escape(text)}</code></pre>\n'


class VoussoirRenderer(
        SyntaxHighlighting,
        mistune.Renderer,
    ):
    pass

class VoussoirInlineGrammar(mistune.InlineGrammar):
    larr = re.compile(r'<--')
    rarr = re.compile(r'-->')
    mdash = re.compile(r'--')
    category_tag = re.compile(r'\[tag:([\w\.]+)\]')
    supers_one = re.compile(r'(\^+)([^\s\(]+)')
    _not_parens = r'[^()]+'
    _paren_pair = r'\(.+?\)'
    _supered = rf'(?:{_not_parens}|{_paren_pair}|(?1))'
    supers_many = regex.compile(rf'(?V1)(\^+)\(({_supered}*)\)')
    footnote_link = re.compile(r'\[footnote_link\]')
    footnote_text = re.compile(r'\[footnote_text\]')
    subreddit = re.compile(r'\/r\/[A-Za-z0-9_]+')
    redditor = re.compile(r'\/u\/[A-Za-z0-9_\-]+')
    youtube_embed = re.compile(r'\[youtube:([A-Za-z0-9_\-]{11})\]')
    checkbox_checked = re.compile(r'\[x\]')
    checkbox_unchecked = re.compile(r'\[ \]')
    dash_spacer = re.compile(r'^\s*-$', re.MULTILINE)
    # This `text` override is based on this article:
    # https://ana-balica.github.io/2015/12/21/mistune-custom-lexers-we-are-going-deeper/
    # in which we have to keep adding characters to the recognized list every
    # time we make a new rule. My additions so far are:
    # \- for --
    # \^ for superscript
    text = re.compile(r'^[\s\S]+?(?=[\\<!\[_*`~\-\^\/]|https?:\/\/| {2,}\n|$)')
    # This `escape` override is first taken from the mistune source.
    # My additions so far are:
    # ^ for escaping supers
    escape = re.compile(r'^\\([\\`*\^{}\[\]()#+\-.!_>~|])')

class VoussoirInline(mistune.InlineLexer):
    default_rules = copy.copy(mistune.InlineLexer.default_rules)
    default_rules.remove('text')
    default_rules.insert(0, 'checkbox_checked')
    default_rules.insert(0, 'checkbox_unchecked')
    default_rules.insert(0, 'mdash')
    default_rules.insert(0, 'larr')
    default_rules.insert(0, 'rarr')
    default_rules.insert(0, 'category_tag')
    default_rules.insert(0, 'supers_one')
    default_rules.insert(0, 'supers_many')
    default_rules.insert(0, 'footnote_link')
    default_rules.insert(0, 'footnote_text')
    default_rules.insert(0, 'dash_spacer')
    default_rules.insert(0, 'youtube_embed')
    default_rules.append('subreddit')
    default_rules.append('redditor')
    default_rules.append('text')

    def __init__(self, renderer, **kwargs):
        rules = VoussoirInlineGrammar()
        super().__init__(renderer, rules, **kwargs)

    def output_category_tag(self, m):
        qualname = m.group(1)
        tagname = qualname.split('.')[-1]
        return f'<a class="tag_link" data-qualname="{qualname}">[{tagname}]</a>'

    def output_checkbox_checked(self, m):
        return '<input type="checkbox" checked/>'

    def output_checkbox_unchecked(self, m):
        return '<input type="checkbox"/>'

    def output_footnote_link(self, m):
        global footnote_link_index
        ret = f'<a id="footnote_link_{footnote_link_index}" class="footnote_link" href="#footnote_text_{footnote_link_index}" data-index={footnote_link_index}>[{footnote_link_index}]</a>'
        footnote_link_index += 1
        return ret

    def output_footnote_text(self, m):
        global footnote_text_index
        ret = f'<a id="footnote_text_{footnote_text_index}" class="footnote_text" href="#footnote_link_{footnote_text_index}" data-index={footnote_text_index}>[{footnote_text_index}]</a>'
        footnote_text_index += 1
        return ret

    def output_mdash(self, m):
        return '&mdash;'

    def output_rarr(self, m):
        return '&rarr;'

    def output_larr(self, m):
        return '&larr;'

    def output_supers(self, m):
        carets = len(m.group(1))
        text = m.group(2)
        text = self.output(text)
        return f'{"<sup>" * carets}{text}{"</sup>" * carets}'

    def output_supers_one(self, m):
        return self.output_supers(m)

    def output_supers_many(self, m):
        return self.output_supers(m)

    def output_subreddit(self, m):
        # Hotfix. I'd like to be able to include /r/ and /u/ inside links
        # without having to escape it. But since these rules are processed after
        # the link rules, the m object doesn't contain anything that would help
        # us know we're inside a link. Need to think about this problem but for
        # now here's a stopgap solution.
        import inspect
        for x in inspect.stack():
            if x.function == '_process_link':
                return m.group(0)
        return f'<a href="https://old.reddit.com{m.group(0)}">{m.group(0)}</a>'

    def output_redditor(self, m):
        import inspect
        for x in inspect.stack():
            if x.function == '_process_link':
                return m.group(0)
        return f'<a href="https://old.reddit.com{m.group(0)}">{m.group(0)}</a>'

    def output_dash_spacer(self, m):
        return ''

    def output_youtube_embed(self, m):
        video_id = m.group(1)
        return f'''
        <center>
        <iframe width="711" height="400" frameborder="0" allow="encrypted-media"
        allowfullscreen src="https://www.youtube.com/embed/{video_id}"></iframe>
        </center>
        '''

class VoussoirBlockGrammar(mistune.BlockGrammar):
    # The single hyphen is used to create a split between elements that
    # would normally merge together, such as block quotes.
    dash_spacer = re.compile(r'^\s*-$', re.MULTILINE)

class VoussoirBlock(mistune.BlockLexer):
    default_rules = copy.copy(mistune.BlockLexer.default_rules)
    default_rules.insert(0, 'dash_spacer')

    def __init__(self, **kwargs):
        rules = VoussoirBlockGrammar()
        super().__init__(rules, **kwargs)

    def parse_dash_spacer(self, m):
        return ''

footnote_link_index = 1
footnote_text_index = 1

renderer = VoussoirRenderer()
inline = VoussoirInline(renderer)
block = VoussoirBlock()
VMARKDOWN = mistune.Markdown(renderer=renderer, inline=inline, block=block)

# GENERIC HELPERS
################################################################################
def cat_file(path):
    if isinstance(path, pathclass.Path):
        path = path.absolute_path
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def cat_files(paths):
    if not paths:
        return ''
    if isinstance(paths, str):
        return cat_file(paths)
    content = [cat_file(path) for path in paths]
    return '\n\n'.join(content)

# SOUP HELPERS
################################################################################
SECTION_SYMBOL = '§'

def add_header_anchors(soup):
    '''
    Give each <hX> an <a> to link to it.
    '''
    header_pattern = re.compile(rf'^h[2-6]$')
    used_slugs = set()

    for header in soup.find_all(header_pattern):
        slug = slugify(header.get_text())
        slug = uniqify_slug(slug, used_slugs)

        header['id'] = slug

        new_a = soup.new_tag('a')
        new_a['href'] = '#' + slug
        new_a['class'] = 'header_anchor_link'
        new_a.append(f' ({SECTION_SYMBOL})')
        header.append(new_a)

def add_toc(soup, max_level=None):
    '''
    Gather up all the header anchors and form a table of contents,
    which will be placed below the first h1 on the page, if the page has an h1.
    '''
    first_h1 = soup.h1
    if not first_h1:
        return

    def new_list(root=False):
        r = bs4.BeautifulSoup('<ol></ol>', 'html.parser')
        if root:
            return r
        return r.ol

    # Official HTML headers only go up to 6.
    if max_level is None:
        max_level = 6

    elif max_level < 1:
        raise ValueError('max_level must be >= 1.')

    header_pattern = re.compile(rf'^h[1-{max_level}]$')
    headers = soup.find_all(header_pattern)
    if headers == [first_h1]:
        return

    toc = new_list(root=True)
    toc.ol['id'] = 'table_of_contents'
    toc.ol.append('Table of contents')
    current_list = toc.ol
    current_list['level'] = None

    for header in headers:
        if header == first_h1:
            continue
        # 'hX' -> X
        level = int(header.name[1])

        toc_line = toc.new_tag('li')
        toc_a = toc.new_tag('a')

        toc_a.append(get_innertext(header).replace(f' ({SECTION_SYMBOL})', ''))
        toc_a['href'] = f'#{header["id"]}'
        toc_line.append(toc_a)

        if current_list['level'] is None:
            current_list['level'] = level

        while level < current_list['level']:
            # Because the sub-<ol> are actually a child of the last
            # <li> of the previous <ol>, we must .parent twice.
            # The second .parent is conditional because if the current
            # list is toc.ol, then parent is a Soup document object, and
            # parenting again would be a mistake. We'll recover from
            # this in just a moment.
            current_list = current_list.parent
            if current_list.name == 'li':
                current_list = current_list.parent
            # If the file has headers in a non-ascending order, like the
            # first header is an h4 and then an h1 comes later, then
            # this while loop would keep attempting to climb the .parent
            # which would take us too far, off the top of the tree.
            # So, if we reach `current_list == toc.ol` then we've
            # reached the root and should stop climbing. At that point
            # we can just snap current_level and use the root list again.
            # In the resulting toc, that initial h4 would have the same
            # toc depth as the later h1 since it never had parents.
            if current_list == toc:
                current_list['level'] = level
                current_list = toc.ol

        if level > current_list['level']:
            # In order to properly render nested <ol>, you're supposed
            # to make the new <ol> a child of the last <li> of the
            # previous <ol>. NOT a child of the prev <ol> directly.
            # Don't worry, .children can never be empty because on the
            # first <li> this condition can never occur, and new <ol>s
            # always receive a child right after being created.
            _l = new_list()
            _l['level'] = level
            final_li = list(current_list.children)[-1]
            final_li.append(_l)
            current_list = _l

        current_list.append(toc_line)

    for ol in toc.find_all('ol'):
        del ol['level']

    first_h1.insert_after(toc.ol)

def add_head_title(soup):
    '''
    Add the <title> element in <head> based on the text of the first <h1>.
    '''
    first_h1 = soup.h1
    if not first_h1:
        return

    text = get_innertext(first_h1)
    title = soup.new_tag('title')
    title.append(text)
    soup.head.append(title)

def embed_images(soup, cache=None):
    '''
    Find <img> srcs and either download the url or load the local file,
    and convert it to a data URI.
    '''
    for element in soup.find_all('img'):
        src = element['src']
        if cache is None:
            cache = {}
        if cache.get(src) is None:
            print('Fetching %s' % src)
            if src.startswith('https://') or src.startswith('http://'):
                response = session.get(src)
                response.raise_for_status()
                data = response.content
            else:
                data = pathclass.Path(src).read('rb')
            data = base64.b64encode(data).decode('ascii')
            mime = mimetypes.guess_type(src)[0]
            mime = mime if mime is not None else ''
            uri = f'data:{mime};base64,{data}'
            cache[src] = uri
        else:
            uri = cache[src]
        element['src'] = uri

def get_innertext(element):
    if isinstance(element, bs4.NavigableString):
        return element.string
    else:
        return element.get_text()

def next_element_sibling(element):
    '''
    Like nextSibling but skips NavigableString.
    '''
    while True:
        element = element.nextSibling
        if isinstance(element, bs4.NavigableString):
            continue
        return element

def previous_element_sibling(element):
    while True:
        element = element.previousSibling
        if isinstance(element, bs4.NavigableString):
            continue
        return element

def remove_leading_empty_nodes(element):
    '''
    Code <pre>s often start with an empty span, so this strips it off.
    '''
    children = list(element.children)
    while children:
        if get_innertext(children[0]) == '':
            children.pop(0).extract()
        else:
            break

def slugify(text):
    '''
    Filter text to contain only SLUG_CHARACTERS.
    '''
    text = text.lower()
    text = text.replace(' ', '_')
    text = [c for c in text if c in SLUG_CHARACTERS]
    text = ''.join(text)
    text = re.sub(r'_{2,}', '_', text)
    return text

def uniqify_slug(slug, used_slugs):
    '''
    If the given slug has already been used, give it a trailing _2 or _3 etc.
    '''
    count = 2
    try_slug = slug
    while try_slug in used_slugs:
        try_slug = f'{slug}_{count}'
        count += 1
    slug = try_slug
    used_slugs.add(slug)
    return slug

# HTML CLEANERS
################################################################################
def html_replacements(html):
    html = re.sub(r'<style>\s*</style>', '', html)
    html = html.replace(
        '<span class="o">&gt;&gt;</span><span class="o">&gt;</span>',
        '<span>&gt;&gt;&gt;</span>'
    )
    html = html.replace(
        '<span class="o">.</span><span class="o">.</span><span class="o">.</span>',
        '<span>...</span>'
    )
    return html

# SOUP CLEANERS
################################################################################
def fix_argument_call_classes(element):
    '''
    Given a <span class="n"> pointing to a function being called, this fixes
    the classes of all the keyword arguments from being plain names to being
    argument names.
    '''
    # print('INPUT', repr(element))
    paren_depth = 0
    last_known_candidate = None
    while True:
        element = next_element_sibling(element)
        # print(element, paren_depth)
        innertext = element.get_text()

        if innertext == '(':
            paren_depth += 1

        if innertext == ')':
            paren_depth -= 1

        if 'n' in element['class']:
            last_known_candidate = element

        if last_known_candidate and 'o' in element['class'] and innertext == '=':
            last_known_candidate['class'].remove('n')
            last_known_candidate['class'].append('narg')
            last_known_candidate = None

        if paren_depth == 0:
            break

def fix_argument_def_classes(element):
    '''
    Given a <span class="kd">def</span>, fix the function arguments so they are
    a special color like they're SUPPOSED TO BE.
    '''
    # print('INPUT', repr(element))
    do_color = True
    while True:
        element = next_element_sibling(element)
        # print(element)
        innertext = element.get_text()
        if innertext == ')' and next_element_sibling(element).get_text() == ':':
            break

        if innertext == '=':
            do_color = False

        elif innertext == ',':
            do_color = True

        elif do_color:
            if 'n' in element['class']:
                element['class'].remove('n')
                element['class'].append('narg')
            elif 'bp' in element['class']:
                element['class'].remove('bp')
                element['class'].append('narg')
            elif 'o' in element['class'] and innertext in ('*', '**'):
                # Fix *args, the star should not be operator colored.
                element['class'].remove('o')
                element['class'].append('n')

def fix_decorator_classes(element):
    '''
    Given the first element of a decorator expression, this gives the decorator
    class to all the siblings for the rest of the line, because pygments stops
    coloring after it finds a dot i.e. [@decorators].my_decorator.
    '''
    while True:
        if get_innertext(element).endswith('\n'):
            break

        if isinstance(element, bs4.NavigableString):
            element = element.nextSibling
            continue

        # print(element, element['class'])
        if element['class'] == ['n']:
            element['class'] = ['nd']

        element = element.nextSibling

def fix_repl_classes(element):
    '''
    Given a <pre> element, this function detects that this pre contains a REPL
    session when the first line starts with '>>>'.

    For REPL sessions, any elements on an input line (which start with '>>>' or
    '...') keep their styles, while elements on output lines are stripped of
    their styles.

    Of course you can confuse it by having an output which starts with '>>>'
    but that's not the point okay?
    '''
    remove_leading_empty_nodes(element)
    children = list(element.children)
    if not children:
        return

    if get_innertext(children[0]) != '>>>':
        return

    del_styles = None
    for child in children:
        if get_innertext(child).endswith('\n'):
            del_styles = None

        elif del_styles is None:
            del_styles = child.string not in ('>>>', '...')

        if isinstance(child, bs4.NavigableString):
            continue
        if del_styles:
            del child['class']

def fix_classes(soup):
    '''
    Because pygments does not conform to my standards of beauty already!
    '''
    for element in soup.find_all('span', {'class': 'k'}):
        if get_innertext(element) in ('def', 'class'):
            element['class'] = ['kd']

    for element in soup.find_all('span', {'class': 'bp'}):
        if get_innertext(element) in ('None', 'True', 'False'):
            element['class'] = ['m']

    for element in soup.find_all('span', {'class': 'o'}):
        if get_innertext(element) in ('.', '(', ')', '[', ']', '{', '}', ';', ','):
            element['class'] = ['n']

    for element in soup.find_all('pre'):
        fix_repl_classes(element)

    for element in soup.find_all('span', {'class': 'kd'}):
        if element.get_text() == 'def':
            fix_argument_def_classes(element)

    for element in soup.find_all('span', {'class': 'n'}):
        if get_innertext(element.nextSibling) == '(':
            fix_argument_call_classes(element)

    for element in soup.find_all('span', {'class': 'nd'}):
        fix_decorator_classes(element)

def fix_reddit_links(soup):
    for a in soup.find_all('a'):
        if not a.get('href'):
            continue
        a['href'] = re.sub(r'^(https?://)?(www\.)?reddit\.com', r'\1old.reddit.com', a['href'])

def inject_footnotes(soup):
    links = soup.find_all('a', {'class': 'footnote_link'})
    texts = soup.find_all('a', {'class': 'footnote_text'})
    texts = {text['data-index']: get_innertext(text.parent) for text in texts}
    for link in links:
        link['title'] = texts[link['data-index']]

def set_img_lazyload(soup):
    imgs = soup.find_all('img')
    for img in imgs:
        if not img.get('loading'):
            img['loading'] = 'lazy'

# FINAL MARKDOWNS
################################################################################
def markdown(
        md,
        *,
        css=None,
        do_embed_images=False,
        image_cache=None,
        return_soup=False,
    ):
    global footnote_link_index
    global footnote_text_index
    footnote_link_index = 1
    footnote_text_index = 1

    css = cat_files(css)

    body = VMARKDOWN(md)

    if footnote_link_index != footnote_text_index:
        links = footnote_link_index-1
        texts = footnote_text_index-1
        warnings.warn(f'There are {links} footnote links, but {texts} texts.')

    html = HTML_TEMPLATE.format(css=css, body=body)

    # HTML cleaning
    html = html_replacements(html)

    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Soup cleaning
    # Make sure to add_head_title before add_header_anchors so you don't get
    # the paragraph symbol in the <title>.
    add_head_title(soup)
    add_header_anchors(soup)
    add_toc(soup)
    fix_classes(soup)
    fix_reddit_links(soup)
    inject_footnotes(soup)
    set_img_lazyload(soup)

    if do_embed_images:
        embed_images(soup, cache=image_cache)

    if return_soup:
        return soup

    html = str(soup)
    return html

def markdown_flask(core_filename, port, *args, **kwargs):
    import flask
    from flask import request
    site = flask.Flask(__name__)
    image_cache = {}
    kwargs['image_cache'] = image_cache
    core_filename = pathclass.Path(core_filename)
    if core_filename.is_dir:
        cwd = core_filename
    else:
        cwd = pathclass.cwd()

    def handle_path(path):
        if path.extension == '.md':
            return do_md_for(path)

        if path.is_dir:
            atags = []
            if path in cwd:
                parent = path.parent.relative_to(cwd, simple=True)
                atags.append(f'<a href="/{parent}">..</a>')
            children = sorted(path.listdir(), key=lambda p: (p.is_file, p.basename.lower()))
            for child in children:
                relative = child.relative_to(cwd, simple=True)
                a = f'<p><a href="/{relative}">{child.basename}</a></p>'
                atags.append(a)
            atags = '\n'.join(atags)
            page = f'''
            <html>
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            </head>
            <body>
            {atags}
            </body>
            </html>
            '''.strip()
            return page

        try:
            content = open(path.absolute_path, 'rb').read()
        except Exception as exc:
            print(exc)
            flask.abort(404)
        else:
            response = flask.make_response(content)

            mime = mimetypes.guess_type(path.absolute_path)[0]
            if mime:
                response.headers['Content-Type'] = mime
            else:
                response.headers['Content-Type'] = None

            return response

    def do_md_for(filename):
        try:
            html = markdown(md=cat_file(filename), *args, **kwargs)
        except FileNotFoundError:
            flask.abort(404)
        refresh = request.args.get('refresh', None)
        if refresh is not None:
            refresh = 1000 * max(float(refresh), 1)
            html += f'<script>setTimeout(function(){{window.location.reload()}}, {refresh})</script>'
        return html

    @site.route('/')
    def root():
        return handle_path(core_filename)

    @site.route('/<path:path>')
    def other_file(path):
        path = cwd.join(path)
        if path not in cwd:
            flask.abort(404)
        return handle_path(path)

    site.run(host='0.0.0.0', port=port)

# COMMAND LINE
################################################################################
def markdown_argparse(args):
    if args.output_filename:
        md_file = pathclass.Path(args.md_filename)
        output_file = pathclass.Path(args.output_filename)
        if md_file == output_file:
            raise ValueError('md file and output file are the same!')

    kwargs = {
        'css': args.css,
        'do_embed_images': args.do_embed_images,
    }

    if args.server:
        return markdown_flask(core_filename=args.md_filename, port=args.server, **kwargs)

    html = markdown(cat_file(args.md_filename), **kwargs)

    if args.output_filename:
        f = open(args.output_filename, 'w', encoding='utf-8')
        f.write(html)
        f.close()
        return

    print(html)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('md_filename')
    parser.add_argument(
        '--css',
        action='append',
        default=None,
    )
    parser.add_argument(
        '--embed_images',
        '--embed-images',
        dest='do_embed_images',
        action='store_true',
    )
    parser.add_argument(
        '-o',
        '--output',
        dest='output_filename',
        default=None,
    )
    parser.add_argument(
        '--server',
        type=int,
        default=None,
    )
    parser.set_defaults(func=markdown_argparse)

    return betterhelp.go(parser, argv)

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
