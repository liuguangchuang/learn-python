# -*- coding: utf-8 -*-
# Time: 2019/7/7 16:10
# Author: laugc
# Email: hahalgc@gmail.com
# File: py89_scatter_squares.py

import matplotlib.pyplot as plt

"""
散点图
"""

x_values = list(range(1, 1001))
# x ** 2 取平方
y_values = [x ** 2 for x in x_values]
# c 值越接近 1，颜色越浅
# plt.scatter(x_values, y_values, c=(0.5, 0, 0), edgecolors='none', s=10)
# 颜色渐变
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)
plt.title('square numbers', fontsize=14)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# 刻度大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

# 保存图片，第一个参数指文件名，第二个参数指剪掉空白区域
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()


