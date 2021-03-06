# -*- coding: utf-8 -*-
# Time: 2019/5/21 22:46
# Author: laugc
# Email: hahalgc@gmail.com
# File: py45_multi_processing.py

"""
多进程
"""

import os
from multiprocessing import Process

print('Process (%s) start...' % os.getpid())


# Only works on Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
#     print('I am child thread_processing (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child thread_processing (%s).' % (os.getpid(), pid))

# 子进程执行的代码
def run_process(name):
    print('run child thread_processing %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent thread_processing %s ' % os.getpid())
    p = Process(target=run_process, args=('test',))
    print('child thread_processing start')
    p.start()
    p.join()
    print('child thread_processing end')
