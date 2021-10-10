Sending emails to myself
========================

In April, I wrote [operatornotify.py](https://github.com/voussoir/voussoirkit/blob/master/voussoirkit/operatornotify.py), a module which allows my programs to notify me of important information or errors. I was immediately very proud of it. It felt awesome to get so much impact out of a sub-100 line module as I went around hooking it up to my existing programs and getting the tracebacks from my horribly broken code delivered right to me.

![](ycdl_errors.png "there's more")

Since then, I have figured out which parts of the interface are most important, and boiled them down into a single decorator, so that adding `@operatornotify.main_decorator` is all it takes to get emails from a program. It's probably the best bang-for-buck code I've written in a while.

```Python
@operatornotify.main_decorator(subject='myprogram.py')
def main(argv):
    ...

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))

```

The most important part of operatornotify's design is that it takes advantage of your existing logging infrastructure. Although you can call `operatornotify.notify` whenever you want, it's much easier to add a log handler that captures WARNING level messages automatically. This has encouraged me to revisit some older programs that just used print statements and replace them with proper logging, which makes them easier to use and debug in general.

There are a few pain points that arise from using operatornotify as a log handler. For example:

- When using `@main_decorator`, you have to pick a subject line ahead of time and can't change it later. But to improve the skimmability of emails in my inbox, I like to prefix the subject lines with `⭕︎` if everything went okay [footnote_link] and `✕` if there was a warning, which obviously is not known until the end of runtime. I can imagine a few solutions but haven't decided which is most clean and appropriate for inclusion in the module [footnote_link].

- Not all messages cleanly fit into the integer levels of logging. For the programs I run as scheduled tasks, it's nice to receive some kind of message to know that they ran successfully and didn't just fail to launch, but I don't necessarily want to see all of their output since I trust the returned status of 0. So neither `--operatornotify-level WARNING` or `INFO` is really ideal.

But these inconveniences are vastly outweighed by the ability to add a single decorator function that immediately supercharges all of the existing log lines and encourages me to add better logging where I skimped on it earlier.

Then I took the next step towards this summit of email enlightenment: running the mail server myself. I figure there are three reasons I should self-host the mail for operatornotify:

1. The notifications usually contain private information or filepaths that I don't like to have sitting on a third-party server. I don't think these worries are justified since my email provider does at-rest encryption and uses SSL, but I just don't like it.

2. My code might wind up sending hundreds of emails in a row, and I don't want to do that to a third-party host.

3. It's a good chance for me to play with stuff I haven't tried before.

I'm using the [Maddy](https://github.com/foxcpp/maddy) email server, which is an all-in-one solution for both SMTP and IMAP. I also considered [Mail-in-a-Box](https://mailinabox.email/), but their documents specifically say that it's designed to have the whole machine to itself, which I don't want to do. The most widely known software is [Postfix](http://www.postfix.org/) for SMTP and [Dovecot](https://www.dovecot.org/) for IMAP, but I started drowning in the configuration of dovecot before even touching postfix, and gave up. I'm just a single user emailing myself. I like that maddy is just a single binary. So now I'm free to send myself as many thousands of emails as I want, containing whatever I want, using my own code and connecting to my own server.

[FairEmail](https://f-droid.org/en/packages/eu.faircode.email/) on Android supports IMAP IDLE, so I can get tracebacks anytime, anywhere. It's great.

Here are some ways I'm using operatornotify:

- My computer emails me after it boots. I configured the BIOS to automatically turn the computer back on after a power outage occurs, so I have an email letting me know roughly when that happened and what to expect next time I'm back.

- My OVH server emails itself after it boots. Then, it launches a few programs -- [etiquette.voussoir.net](https://etiquette.voussoir.net), [/u/Newsletterly](https://old.reddit.com/r/GoldTesting/comments/26xset/newsletter_bot_commands/), etc. -- and emails again me when all of those have finished starting and the processes appear in `pidof`. If I accidentally break something in my Python environment that prevents those programs from working, I'll know about it before too long.

- Most of my task scheduler jobs use `--operatornotify-level WARNING`. A lot of repetetive tasks that I used to do manually are now fully automated, but if they experience any errors (usually just network timeouts or 503s), I can re-run them at my convenience.

- I'm working on a daily "system heartbeat" email that gives me a rundown of all the daemon processes that should always be running, and all of the task scheduler jobs that ran throughout the day. Although adding operatornotify to a program can help me get its traceback, it doesn't help me when the program is totally broken and didn't even launch. For example, when I upgrade Python and forget to `pip install` a module, so the `ImportError` occurs before main ever runs. I'd rather not add an intermediate launcher that tries to launch the task and notifies me if that fails.

For the record, the code that actually sends the emails is in my `my_operatornotify.py`. The basic code you need is:

```Python
import email.message
import smtplib

def send_email(subject, body=''):
    sender = 'xxx'
    recipient = 'xxx'

    subject = str(subject)
    body = str(body)

    message = email.message.EmailMessage()
    message.add_header('From', sender)
    message.add_header('Subject', subject)
    message.add_header('To', recipient)
    message.set_payload(body, charset='utf-8')

    server = smtplib.SMTP_SSL('xxx', 465)
    server.login('username', 'password')
    server.send_message(message)
    server.quit()

def notify(subject, body=''):
    ...
    send_email(subject, body)
    ...
```

But I have some additional stuff in there to deal with retrying and eventually writing the message to my desktop if the mail server is unreachable.

To write the system heartbeat, I'm parsing the output of `schtasks` with the subprocess module:

```Python
import csv
import subprocess
from voussoirkit import winwhich

command = [
    winwhich.which('schtasks'),
    '/query',
    '/tn', '\\voussoir\\',
    '/fo', 'csv',
    '/v'
]
output = subprocess.check_output(
    command,
    stderr=subprocess.STDOUT,
    creationflags=subprocess.CREATE_NO_WINDOW,
)
output = output.decode('utf-8')
lines = output.splitlines()
reader = csv.DictReader(lines)
for line in reader:
    ...
```

[footnote_text] I wanted to use a checkmark, but the fonts on Android make all of the unicode check marks look [stupendously ugly](checkmarks.png). And Android doesn't let me change the system font outside of Daddy Google's approved list because I'm a big stupid dummy baby who can't be trusted with a ttf because I might get a boo-boo.


[footnote_text] I am using a stopgap solution in `my_operatornotify` that detects the phrase "Program finished, returned 0" to add the ⭕︎.
