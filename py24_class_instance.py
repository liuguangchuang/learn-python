# -*- coding: utf-8 -*-
# Time: 2019/5/13 22:47
# Author: laugc
# Email: hahalgc@gmail.com
# File: py24_class_instance.py

"""
类和实例
"""


# 继承自 object
class Student(object):
    # __init__ 方法的第一个参数永远是 self
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


s = Student('lau', 12)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


print_score(s)
print(s.get_grade())
