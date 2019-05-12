# -*- coding: utf-8 -*-
# Time: 2019/5/12 22:05
# Author: laugc
# Email: hahalgc@gmail.com
# File: py18_sorted.py

"""
排序算法
"""

# list 排序
print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

# 按照 ASCII 的大小比较，Z < a
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
