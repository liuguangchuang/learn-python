# -*- coding: utf-8 -*-
# Time: 2019/5/12 22:11
# Author: laugc
# Email: hahalgc@gmail.com
# File: py19_return_func.py

"""
返回函数
"""


# 函数作为返回值，传入可变参数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# f 为返回的函数，需调用才能输出值
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


# 函数 lazy_sum 中又定义了函数 sum，并且，内部函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，
# 当 lazy_sum 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为「闭包」Closure
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# 注：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 返回的函数引用了变量 i，但它并非立刻执行。等到 3 个函数都返回时，它们所引用的变量 i 已经变成了 3
# 所以值都是 9
f1, f2, f3 = count()
print(f1)
print(f1())
print(f2())
print(f3())

print("=========")


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
# 已绑定到函数参数的值不变
def count1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f1(i) 立刻被执行，因此 i 的当前值被传入 f1()
    return fs


f1, f2, f3 = count1()
print(f1)
print(f1())
print(f2())
print(f3())
