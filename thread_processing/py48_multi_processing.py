# -*- coding: utf-8 -*-
# Time: 2019/5/23 22:07
# Author: laugc
# Email: hahalgc@gmail.com
# File: py48_multi_processing.py

"""
进程间通信
"""

from multiprocessing import Process, Queue
import os
import time
import random


# 写数据进程
def write(q):
    print('thread_processing to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程
def read(q):
    print('thread_processing to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建 queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程，写入
    pw.start()
    # 启动子进程，读取
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环，只能强制结束
    pr.terminate()
