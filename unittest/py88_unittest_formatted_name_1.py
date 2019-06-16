# -*- coding: utf-8 -*-
# Time: 2019/6/16 22:33
# Author: laugc
# Email: hahalgc@gmail.com
# File: py88_unittest_formatted_name_1.py

"""

"""

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
