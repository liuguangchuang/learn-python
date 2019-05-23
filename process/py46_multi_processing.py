# -*- coding: utf-8 -*-
# Time: 2019/5/21 23:10
# Author: laugc
# Email: hahalgc@gmail.com
# File: py46_multi_processing.py

"""
进程池
"""

from multiprocessing import Pool
import os
import time
import random
import subprocess


def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s run %0.2f seconds ' % (name, (end - start)))


if __name__ == '__main__':
    print('parent process %s ' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('waiting for all subprocess done...')
    p.close()
    p.join()
    print('all subprocess done')
