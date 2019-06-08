# -*- coding: utf-8 -*-
# Time: 2019/6/8 13:02
# Author: laugc
# Email: hahalgc@gmail.com
# File: py74_turtle_1.py

from turtle import *

"""
海龟绘图
"""

t = Turtle()

# 设置笔刷宽度
t.width(4)
# 前进
t.forward(200)
# 右转 90 度
t.right(90)

# 笔刷颜色
t.pencolor('red')
t.forward(100)
t.right(90)

t.pencolor('green')
t.forward(200)
t.right(90)

t.pencolor('blue')
t.forward(100)
t.right(90)

# 调用 done() 使得窗口等待被关闭，否则将立刻关闭窗口
done()
