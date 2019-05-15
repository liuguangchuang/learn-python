# -*- coding: utf-8 -*-
# Time: 2019/5/15 22:04
# Author: laugc
# Email: hahalgc@gmail.com
# File: py29_slots.py

"""
使用 __slots__
"""

from types import MethodType


class Student(object):
    # 用 tuple 定义允许绑定的属性名称，对继承的子类是不起作用
    # 实例只能绑定 name 和 age
    # 子类中也定义 __slots__，子类实例允许定义的属性就是自身的 __slots__ 加上父类的 __slots__
    __slots__ = ('name', 'age')


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


# 类绑定方法
Student.set_score = set_score

s = Student()
s.name = "Mike"
print(s.name)

# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(27)
print(s.age)

s.set_score(10)
print(s.score)
