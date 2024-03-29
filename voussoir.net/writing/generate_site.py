import bs4
import datetime
import dateutil.parser
import etiquette
import html
import jinja2
import os
import pprint
import re
import subprocess
import vmarkdown

from voussoirkit import dotdict
from voussoirkit import pathclass
from voussoirkit import spinal
from voussoirkit import winwhich

P = etiquette.photodb.PhotoDB(ephemeral=True)

WRITING_ROOTDIR = pathclass.Path(__file__).parent

GIT = winwhich.which('git')

# HELPERS
################################################################################
def check_output(command):
    return subprocess.check_output(command, stderr=subprocess.PIPE).decode('utf-8')

def write(path, content):
    '''
    open() and write the file, with validation that it is in the writing dir.
    '''
    path = pathclass.Path(path)
    if path not in WRITING_ROOTDIR:
        raise ValueError(path)
    print(path.absolute_path)
    f = path.open('w', encoding='utf-8')
    f.write(content)
    f.close()

# GIT
################################################################################
def git_repo_for_file(path):
    path = pathclass.Path(path)
    folder = path.parent
    prev = None
    while folder != prev:
        if folder.with_child('.git').exists:
            return folder
        prev = folder
        folder = folder.parent
    raise Exception('No Git repo.')

def git_file_edited_date(path) -> datetime.datetime:
    '''
    Return the ISO formatted date of the most recent commit that touched this
    file, ignoring commits marked as "[minor]".
    '''
    path = pathclass.Path(path)
    repo = git_repo_for_file(path)
    path = path.relative_to(repo, simple=True)
    command = [
        GIT,
        '-C', repo.absolute_path,
        'log',
        '-1',
        '--pretty=format:%ad',
        '--date=iso',
        r'--grep=\[minor\]',
        '--invert-grep',
        '--',
        path,
    ]
    date = check_output(command)
    if date:
        date = dateutil.parser.parse(date)
        # date = date.astimezone(datetime.timezone.utc)
        return date
    else:
        return datetime.datetime.now(datetime.timezone.utc)

def git_file_commit_history(path):
    '''
    Return tuples like (hash, 'YYYY-MM-DD commit message') for all commits that
    touched this file, most recent first.

    This is used for "view this document's history".
    '''
    path = pathclass.Path(path)
    repo = git_repo_for_file(path)
    path = path.relative_to(repo, simple=True)
    command = [
        GIT,
        '-C', repo.absolute_path,
        'log',
        '--follow',
        '--pretty=format:%H///%ad///%s',
        '--date=iso',
        '--',
        path,
    ]
    output = check_output(command)
    lines = [line for line in output.splitlines() if line.strip()] #'*' in line]
    lines = [line.split('///', 2) for line in lines]
    commits = []
    for (commit_hash, date, title) in lines:
        commit = dotdict.DotDict({
            'hash': commit_hash,
            'date': dateutil.parser.parse(date),
            'title': title,
        })
        commits.append(commit)
    commits.sort(key=lambda commit: commit.date, reverse=True)
    return commits

def git_file_published_date(path) -> datetime.datetime:
    '''
    Return the ISO formatted date of the commit where this file first appeared.
    '''
    path = pathclass.Path(path)
    repo = git_repo_for_file(path)
    path = path.relative_to(repo, simple=True)
    command = [
        GIT,
        '-C', repo.absolute_path,
        'log',
        '--follow',
        '--diff-filter=A',
        '--pretty=format:%ad',
        '--date=iso',
        '--',
        path,
    ]
    date = check_output(command)
    if date:
        date = dateutil.parser.parse(date)
        # date = date.astimezone(datetime.timezone.utc)
        return date
    else:
        return datetime.datetime.now(datetime.timezone.utc)

# SOUP
################################################################################
def soup_set_tag_links(soup):
    '''
    vmarkdown renders [tag:example] into
    <a class="tag_link" data-qualname="example">, with no href. At this point,
    let's add the href to voussoir.net.
    '''
    tag_links = soup.find_all('a', {'class': 'tag_link'})
    for tag_link in tag_links:
        tagname = tag_link['data-qualname'].split('.')[-1]
        tag_link['href'] = f'/writing/tags/{tagname}'

    tags = [a['data-qualname'] for a in tag_links]
    return tags

def soup_adjust_relative_links(soup, md_file, repo_path):
    '''
    The markdown files are stored in article/article.md so if they contain a
    relative link to some screenshot.png, naturally that file is
    article/screenshot.png. But because of the nginx rules where we visit
    /writing/article, the relative link thinks that it points to
    /writing/screenshot.png which doesn't exist. So this function turns all
    relative links into absolute links starting from /writing.
    '''
    folder = pathclass.Path(md_file.parent)
    writing_rootdir = pathclass.Path(WRITING_ROOTDIR)

    base = soup.new_tag('base')
    base['href'] = f'https://voussoir.net/writing/{folder.basename}/'
    soup.find('head').append(base)

    def fixby(tagname, attribute):
        links = soup.find_all(tagname)
        for link in links:
            href = link.get(attribute)
            if not href:
                continue
            if '://' in href:
                continue
            if href.startswith('/'):
                continue
            if href.startswith('#'):
                continue
            href = folder.join(href)
            href = '/' + href.relative_to(writing_rootdir.parent, simple=True).replace('\\', '/')
            if not href.startswith('/writing/'):
                raise ValueError('Somethings wrong with', href)
            link[attribute] = href
    fixby('a', 'href')
    fixby('img', 'src')
    fixby('video', 'src')
    fixby('audio', 'src')
    fixby('source', 'src')

# ARTICLE
################################################################################
class Article:
    def __init__(self, md_file):
        self.md_file = pathclass.Path(md_file)
        self.html_file = self.md_file.replace_extension('html')
        self.web_path = self.md_file.parent.relative_to(WRITING_ROOTDIR, simple=True).replace('\\', '/')
        self.web_path = f'https://voussoir.net/writing/{self.web_path}'

        self.published = git_file_published_date(self.md_file)
        self.published_iso = self.published.isoformat()
        self.published_date = self.published.strftime('%Y-%m-%d')

        self.edited = git_file_edited_date(self.md_file)
        self.edited_iso = self.edited.isoformat()
        self.edited_date = self.edited.strftime('%Y-%m-%d')

        repo_path = git_repo_for_file(self.md_file)
        relative_path = self.md_file.relative_to(repo_path, simple=True).replace('\\', '/')
        github_history = f'https://git.voussoir.net/voussoir/voussoir.net/commits/master/{relative_path}'

        commits = git_file_commit_history(self.md_file)
        self.publication_id = f'{commits[-1].hash}/{self.md_file.parent.basename}' if commits else None

        self.soup = vmarkdown.markdown(
            self.md_file.read('r', encoding='utf-8'),
            css=WRITING_ROOTDIR.with_child('dark.css').absolute_path,
            return_soup=True,
        )
        header = jinja2.Template('''
        <p><a href="/writing">Back to writing</a></p>
        ''').render()
        footer = jinja2.Template('''
        <hr/>
        <p><a href="{{github_history}}">View this document's history</a></p>
        <ul>
            {% for commit in commits %}
            <li><a href="https://git.voussoir.net/voussoir/voussoir.net/commit/{{commit.hash}}"><time datetime="{{commit.date.isoformat()}}">{{commit.date.strftime('%Y-%m-%d')}}</time> {{commit.title}}</a></li>
            {% endfor %}
        </ul>

        <address>Contact me: writing@voussoir.net</address>

        <p>If you would like to subscribe for more, add this to your RSS reader: <a rel="alternate" type="application/atom+xml" href="/writing/writing.atom">https://voussoir.net/writing/writing.atom</a></p>
        ''').render(
            github_history=github_history,
            commits=commits,
        )
        self.soup.article.insert(0, bs4.BeautifulSoup(header, 'html.parser'))
        self.soup.article.append(bs4.BeautifulSoup(footer, 'html.parser'))

        if self.soup.head.title:
            self.title = self.soup.head.title.get_text()
        else:
            self.title = self.md_file.basename

        self.tags = soup_set_tag_links(self.soup)
        soup_adjust_relative_links(self.soup, self.md_file, repo_path)

    def __repr__(self):
        return f'Article:{self.title}'

# TAG INDEX
################################################################################
class Index:
    def __init__(self):
        self.articles = []
        self.children = {}

    def __str__(self):
        return f'Index (articles={self.articles}) (children={self.children})'

    def navigate(self, query, create=False):
        dest = self
        while query:
            parent = query[0]
            if create:
                dest = dest.children.setdefault(parent, Index())
            else:
                dest = dest.children.get(parent)
                if not dest:
                    return
            query = query[1:]
        return dest

    def assign(self, query, articles):
        self.navigate(query, create=True).articles = articles

    def get(self, query):
        dest = self.navigate(query, create=False)
        if dest:
            return dest.articles
        return []

def remove_redundant(query):
    seen = set()
    newq = tuple()
    for tag in query:
        if tag in seen:
            continue
        newq += (tag,)
        seen.add(tag)
        seen.update(tag.walk_parents())
    return newq

def permute(pool, query=tuple()):
    if query:
        query = remove_redundant(query)
        if complete_tag_index.get(query):
            return

        articles = list(P.search(tag_musts=query, yield_photos=True).results)
        if not articles:
            return

        articles = [ARTICLES[article.real_path] for article in articles]

        # Only generate a page for this tag query if it contains different
        # results from the previous query. For example, if an article has tags
        # A, B, and C, but it is the only article with those tags, there's no
        # reason to generate tag pages for /A, /A/B, /A/B/C, all of which have
        # the same single result.
        if len(query) > 1:
            previous = query[:-1]
            prevarticles = complete_tag_index.get(previous)
            if set(articles) == set(prevarticles):
                return

        complete_tag_index.assign(query, articles)

    for tag in pool:
        rest = pool.copy()
        rest.remove(tag)
        q = query + (tag,)
        permute(rest, q)

# RENDER FILES
################################################################################
def write_articles():
    for article in ARTICLES.values():
        if article.md_file.replace_extension('').basename != article.md_file.parent.basename:
            print(f'Warning: {article} does not match folder name.')

        for qualname in article.tags:
            P.easybake(qualname)

        P.new_photo(article.md_file.absolute_path, tags=article.tags)
        html = str(article.soup)
        write(article.html_file.absolute_path, html)

def make_tag_page(index, path):
    path = [tag.name for tag in path]
    parent = path[:-1]
    parent = '/'.join(parent)
    path = '/'.join(path)

    page = jinja2.Template('''
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="icon" href="/favicon.png" type="image/png"/>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="/writing/dark.css"/>
    {% if path %}
    <title>Articles tagged {{path}}</title>
    {% else %}
    <title>Articles by tag</title>
    {% endif %}
    </head>
    <body>
    <article>
    <section style="grid-area:tagnav">
    <p><a href="/writing">Back to writing</a></p>
    {% if parent %}
    <a href="/writing/tags/{{parent}}">Back to {{parent}}</a>
    {% else %}
    <a href="/writing/tags">Back to tags</a>
    {% endif %}
    </section>

    {% if articles %}
    <section style="grid-area:articles">
    <h1>{{path}}</h1>
    <ol class="article_list">
    {% for article in articles %}
    <li>
        <a href="{{article.web_path}}"><time datetime="{{article.published_iso}}">{{article.published_date}}</time> - {{article.title|e}}</a>
    </li>
    {% endfor %}
    </ol>
    </section>
    {% endif %}

    {% if index.children %}
    <section style="grid-area:refine">
    <h1>Refine your query</h1>
    <ul class="article_list">
    {% for refine in children %}
    <li>
    {% if path %}
    <a href="/writing/tags/{{path}}/{{refine}}">{{refine}}</a>
    {% else %}
    <a href="/writing/tags/{{refine}}">{{refine}}</a>
    {% endif %}
    </li>
    {% endfor %}
    </ul>
    </section>
    {% endif %}

    </article>
    </body>
    </html>
    ''').render(
        parent=parent,
        index=index,
        articles=sorted(index.articles, key=lambda a: a.published, reverse=True),
        path=path,
        children=sorted(tag.name for tag in index.children.keys()),
    )
    return page

def write_tag_pages(index, path=[]):
    for (child_name, child_index) in index.children.items():
        write_tag_pages(child_index, path=path+[child_name])

    filepath = ['tags'] + [tag.name for tag in path] + ['index.html']
    filepath = os.sep.join(filepath)
    filepath = WRITING_ROOTDIR.join(filepath)
    filepath.parent.makedirs(exist_ok=True)

    page = make_tag_page(index, path)

    write(filepath, page)

def write_writing_index():
    page = jinja2.Template('''
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="/writing/dark.css"/>
    <link rel="alternate" type="application/atom+xml" href="/writing/writing.atom"/>
    <link rel="alternate" type="application/rss+xml" href="/writing/writing.rss"/>
    <title>writing</title>
    </head>

    <body>
    <article>
    <h1>Writing</h1>
    <ol class="article_list">
    {% for article in articles %}
        <li>
        <a href="{{article.web_path}}"><time datetime="{{article.published_iso}}">{{article.published_date}}</time> - {{article.title|e}}</a>
        </li>
    {% endfor %}
    </ol>

    <h2>Recently edited</h2>
    <ol class="article_list">
    {% for article in articles_edited %}
        {% if article.edited and article.edited != article.published %}
        <li>
        <a href="{{article.web_path}}"><time datetime="{{article.edited_iso}}">{{article.edited_date}}</time> - {{article.title|e}} ({{article.published_date}})</a>
        </li>
        {% endif %}
    {% endfor %}
    </ol>

    <h2>The footer</h2>
    <p>I greatly appreciate the time you have taken to visit my page. If you
    have feedback, corrections, or tales of harrowing adventure, send an email
    to writing@voussoir.net.

    <p>If you would like to subscribe for more, add this to your RSS reader: <a rel="alternate" type="application/atom+xml" href="/writing/writing.atom">https://voussoir.net/writing/writing.atom</a></p>

    </article>
    </body>
    </html>
    ''').render(
        articles=sorted(ARTICLES.values(), key=lambda a: a.published, reverse=True),
        articles_edited=sorted(ARTICLES.values(), key=lambda a: a.edited, reverse=True)
    )
    write(WRITING_ROOTDIR.with_child('index.html'), page)

def write_atom():
    latest_date = max(article.published for article in ARTICLES_PUBLISHED.values())
    atom = jinja2.Template('''
    <?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
        <title>voussoir.net/writing</title>
        <link href="https://voussoir.net/writing"/>
        <id>voussoir.net/writing</id>
        <updated>{{latest_date}}</updated>

        {% for article in articles %}
        <entry>
            <id>{{article.publication_id}}</id>
            <title>{{article.title|e}}</title>
            <link rel="alternate" type="text/html" href="{{article.web_path}}"/>
            <updated>{{article.published_iso}}</updated>
            <content type="html">
            <![CDATA[
            {{article.soup.article}}
            ]]>
            </content>
        </entry>
        {% endfor %}
    </feed>
    '''.strip()).render(
        articles=sorted(ARTICLES_PUBLISHED.values(), key=lambda a: a.published, reverse=True),
        latest_date=latest_date,
    )
    write(WRITING_ROOTDIR.with_child('writing.atom'), atom)

def write_rss():
    rss = jinja2.Template('''
    <?xml version="1.0" encoding="utf-8"?>
    <rss version="2.0">
    <channel>
        <title>voussoir.net/writing</title>
        <link>https://voussoir.net/writing</link>
        <description>voussoir's writing</description>

        {% for article in articles %}
        <item>
            <title>{{article.title|e}}</title>
            <guid isPermalink="false">{{article.publication_id}}</guid>
            <link>{{article.web_path}}</link>
            <pubDate>{{article.published_iso}}</pubDate>
            <description>
            <![CDATA[
            {{article.soup.article}}
            ]]>
            </description>
        </item>
        {% endfor %}
    </channel>
    </rss>
    '''.strip()).render(articles=sorted(ARTICLES_PUBLISHED.values(), key=lambda a: a.published, reverse=True))
    write(WRITING_ROOTDIR.with_child('writing.rss'), rss)

# GO
################################################################################
ARTICLES = {
    file: Article(file)
    for file in spinal.walk(WRITING_ROOTDIR)
    if file.extension == 'md' and file.parent != WRITING_ROOTDIR and '_unpublished' not in file.absolute_path
}

ARTICLES_PUBLISHED = {file: article for (file, article) in ARTICLES.items() if article.publication_id}

with P.transaction:
    write_articles()

complete_tag_index = Index()
all_tags = set(P.get_tags())
permute(all_tags)
write_tag_pages(complete_tag_index)
write_writing_index()
write_atom()
write_rss()
