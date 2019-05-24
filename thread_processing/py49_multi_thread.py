# -*- coding: utf-8 -*-
# Time: 2019/5/23 22:18
# Author: laugc
# Email: hahalgc@gmail.com
# File: py49_multi_thread.py

"""
多线程
一个进程至少有一个线程
"""

import time
import threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
