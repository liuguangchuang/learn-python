# -*- coding: utf-8 -*-
# @Time : 2019/5/11 15:20
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py14_list_generator.py
"""
列表生成式
"""
import os

l = list(range(1, 11))
print(l)

l1 = []
for x in range(1, 11):
    l1.append(x * x)
print(l1)

l2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l2)

l3 = [m + n for m in 'ABC' for n in 'XYZ']
print(l3)

# os.listdir 可以列出文件和目录
l4 = [d for d in os.listdir('.')]
print(l4)

# dict 的 items() 可以同时迭代 key 和 value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 把 list 中所有的字符串变成小写
l5 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in l5])
