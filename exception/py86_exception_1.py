# -*- coding: utf-8 -*-
# Time: 2019/6/16 22:00
# Author: laugc
# Email: hahalgc@gmail.com
# File: py86_exception_1.py

"""
异常处理
"""

try:
    answer = 5 / 0
    print(answer)
except ZeroDivisionError:
    print('除 0 异常。')
else:
    # 如果不出异常，以也会执行
    print(answer)
