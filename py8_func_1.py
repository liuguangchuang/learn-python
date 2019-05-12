# -*- coding: utf-8 -*-
# Time: 2019/5/10 21:50
# Author: laugc
# Email: hahalgc@gmail.com
# File: py8_func_1.py

"""
函数
"""

print(abs(-20))

# 类型转换
print(int('123'))
print(bool(1))

a = abs  # 变量 a 指向 abs 函数
print(a(-1))  # 所以也可以通过 a 调用 abs 函数
