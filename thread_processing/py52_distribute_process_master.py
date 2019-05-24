# -*- coding: utf-8 -*-
# Time: 2019/5/24 22:45
# Author: laugc
# Email: hahalgc@gmail.com
# File: py52_distribute_process_master.py

"""
分布式进程
主进程
"""

import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


# 从 BaseManager 继承的 QueueManager
class QueueManager(BaseManager):
    pass


# 把 queue 都注册到网络上，callable 参数关联了 Queue 对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定 5000 端口，设置验证码 abc
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动 queue
manager.start()
# t获得通过网络访问的 queue 对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 任务
for i in range(10):
    n = random.randint(0, 10000)
    print('put task %d...' % n)
    task.put(n)

# 从 result 队列获取结果
print('try get result')
for i in range(10):
    r = result.get(timeout=10)
    print('result: %s' % r)

manager.shutdown()
print('master exit')
