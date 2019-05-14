# -*- coding: utf-8 -*-
# Time: 2019/5/14 21:54
# Author: laugc
# Email: hahalgc@gmail.com
# File: py25_restrict_visit.py

"""
访问限制
"""


class Student(object):
    def __init__(self, name, score):
        # 例的变量名如果以 __ 开头，表示私有
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


s = Student('laugc', 98)

# _name 可以访问，但视为私有变量

# 不能直接访问 __name 是因为 Python 解释器对外把 __name 变量改成了 _Student__name，
# 仍然可以通过 _Student__name 来访问 __name 变量
print(s._Student__name)

# 内部的 __name 变量已经被 Python 解释器自动改成了 _Student__name，而外部代码给 s 新增了一 个__name 变量
s.__name = 'new'
print(s.get_name())
