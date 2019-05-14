# -*- coding: utf-8 -*-
# Time: 2019/5/14 22:21
# Author: laugc
# Email: hahalgc@gmail.com
# File: py27_get_obj_info.py

"""
获取对象信息
"""

import types

# 判断对象类型
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print("==================")
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print("==========================")
# 如果要获得一个对象的所有属性和方法，可以使用 dir() 函数
print(dir('ABC'))

# len() 会调用 __len__() 方法，可自定义该方法
print(len('str'))


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(dog.__len__())

# 判断对象是否有该属性，也可用于方法
print(hasattr(dog, 'x'))

# 设置属性
print(setattr(dog, 'y', 19))

# 获取属性
# 如果属性不存在，就返回默认值 404
print(getattr(dog, 'y', 404))
