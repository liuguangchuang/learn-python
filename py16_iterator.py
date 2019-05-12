# -*- coding: utf-8 -*-
# Time: 2019/5/11 16:06
# Author: laugc
# Email: hahalgc@gmail.com
# File: py16_iterator.py

"""
迭代器
凡是可作用于 for 循环的对象都是 Iterable 类型
凡是可作用于 next() 函数的对象都是 Iterator 类型
"""
from collections import Iterable, Iterator

# 判断一个对象是否是 Iterable 对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器 Iterator
# 判断一个对象是否是 Iterator 对象
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
