# -*- coding: utf-8 -*-
# Time: 2019/6/8 10:02
# Author: laugc
# Email: hahalgc@gmail.com
# File: py72_tkinter_1.py

from tkinter import *

"""
图形界面
"""


# Tkinter
# 第一步，导包
# 第二步是从 Frame 派生一个 Application 类，这是所有 Widget 的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='hello')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.pack()

# 在 GUI 中，每个 Button、Label、输入框等，都是一个 Widget。Frame 则是可以容纳其他 Widget 的 Widget，
# 所有的 Widget 组合起来就是一棵树。
# pack() 方法把 Widget 入到父容器中，并实现布局。pack() 是最简单的布局，grid() 可以实现更复杂的布局。
# 在 createWidgets() 方法中，创建一个 Label 和一个 Button，当 Button 被点击时，触发 self.quit() 使程序退出。

# 第三步，实例化 Application，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('hello lau')
# 主消息循环
app.mainloop()
