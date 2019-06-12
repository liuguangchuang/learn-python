# -*- coding: utf-8 -*-
# Time: 2019/6/12 22:27
# Author: laugc
# Email: hahalgc@gmail.com
# File: py79_tcp_client_1.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接收消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Brad', b'Leo']:
    # 发送数据
    s.send(b'exit')
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
