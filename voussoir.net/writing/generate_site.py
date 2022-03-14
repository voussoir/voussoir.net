import bs4
import etiquette
import html
import jinja2
import os
import pprint
import re
import subprocess
import vmarkdown

from voussoirkit import pathclass
from voussoirkit import spinal
from voussoirkit import winwhich

P = etiquette.photodb.PhotoDB(ephemeral=True)

WRITING_ROOTDIR = pathclass.Path(__file__).parent

GIT = winwhich.which('git')

ARTICLE_TEMPLATE = '''
[Back to writing](/writing)

{body}

---

[View this document's history]({github_history})

{commits}
'''

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

def git_file_edited_date(path):
    '''
    Return the YYYY-MM-DD date of the most recent commit that touched this file,
    ignoring commits marked as "[minor]".
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
        '--date=short',
        r'--grep=\[minor\]',
        '--invert-grep',
        '--',
        path,
    ]
    output = check_output(command)
    return output

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
        '--pretty=format:%H %ad %s',
        '--date=short',
        '--',
        path,
    ]
    output = check_output(command)
    lines = [line for line in output.splitlines() if line.strip()] #'*' in line]
    lines = [re.sub(r'([\*\_\[\]\(\)\^])', r'\\\1', line) for line in lines]
    lines = [line.split(' ', 1) for line in lines]
    return lines

def git_file_published_date(path):
    '''
    Return the YYYY-MM-DD date of the commit where this file first appeared.
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
        '--date=short',
        '--',
        path,
    ]
    output = check_output(command)
    return output

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
    def fixby(tagname, attribute):
        links = soup.find_all(tagname)
        for link in links:
            href = link[attribute]
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
        self.date = git_file_published_date(self.md_file)
        self.edited = git_file_edited_date(self.md_file)

        repo_path = git_repo_for_file(self.md_file)
        relative_path = self.md_file.relative_to(repo_path, simple=True).replace('\\', '/')
        github_history = f'https://github.com/voussoir/voussoir.net/commits/master/{relative_path}'

        commits = git_file_commit_history(self.md_file)
        self.publication_id = f'{commits[-1][0]}/{self.web_path}' if commits else None

        commits = [
            f'- [{html.escape(line)}](https://github.com/voussoir/voussoir.net/commit/{hash})'
            for (hash, line) in commits
        ]
        commits = '\n'.join(commits)

        md = vmarkdown.cat_file(self.md_file.absolute_path)
        md = ARTICLE_TEMPLATE.format(
            body=md,
            github_history=github_history,
            commits=commits,
        )
        self.soup = vmarkdown.markdown(
            md,
            css=WRITING_ROOTDIR.with_child('dark.css').absolute_path,
            return_soup=True,
        )
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

        articles = list(P.search(tag_musts=query))
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
    <html>
    <head>
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
        <a href="/writing/{{article.web_path}}">{{article.date}} - {{article.title|e}}</a>
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
        articles=sorted(index.articles, key=lambda a: a.date, reverse=True),
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
    <title>Writing</title>
    </head>

    <body>
    <article>
    <h1>Writing</h1>
    <ol class="article_list">
    {% for article in articles %}
        <li>
        <a href="{{article.web_path}}">{{article.date}} - {{article.title|e}}</a>
        </li>
    {% endfor %}
    </ol>

    <p>
    <a rel="alternate" type="application/atom+xml" href="/writing/writing.atom">Atom</a> /
    <a rel="alternate" type="application/rss+xml" href="/writing/writing.rss">RSS</a>
    </p>

    <h2>Recently edited</h2>
    <ol class="article_list">
    {% for article in articles_edited %}
        {% if article.edited and article.edited != article.date %}
        <li>
        <a href="{{article.web_path}}">{{article.edited}} - {{article.title|e}} ({{article.date}})</a>
        </li>
        {% endif %}
    {% endfor %}
    </ol>

    <h2>The footer</h2>
    <p>I greatly appreciate the time you have taken to visit my page. If you
    have feedback, corrections, or tales of harrowing adventure, send an email
    to writing@voussoir.net. If you want me to hold on to some of your dollars
    for permanent safekeeping,
    <a href="https://www.buymeacoffee.com/voussoir">click here</a>.</p>
    </article>
    </body>
    </html>
    ''').render(
        articles=sorted(ARTICLES.values(), key=lambda a: a.date, reverse=True),
        articles_edited=sorted(ARTICLES.values(), key=lambda a: a.edited, reverse=True)
    )
    write(WRITING_ROOTDIR.with_child('index.html'), page)

def write_atom():
    latest_date = max(article.date for article in ARTICLES_PUBLISHED.values())
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
            <link rel="alternate" type="text/html" href="https://voussoir.net/writing/{{article.web_path}}"/>
            <updated>{{article.date}}T00:00:00Z</updated>
            <content type="html">
            <![CDATA[
            {{article.soup.article}}
            ]]>
            </content>
        </entry>
        {% endfor %}
    </feed>
    '''.strip()).render(
        articles=sorted(ARTICLES_PUBLISHED.values(), key=lambda a: a.date, reverse=True),
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
            <link>https://voussoir.net/writing/{{article.web_path}}</link>
            <pubDate>{{article.date}}T00:00:00Z</pubDate>
            <description>
            <![CDATA[
            {{article.soup.article}}
            ]]>
            </description>
        </item>
        {% endfor %}
    </channel>
    </rss>
    '''.strip()).render(articles=sorted(ARTICLES_PUBLISHED.values(), key=lambda a: a.date, reverse=True))
    write(WRITING_ROOTDIR.with_child('writing.rss'), rss)

# GO
################################################################################
ARTICLES = {
    file: Article(file)
    for file in spinal.walk(WRITING_ROOTDIR)
    if file.extension == 'md' and file.parent != WRITING_ROOTDIR
}

ARTICLES_PUBLISHED = {file: article for (file, article) in ARTICLES.items() if article.publication_id}

write_articles()
complete_tag_index = Index()
all_tags = set(P.get_tags())
permute(all_tags)
write_tag_pages(complete_tag_index)
write_writing_index()
write_atom()
write_rss()
