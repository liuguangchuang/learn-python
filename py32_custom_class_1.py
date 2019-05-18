# -*- coding: utf-8 -*-
# Time: 2019/5/15 22:48
# Author: laugc
# Email: hahalgc@gmail.com
# File: py32_custom_class_1.py

"""
定制类
"""


# __str__
class Student(object):
    def __init__(self):
        self.name = 'lau'

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 只有在没有找到属性的情况下，才调用 __getattr__
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    # __call__() 方法，就可以直接对实例进行调用
    def __call__(self):
        print('My name is %s.' % self.name)


s = Student()
print(s)
print(s())
print(s.age)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


c = Chain()
print(c.status.user.timeline.list)
