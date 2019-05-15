# -*- coding: utf-8 -*-
# Time: 2019/5/15 22:39
# Author: laugc
# Email: hahalgc@gmail.com
# File: py31_multi_extend.py

"""
多重继承
"""


class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class RunnableMixIn(object):
    def run(self):
        print('running...')


class FlyableMixIn(object):
    def fly(self):
        print('flying...')


# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich 继承自 Bird。但是，如果需要「混入」额外的功能，
# 通过多重继承就可以实现，比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。这种设计通常称之为 MixIn
# Runnable 和 Flyable 改为 RunnableMixIn 和 FlyableMixIn
class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass
