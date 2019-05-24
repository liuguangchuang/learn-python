# -*- coding: utf-8 -*-
# Time: 2019/5/24 23:08
# Author: laugc
# Email: hahalgc@gmail.com
# File: py53_distribute_process_worker.py

"""
分布式进程
从进程
"""

import time
import sys
import queue
from multiprocessing.managers import BaseManager


# 创建类似的 QueueManager
class QueueManager(BaseManager):
    pass


# 由于这个 QueueManager 只从网络上获取 Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 连接至服务器，也就是运行 task_master 的机器
server_addr = '127.0.0.1'
print('connect to server %s...' % server_addr)
# 端口和验证码要与 master 设置的一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
m.connect()
# 获取 Queue 对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从 task 队列获取任务，并把结果写入 result 队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d*%d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

# 处理结果
print('worker exit...')
