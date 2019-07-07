# -*- coding: utf-8 -*-
# Time: 2019/7/7 21:55
# Author: laugc
# Email: hahalgc@gmail.com
# File: py92_dice.py

from random import randint

"""
骰子
"""


class Dice():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回位于 1 与骰子面数之间的随机值"""
        return randint(1, self.num_sides)
