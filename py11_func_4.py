# -*- coding: utf-8 -*-
# Time: 2019/5/10 23:34
# Author: laugc
# Email: hahalgc@gmail.com
# File: py11_func_4.py

"""
递归函数
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 尾递归是指，在函数返回的时候，调用自身本身，并且，return 语句不能包含表达式
# 尾递归方式
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
