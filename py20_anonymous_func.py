# -*- coding: utf-8 -*-
# Time: 2019/5/12 22:31
# Author: laugc
# Email: hahalgc@gmail.com
# File: py20_anonymous_func.py

"""
匿名函数
"""

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 匿名函数作为返回值
def build(x, y):
    return lambda: x * x + y * y


f = build(2, 3)
print(f())
