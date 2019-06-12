# -*- coding: utf-8 -*-
# Time: 2019/6/12 22:11
# Author: laugc
# Email: hahalgc@gmail.com
# File: py78_tcp_server_1.py

import socket
import threading
import time

"""
tcp 编程
Socket 是网络编程的一个抽象概念
通常用一个 Socket 表示「打开了一个网络链接」，而打开一个 Socket 需要知道目标计算机的 IP 地址和端口号，再指定协议类型即可
"""

# 创建一个基于 IPv4 和 TCP 协议的 Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))
# 参数表示等待连接的最大数量
s.listen(5)
print('waiting for connecting')


def tcp_link(sock, address):
    print('accept new connection from %s: %s...' % address)
    sock.send(b'welcome.')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send('hello, %s.' % data.decode('utf-8')).encode('utf-8')
    sock.close()
    print('connection from %s: %s closed' % address)


# accept() 会等待并返回一个客户端的连接
while True:
    # 接收一个新连接
    sock, address = s.accept()
    # 创建新线程处理 tcp 连接
    t = threading.Thread(target=tcp_link, args=(sock, address))
    t.start()
