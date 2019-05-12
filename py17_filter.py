# -*- coding: utf-8 -*-
# Time: 2019/5/11 16:19
# Author: laugc
# Email: hahalgc@gmail.com
# File: py17_filter.py

"""
filter() 函数
"""


def is_odd(n):
    return n % 2 == 0


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 求素数
# 从 3 开始的奇数，无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 生成器，无限序列
def primes():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n, end=', ')
    else:
        break
