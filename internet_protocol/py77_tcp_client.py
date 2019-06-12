# -*- coding: utf-8 -*-
# Time: 2019/6/12 21:50
# Author: laugc
# Email: hahalgc@gmail.com
# File: py77_tcp_client.py

import socket

"""
tcp 编程
Socket 是网络编程的一个抽象概念
通常用一个 Socket 表示「打开了一个网络链接」，而打开一个 Socket 需要知道目标计算机的 IP 地址和端口号，再指定协议类型即可
"""

# 创建 socket
# AF_INET 指定使用 IPv4 协议，AF_INET6 指定为 IPv6
# SOCK_STREAM指 定使用面向流的 TCP 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# 注意参数是一个 tuple
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收 1k 字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
print(data)

# 接收到的数据包括 HTTP 头和网页本身，把 HTTP 头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)

# 关闭连接
s.close()
