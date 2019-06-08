# -*- coding: utf-8 -*-
# Time: 2019/6/8 11:10
# Author: laugc
# Email: hahalgc@gmail.com
# File: py73_tkinter_2.py

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'haha'
        messagebox.showinfo('message', 'hello, %s' % name)


# 当用户点击按钮时，触发 hello()，通过 self.nameInput.get() 获得用户输入的文本后，
# 使用 tkMessageBox.showinfo() 可以弹出消息对话框

app = Application()
# 设置窗口标题
app.master.title('lau')
# 主消息循环
app.mainloop()
