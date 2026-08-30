import argparse
import bs4
import datetime
import dateutil.parser
import email
import email.parser
import email.policy
import html
import imapclient
import pyperclip
import re
import sys
import textwrap
import time

from voussoirkit import betterhelp
from voussoirkit import interactive
from voussoirkit import niceprints
from voussoirkit import pathclass
from voussoirkit import vlogging

import spambot_credentials

log = vlogging.getLogger(__name__, 'spambot')
vlogging.getLogger('imapclient').setLevel(vlogging.WARNING)

TEMPLATE = '''
<article id="{article_id}">
{selectheaders}
    <details>
    <summary>Headers</summary>
    <pre>
{headers}
    </pre>
    </details>

    <hr/>

{body}
</article>
'''.strip()

def normalize_body(body):
    body = body.replace('\r', '')
    soup = bs4.BeautifulSoup(body, 'html.parser')
    # print(niceprints.solid_hash_header('ORIGINAL BODY'))
    # print(repr(str(soup)))

    for doctype in soup.find_all(string=lambda s: isinstance(s, bs4.Doctype)):
        doctype.decompose()

    for comment in soup.find_all(string=lambda s: isinstance(s, bs4.Comment)):
        comment.decompose()

    for chaff in soup.find_all(['style', 'meta', 'title', 'wbr']):
        chaff.decompose()

    for img in soup.find_all('img'):
        alt_text = img.get('alt', '')
        alt_text = f'"{alt_text}"' if alt_text else ''
        src = img.get('src')
        if src.startswith('data:'):
            src = 'data:...'

        parts = ['img', alt_text, src]
        parts = [x for x in parts if x]
        parts = ' '.join(parts)
        img.replace_with(f'<{parts}/>')

    for anchor in soup.find_all('a'):
        href = anchor.get('href', '')
        anchor.replace_with(f'{anchor.get_text()} <{href}>')

    for element in soup.find_all():
        element.attrs = {}

    print(niceprints.solid_hash_header('NO ATTRS BODY'))
    print(repr(str(soup)))

    # print('# BEFORE #################################')
    # print(repr(str(soup)))
    for span in soup.find_all(['span', 'a', 'img', 'strong', 'b', 'i', 'em', 'font']):
        span.replace_with(*(span.children))

    for navigablestring in soup.strings:
        navigablestring.replace_with(re.sub(r'\s+', ' ', navigablestring.string))

    for br in soup.find_all('br'):
        br.replace_with('\n')

    for hr in soup.find_all('hr'):
        hr.replace_with('\n\n------------------------------\n\n')

    for block_tag in soup.find_all(['div', 'h1', 'h2', 'h3']):
        block_tag.replace_with(*block_tag.children, '\n\n')
        # block_tag.name = 'p'

    for remaining_tag in soup.find_all():
        # if remaining_tag.name in {'table', 'thead', 'tbody', 'tr', 'td', 'th'}:
        #     continue
        remaining_tag.replace_with(*remaining_tag.children, '\n\n')

    # for table in soup.find_all('table'):
    #     if not table.get_text().strip():
    #         table.decompose()

    soup.smooth()
    # print(niceprints.in_box('\n'.join(textwrap.wrap(repr(str(soup)))), title='SMOOTHED'))

    for navigablestring in soup.strings:
        text = navigablestring.string
        text = re.sub(r'\n\s+\n', '\n\n', text)
        text = re.sub(r' +\n', '\n', text)
        text = re.sub(r'\n +', '\n', text)
        text = re.sub(r'  +', ' ', text)
        paragraphs = text.split('\n\n')
        paragraphs = [para.strip() for para in paragraphs]
        paragraphs = [para for para in paragraphs if para]
        new_elements = []
        for para in paragraphs:
            new_p = soup.new_tag('p')
            new_p.append(para)
            new_elements.append(new_p)
        navigablestring.replace_with(*new_elements)

    for navigablestring in soup.strings:
        text = navigablestring.string
        lines = text.split('\n')
        new_elements = []
        new_elements.append(lines.pop(0))
        for line in lines:
            new_elements.append(soup.new_tag('br'))
            new_elements.append(line)
        navigablestring.replace_with(*new_elements)

    print(niceprints.solid_hash_header('CHILDREN'))
    print(list(x.name for x in soup.children))

    # print('# AFTER #################################')
    # print(repr(str(soup)))

    # ret = str(soup)
    # ret = re.sub(r'\n\s+\n', '\n\n', ret)
    # ret = re.sub(r' +\n', '\n', ret)
    # ret = re.sub(r'\n +', '\n', ret)
    # ret = re.sub(r'  +', ' ', ret)
    ret = '\n'.join(str(child) for child in soup.children)
    # print('# FINAL CLEANUP ##########################')
    # print(repr(ret))
    return ret

def extract_full_body(message):
    html_parts = []
    plain_parts = []

    for part in message.walk():
        # Skip attachments
        if part.get_content_maintype() == 'multipart' or part.get_filename():
            log.debug('Skipping an attachment part.')
            continue

        content_type = part.get_content_type()
        if content_type == 'text/plain':
            log.debug('Found a plain part.')
            plain_parts.append(part.get_content())
        elif content_type == 'text/html':
            log.debug('Found an html part.')
            html_parts.append(part.get_content())

    if html_parts:
        return '\n'.join(html_parts)

    if plain_parts:
        return '\n'.join(plain_parts)

    return ''

def email_to_spamarticle(message):
    log.info(f'Processing message {message.article_id}.')

    # HEADERS PREP #################################################################################
    headers = '\n'.join([f'{html.escape(k)}: {html.escape(v)}' for (k, v) in message.items() if v])

    # These headers are shown prominently, while the rest of the headers are
    # inside the summary/details.
    selectheaders = []
    selectkeys = [
        'From',
        'Reply-To',
        'Return-Path',
        'To',
        'Cc',
        'Bcc',
        'Subject',
        'Date',
    ]
    for key in selectkeys:
        value = message.get(key)
        # print(key, repr(value))
        if not value:
            continue
        value = value.strip()
        if not value:
            continue
        selectheaders.append(f'<p><b>{key}</b>: {html.escape(value)}</p>')
    selectheaders = '\n'.join(selectheaders)
    selectheaders = textwrap.indent(selectheaders, '    ')

    # BODY PREP ####################################################################################

    html_body = message.get_body(preferencelist=('html',))
    html_body = html_body.get_content() if html_body else ''
    # print('# HTML BODY ##############################')
    # print(repr(html_body))
    plain_body = message.get_body(preferencelist=('plain',))
    plain_body = plain_body.get_content() if plain_body else ''
    # print('# PLAIN BODY #############################')
    # print(repr(plain_body))

    # if html_body:
    #     body = html_body
    #     log.debug('Using HTML body.')
    # elif plain_body:
    #     log.debug('Using plaintext body.')
    #     body = plain_body
    body = extract_full_body(message)

    body_lower = body.lower()
    if any(indicator in body_lower for indicator in {'<html', '<div', '<p', '<br', '<span'}):
        body = normalize_body(body)
    else:
        body = body.replace('\r', '')
        body = html.escape(body)
        body = [para.strip().replace('\n', '<br>') for para in body.split('\n\n')]
        body = [line for line in body if line]
        body = ['<p>' + line + '</p>' for line in body]
        body = '\n'.join(body)

    # print(niceprints.in_box('\n'.join('\n'.join(textwrap.wrap(line, 110)) for line in body.splitlines()), title='FINAL SPAM BODY'))
    body = textwrap.indent(body, '    ')

    ################################################################################################

    article = TEMPLATE.format(
        article_id=message.article_id,
        body=body,
        headers=headers,
        selectheaders=selectheaders,
    )
    print(niceprints.in_box('\n'.join('\n'.join(textwrap.wrap(line, 110)) for line in article.splitlines()), title='FINAL SPAM ARTICLE'))
    # print(niceprints.solid_hash_header('FINAL SPAM ARTICLE'))
    # print(article)
    return article

def fetch_messages(client):
    log.info(f'Searching {spambot_credentials.FOLDER}.')
    client.select_folder(spambot_credentials.FOLDER)
    message_uids = client.search(['NOT', 'DELETED'])
    response = client.fetch(message_uids, ['FLAGS', 'RFC822'])

    bytesparser = email.parser.BytesParser(policy=email.policy.default)
    messages = []
    for (uid, message) in response.items():
        message = bytesparser.parsebytes(message[b'RFC822'])
        if message.get('Date'):
            message.datetime = dateutil.parser.parse(message.get('Date'))
        else:
            continue
        message.uid = uid
        message.article_id = message.datetime.astimezone(datetime.timezone.utc).replace(microsecond=0).replace(tzinfo=None).isoformat()
        messages.append(message)

    messages.sort(key=lambda x: x.datetime)
    return messages

def spambot_argparse(args):
    spamfile = pathclass.Path(spambot_credentials.SPAMFILE_PATH)
    spamcontent = spamfile.read('r')
    belowline = '<!-- new items below this line -->'

    client = imapclient.IMAPClient(host=spambot_credentials.HOSTNAME)
    with client:
        log.info(f'Logging into {spambot_credentials.USERNAME}.')
        client.login(spambot_credentials.USERNAME, spambot_credentials.PASSWORD)

        messages = fetch_messages(client)
        log.info(f'Found {len(messages)} spams.')

        for message in messages:
            spamarticle = email_to_spamarticle(message)
            # spamarticle = textwrap.indent(spamarticle, '    ')
    
            # break
            # if not interactive.getpermission('ok?'):
            #     break

            log.info(f'Moving message {message.article_id} to Trash.')
            client.move([message.uid], 'Trash')
            spamcontent = spamcontent.replace(belowline, belowline + '\n\n' + spamarticle)
            spamfile.write('w', spamcontent)
            # break

    return 0

@vlogging.main_decorator
def main(argv):
    parser = argparse.ArgumentParser(
        description='''
        ''',
    )
    parser.set_defaults(func=spambot_argparse)

    return betterhelp.go(parser, argv)

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))



