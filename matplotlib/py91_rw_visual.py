# -*- coding: utf-8 -*-
# Time: 2019/7/7 16:58
# Author: laugc
# Email: hahalgc@gmail.com
# File: py91_rw_visual.py

import matplotlib.pyplot as plt
from py90_random_walk import RandomWalk

"""
绘制随机漫步图
"""

while True:
    # 创建 RandomWalk 实例
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 起点和终点
    plt.scatter(0, 0, c='yellow', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('make another random walk? (y/n): ')
    if keep_running == 'n':
        break
