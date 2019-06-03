# -*- coding: utf-8 -*-
# Time: 2019/6/3 22:37
# Author: laugc
# Email: hahalgc@gmail.com
# File: py63_contextlib_2.py

from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info about %s...' % self.name)


# @contextmanager 这个 decorator 接受一个 generator，用 yield 语句把 with ... as var 把变量输出出去，
# with 语句就可以正常地工作
@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')


with create_query('laugc') as q:
    q.query()


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)


# with 语句首先执行 yield 之前的语句，因此打印出 <h1>
# yield 调用会执行 with 语句内部的所有语句，因此打印出 hello
# 最后执行 yield 之后的语句，打印出 </h1>
with tag('h1'):
    print('hello')

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
