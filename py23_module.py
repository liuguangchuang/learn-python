# -*- coding: utf-8 -*-
# Time: 2019/5/13 22:31
# Author: laugc
# Email: hahalgc@gmail.com
# File: py23_module.py

"""
模块
"""

import sys

# 类似 __xxx__ 这样的变量是特殊变量，可以被直接引用
__author__ = 'laugc'


def test():
    # argv 至少有一个元素，因为第一个参数永远是该 .py 文件的名称
    args = sys.argv
    if len(args) == 1:
        print('hello')
    elif len(args) == 2:
        print('yolo, %s' % args[1])
    else:
        print('oops')


if __name__ == '__main__':
    test()


# 类似 _xxx 和 __xxx 这样的函数或变量就是非公开的「private」，不应该被直接引用
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
