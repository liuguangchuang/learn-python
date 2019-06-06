# -*- coding: utf-8 -*-
# Time: 2019/6/6 21:53
# Author: laugc
# Email: hahalgc@gmail.com
# File: py66_htmlparser.py

from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&#%s: ' % name)

    def handle_charref(self, name):
        print('&#%s: ' % name)


parser = MyHTMLParser()
# feed() 方法可以多次调用
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>
''')

# 特殊字符有两种，一种是英文表示的 &nbsp;，一种是数字表示的 &#1234;，这两种字符都可以通过 Parser 解析出来
