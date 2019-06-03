# -*- coding: utf-8 -*-
# Time: 2019/6/2 22:48
# Author: laugc
# Email: hahalgc@gmail.com
# File: py61_itertools.py

import itertools

"""
itertools 提供了非常有用的用于操作迭代对象的函数
"""

# count() 会创建一个无限的迭代器
natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cycle() 会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')  # 字符串也是序列的一种
# for c in cs:
#     print(c)

# repeat() 负责把一个元素无限重复下去，第二个参数为重复次数
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

natuals1 = itertools.count(1)
# takewhile() 根据条件判断来截取出一个有限的序列
ns1 = itertools.takewhile(lambda x: x <= 10, natuals1)
print(list(ns1))

# chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby() 把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
