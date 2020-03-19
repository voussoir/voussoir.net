import os
import bs4
import etiquette
import pprint
import vmarkdown
import jinja2
import subprocess

from voussoirkit import pathclass
from voussoirkit import spinal
from voussoirkit import winwhich

P = etiquette.photodb.PhotoDB(ephemeral=True)
P.log.setLevel(100)

writing_rootdir = pathclass.Path(__file__).parent

ARTICLE_TEMPLATE = '''
[Back to writing](/writing)

{body}
'''

def write(path, content):
    path = pathclass.Path(path)
    if path not in writing_rootdir:
        raise ValueError(path)
    print(path.absolute_path)
    f = open(path.absolute_path, 'w', encoding='utf-8')
    f.write(content)
    f.close()

GIT = winwhich.which('git')

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

def git_file_date(path):
    path = pathclass.Path(path)
    repo = git_repo_for_file(path)
    path = path.relative_to(repo, simple=True)
    command = [
        GIT,
        '-C', repo.absolute_path,
        'log',
        '--diff-filter=A',
        '--pretty=format:%ad',
        '--date=short',
        '--', path,
    ]
    # print(command)
    output = subprocess.check_output(command, stderr=subprocess.PIPE).decode('utf-8')
    return output

class Article:
    def __init__(self, md_file):
        self.md_file = pathclass.Path(md_file)
        self.html_file = self.md_file.replace_extension('html')
        self.web_path = self.md_file.parent.relative_to(writing_rootdir, simple=True)
        self.date = git_file_date(self.md_file)

        md = vmarkdown.cat_file(self.md_file.absolute_path)
        md = ARTICLE_TEMPLATE.format(
            body=md,
        )
        self.soup = vmarkdown.markdown(
            md,
            css=writing_rootdir.with_child('css').with_child('dark.css').absolute_path,
            return_soup=True,
        )
        self.title = self.soup.head.title.get_text()

        tag_links = self.soup.find_all('a', {'class': 'tag_link'})
        for tag_link in tag_links:
            tagname = tag_link['data-qualname'].split('.')[-1]
            tag_link['href'] = f'/writing/tags/{tagname}'

        self.tags = [a['data-qualname'] for a in tag_links]

    def __str__(self):
        return f'Article({self.md_file.absolute_path})'

ARTICLES = {file: Article(file) for file in spinal.walk_generator(writing_rootdir) if file.extension == 'md' and file.parent != writing_rootdir}

def write_articles():
    for article in ARTICLES.values():
        if article.md_file.replace_extension('').basename != article.md_file.parent.basename:
            print(f'Warning: {article} does not match folder name.')

        for qualname in article.tags:
            P.easybake(qualname)

        P.new_photo(article.md_file.absolute_path, tags=article.tags)
        html = str(article.soup)
        write(article.html_file.absolute_path, html)

class Index:
    def __init__(self):
        self.articles = []
        self.children = {}

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

def permute(query, pool):
    if query:
        query = remove_redundant(query)
        if complete_tag_index.get(query):
            return
        articles = list(P.search(tag_musts=query))
        if not articles:
            return
        articles = [ARTICLES[article.real_path] for article in articles]

        if len(query) > 1:
            previous = query[:-1]
            prevarticles = complete_tag_index.get(previous)
            # print(f'''
            #     query={query},
            #     docs={docs}
            #     previous={previous},
            #     prevdocs={prevdocs},
            # ''')
            if set(articles) == set(prevarticles):
                return
        s = str(query)
        if 'python' in s and 'java' in s:
            print('BAD', query, articles)
        complete_tag_index.assign(query, articles)
        # pprint.pprint(complete_tag_index)
        # complete_tag_index[query] = docs
        # print(query, pool, docs)

    for tag in pool:
        rest = pool.copy()
        rest.remove(tag)
        q = query + (tag,)
        permute(q, rest)


def maketagpage(index, path):
    path = [tag.name for tag in path]
    parent = path[:-1]
    parent = '/'.join(parent)
    path = '/'.join(path)

    page = jinja2.Template('''
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="/writing/css/dark.css"/>
    <style>
    body
    {
        display:grid;
        grid-template:
            "tagnav tagnav"
            "articles refine";
    }
    </style>
    </head>
    <body>
    <section style="grid-area:tagnav">
    <p><a href="/writing">Back to writing</a></p>
    {% if parent %}
    <a href="/writing/tags/{{parent}}">Back to {{parent}}</a>
    {% else %}
    <a href="/writing/tags">Back to tags</a>
    {% endif %}
    </section>

    {% if index.articles %}
    <section style="grid-area:articles">
    <h1>{{path}}</h1>
    <ul>
    {% for article in index.articles %}
    <li>
        <a href="/writing/{{article.web_path}}">{{article.title}}</a>
    </li>
    {% endfor %}
    </ul>
    </section>
    {% endif %}

    {% if index.children %}
    <section style="grid-area:refine">
    <h1>Refine your query</h1>
    <ul>
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

    </body>
    ''').render(
        parent=parent,
        index=index,
        path=path,
        children=sorted(tag.name for tag in index.children.keys()),
    )
    return page

def outs(index, path=[]):
    filepath = ['tags'] + [tag.name for tag in path] + ['index.html']
    for (child_name, child_index) in index.children.items():
        outs(child_index, path=path+[child_name])
    page = maketagpage(index, path)
    filepath = os.sep.join(filepath)
    filepath = writing_rootdir.join(filepath)
    os.makedirs(filepath.parent.absolute_path, exist_ok=True)
    write(filepath, page)

def write_tag_pages():
    outs(complete_tag_index)


def write_writing_index():
    page = jinja2.Template('''
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="/writing/css/dark.css"/>
    </head>

    <body>
    <h1>Writing</h1>
    <ul>
    {% for article in articles %}
        <li>
        <a href="{{article.web_path}}">{{article.date}} - {{article.title}}</a>
        </li>
    {% endfor %}
    </ul>
    </body>
    ''').render(
        articles=sorted(ARTICLES.values(), key=lambda a: a.date, reverse=True),
    )
    write(writing_rootdir.with_child('index.html'), page)

write_articles()
complete_tag_index = Index()
all_tags = set(P.get_tags())
permute(tuple(), all_tags)
write_tag_pages()
write_writing_index()