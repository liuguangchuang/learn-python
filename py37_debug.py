# -*- coding: utf-8 -*-
# Time: 2019/5/19 16:22
# Author: laugc
# Email: hahalgc@gmail.com
# File: py37_debug.py

"""
调试
"""

import logging
import pdb


# print 输出调试
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


def main():
    foo('1')


main()


# 断言
# 断言的开关 -O，是英文大写字母 O，不是数字 0
# 关闭后，你可以把所有的 assert 语句当成 pass 来看
def foo1(s):
    n = int(s)
    # 如果断言失败，assert 语句本身就会抛出 AssertionError
    assert n != 0, 'n is zero!'
    return 10 / n


def main1():
    foo1('1')


main1()

# logging 不会抛出错误，而且可以输出到文件
# logging 有 debug，info，warning，error等几个级别。
# 当指定 level=INFO 时，logging.debug 就不起作用了
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / 1)

# pdb.set_trace()
s1 = '0'
n = int(s1)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)
