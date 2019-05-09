# -*- coding: utf-8 -*-
# @Time : 2019/5/9 22:34
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py5_if.py

"""
if 条件判断
"""

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
# ============
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
# ============
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# ============
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
