# -*- coding: utf-8 -*-
# Time: 2019/5/15 22:18
# Author: laugc
# Email: hahalgc@gmail.com
# File: py30_property.py

"""
使用 @property
"""


class Student(object):

    # 把一个 getter 方法变成属性，只需要加上 @property 就可以了
    @property
    def score(self):
        return self._score

    # 装饰器 @score.setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2000 - self._birth


s = Student()
# OK，实际转化为 s.set_score(60)
s.score = 45
# OK，实际转化为 s.get_score(60)
print(s.score)
s.score = 9999
