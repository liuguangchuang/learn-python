# -*- coding: utf-8 -*-
# Time: 2019/6/3 22:21
# Author: laugc
# Email: hahalgc@gmail.com
# File: py62_contextlib_1.py

"""
contextlib
"""

try:
    f = open('C:\\Users\\lgc15\\Desktop\\a.txt', 'r')
    f.read()
finally:
    if f:
        f.close()

# 简化
with open('C:\\Users\\lgc15\\Desktop\\a.txt', 'r') as f:
    f.read()


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('end')

    def query(self):
        print('query info about %s...' % self.name)


# q = Query('laugc')
# print(q.query())

with Query('laugc') as q:
    q.query()
