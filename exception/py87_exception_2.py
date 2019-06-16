# -*- coding: utf-8 -*-
# Time: 2019/6/16 22:09
# Author: laugc
# Email: hahalgc@gmail.com
# File: py87_exception_2.py

filename = 'a.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    # pass 指跳过
    # pass
    msg = 'file ' + filename + ' not found'
    print(msg)
else:
    words = contents.split()
    print(len(words))
