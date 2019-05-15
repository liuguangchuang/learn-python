# -*- coding: utf-8 -*-
# Time: 2019/5/14 22:42
# Author: laugc
# Email: hahalgc@gmail.com
# File: py28_attribute.py

"""
实例属性和类属性
"""


class Student(object):
    # 类属性
    name = 'Stu'

    def __init__(self, name):
        self.name = name


# 实例属性，优先级比类属性高
s = Student('Bob')
s.score = 90

# 删除实例属性
del s.score
