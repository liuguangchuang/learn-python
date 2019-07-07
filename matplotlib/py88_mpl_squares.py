# -*- coding: utf-8 -*-
# Time: 2019/7/7 14:59
# Author: laugc
# Email: hahalgc@gmail.com
# File: py88_mpl_squares.py

import matplotlib.pyplot as plt

"""
折线图
"""

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图标标题，坐标加上标签
plt.title('square numbers', fontsize=14)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
