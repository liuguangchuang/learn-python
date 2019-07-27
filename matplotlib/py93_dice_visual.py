# -*- coding: utf-8 -*-
# Time: 2019/7/7 21:58
# Author: laugc
# Email: hahalgc@gmail.com
# File: py93_dice_visual.py

import pygal
from py92_dice import Dice

"""
投骰子
"""

dice = Dice()
# 10 面骰子
dice2 = Dice()
results = []
for roll_num in range(50000):
    result = dice.roll() + dice2.roll()
    results.append(result)

print(results)

frequencies = []
max_result = dice.num_sides + dice2.num_sides
# 分析结果
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 可视化结果
hist = pygal.Bar()

hist.title = 'result of rolling dice.'
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'result'
hist.y_title = 'frequency of result'
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
