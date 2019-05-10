# -*- coding: utf-8 -*-
# @Time : 2019/5/10 22:08
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py10_func_3.py

"""
函数参数
"""


# 计算 x 的 n 次方，n=2 默认参数，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# None 不变对象
# 默认参数必须指向不变对象
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


# 「*numbers」 可变参数，可传入 0 个或任意个参数，在函数调用时
# 可变参数自动组装为一个 tuple，(1,2,3)
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
# list
nums = [1, 2, 3]
print(calc(*nums))


# 「**kw」关键字参数，在函数调用时，关键字参数在函数内部自动组装为一个 dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Bob', 35, city='Beijing')
person('Adam', 45, gender='male', job='engineering')
extra = {'city': 'beijing', 'job': 'engineering'}
person('Jack', 24, **extra)


# 命名关键字参数，命名关键字参数必须传入参数名
# * 后面的参数被视为命名关键字参数
def person_1(name, age, *, city, job):
    print(name, age, city, job)


person_1('Lau', 15, job='IT', city='guangzhou')


# city 和 job 也是命名关键字参数
def person_2(name, age, *args, city, job):
    print(name, age, args, city, job)
