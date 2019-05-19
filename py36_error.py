# -*- coding: utf-8 -*-
# Time: 2019/5/19 15:57
# Author: laugc
# Email: hahalgc@gmail.com
# File: py36_error.py

"""
错误处理
"""

# 所有的错误类型都继承自 BaseException
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
# 当没有错误发生时，会自动执行 else 语句
else:
    print('no error!')
finally:
    print('finally...')
print('end')


# raise 语句抛出错误
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()
