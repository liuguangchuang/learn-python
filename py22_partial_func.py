# -*- coding: utf-8 -*-
# Time: 2019/5/13 22:12
# Author: laugc
# Email: hahalgc@gmail.com
# File: py22_partial_func.py

"""
偏函数
可以降低函数调用的难度
"""

import functools

# int() 函数默认按十进制转换
print(int('12345', base=8))
print(int('12345', base=16))


def int2(x, base=2):
    return int(x, base)


# 偏函数
int3 = functools.partial(int, base=2)
print(int3('1000000'))

# 以上偏函数相当于
kw = {'base': 2}
int('10010', **kw)

# 10 会作为 *args 的一部分自动加到左边
max1 = functools.partial(max, 10)
print(max1(1, 6, 8))
