# -*- coding: utf-8 -*-
# Time: 2019/6/7 17:20
# Author: laugc
# Email: hahalgc@gmail.com
# File: py70_chardet.py

from requests.packages import chardet

"""
编码
"""

print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data1 = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data1))

data2 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data2))
