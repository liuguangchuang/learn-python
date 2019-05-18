# -*- coding: utf-8 -*-
# Time: 2019/5/18 22:32
# Author: laugc
# Email: hahalgc@gmail.com
# File: py33_custom_class_2.py

"""
定制类
"""


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a, b

    # 传入的参数可能是一个 int，也可能是一个切片对象 slice
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    # __next__() 方法拿到循环的下一个值
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)

f = Fib()
print(f[5])
