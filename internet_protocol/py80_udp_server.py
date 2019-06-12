# -*- coding: utf-8 -*-
# Time: 2019/6/12 22:40
# Author: laugc
# Email: hahalgc@gmail.com
# File: py80_udp_server.py

import socket

"""
UDP 则是面向无连接的协议
速度快，无须建立连接，不能保证数据是否能被接收
"""

# SOCK_DGRAM 指定了这个 Socket 的类型是 UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))

print('bind UDP on 9999')
# recvfrom() 返回数据和客户端的地址与端口，sendto() 可以把数据用 UDP 发给客户端
while True:
    # 接收数据
    data, address = s.recvfrom(1024)
    print('received from %s: %s.' % address)
    s.sendto(b'hello, %s' % data, address)
