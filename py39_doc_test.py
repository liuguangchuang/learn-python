# -*- coding: utf-8 -*-
# Time: 2019/5/19 21:45
# Author: laugc
# Email: hahalgc@gmail.com
# File: py39_doc_test.py

"""
文档测试
"""

import re

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))


def abs(n):
    '''
    Function to get absolute value of number.
    Example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)


print(abs(10))
