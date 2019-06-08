# -*- coding: utf-8 -*-
# Time: 2019/6/8 13:24
# Author: laugc
# Email: hahalgc@gmail.com
# File: py75_turtle_2.py

from turtle import *

t = Turtle()


def drawStar(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    # 五角星方向
    t.seth(0)
    for i in range(5):
        # 五角星大小
        t.fd(40)
        t.rt(144)


for x in range(0, 255, 50):
    drawStar(x, 0)

done()
