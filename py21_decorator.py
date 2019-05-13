# -*- coding: utf-8 -*-
# Time: 2019/5/13 21:49
# Author: laugc
# Email: hahalgc@gmail.com
# File: py21_decorator.py

"""
装饰器
"""

import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print(time.time())


now()

# 函数对象有一个 __name__ 属性，可以拿到函数名
print(now.__name__)
