# -*- coding: utf-8 -*-
# Time: 2019/5/19 15:12
# Author: laugc
# Email: hahalgc@gmail.com
# File: py35_meta_class.py

"""
元类
"""


# type() 创建类
# 先定义函数
def fn(self, name='world'):
    print('Hello, %s.' % name)


# type() 函数既可以返回一个对象的类型，又可以创建出新的类型
# 类名
# 继承的父类集合，如果只有一个父类，与 tuple 只有一个元素写法一样
# class 的方法名称与函数绑定，函数 fn 绑定到方法名 hello 上
# 创建 Hello class
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print(h)
