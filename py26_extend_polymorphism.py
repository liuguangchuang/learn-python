# -*- coding: utf-8 -*-
# Time: 2019/5/14 22:07
# Author: laugc
# Email: hahalgc@gmail.com
# File: py26_extend_polymorphism.py

"""
继承和多态
"""


# 继承自 object
class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承自 Animal
class Dog(Animal):
    def run(self):
        print('dog is running...')

    def eat(self):
        print('dog eating meat...')


# 继承自 Animal
class Cat(Animal):
    def run(self):
        print('cat is running...')

    def eat(self):
        print('cat eating meat...')


class Tortoise(Animal):
    def run(self):
        print('tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 判断一个变量是否是某个类型用 isinstance()
print(isinstance(dog, Animal))
print(isinstance(cat, Dog))

run_twice(Animal())
