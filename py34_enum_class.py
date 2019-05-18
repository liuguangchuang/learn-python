# -*- coding: utf-8 -*-
# Time: 2019/5/18 22:47
# Author: laugc
# Email: hahalgc@gmail.com
# File: py34_enum_class.py

"""
枚举类
"""

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# @unique 装饰器可以检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0  # Sun 的 value 被设定为 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue.value)
print(day1 == Weekday.Tue)
print(Weekday(1))
