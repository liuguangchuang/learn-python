# -*- coding: utf-8 -*-
# Time: 2019/5/24 21:51
# Author: laugc
# Email: hahalgc@gmail.com
# File: py51_threadlocal.py

import threading

# 创建全局 ThreadLocal 对象
local_school = threading.local()


def process_student():
    # 获取当前关联的 student
    std = local_school.student
    print('hello %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定 ThreadLocal 的 student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('lau',), name='thread-a')
t2 = threading.Thread(target=process_thread, args=('li',), name='thread-b')
t1.start()
t2.start()
t1.join()
t2.join()
