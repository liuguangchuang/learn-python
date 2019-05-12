# -*- coding: utf-8 -*-
# Time: 2019/5/11 11:25
# Author: laugc
# Email: hahalgc@gmail.com
# File: py12_slice.py

"""
切片
"""

# 定义 list
l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 0、1、2，不包含 3
print(l[0:3])
print(l[:3])

# -1 表示倒数第一个
print(l[-2:-1])

l1 = list(range(100))
# 最后 10 个数
print(l1[-10:])

# 每 5 个取一个数
print(l1[::5])

print('ABCDEFG'[:3])

print('ABCDEFG'[::2])
