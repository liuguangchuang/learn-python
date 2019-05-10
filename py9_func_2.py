# -*- coding: utf-8 -*-
# @Time : 2019/5/10 21:53
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py9_func_2.py


"""
自定义函数
"""
import math


# 数据类型检查函数 isinstance()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


# 空函数
def nop():
    pass


# 缺少了 pass，代码运行就会有语法错误
a = 2
if a >= 18:
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))

# 平方根
print(math.sqrt(4))
