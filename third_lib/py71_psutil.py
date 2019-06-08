# -*- coding: utf-8 -*-
# Time: 2019/6/8 9:35
# Author: laugc
# Email: hahalgc@gmail.com
# File: py71_psutil.py

import psutil

"""
用于运维
psutil: process and system utilities
"""

# cpu 逻辑数量
print(psutil.cpu_count())

# cpu 物理核心
print(psutil.cpu_count(logical=False))

# 统计 CPU 的用户、系统、空闲时间
print(psutil.cpu_times())

# 实现类似 top 命令的 CPU 使用率，每秒刷新一次，累计 2 次
for x in range(2):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
# 获取磁盘分区信息
print(psutil.disk_partitions())
# 获取磁盘使用情况
print(psutil.disk_usage('/'))
# 获取磁盘 io
print(psutil.disk_io_counters())
print("=========================")

# 获取网络信息
# 获取网络读写字节/包的数量
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())
# 要获取当前网络连接信息
print(psutil.net_connections())

