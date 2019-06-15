# -*- coding: utf-8 -*-
# Time: 2019/5/19 22:14
# Author: laugc
# Email: hahalgc@gmail.com
# File: py40_read_write.py

"""
IO: 文件读写
"""

# 读文件
try:
    # 标示符 r 表示读
    f = open('D:\python_code\learn-python\io.txt', 'r')
    # read(size) 方法，每次最多读取 size 个字节的内容，readline() 可以每次读取一行内容
    # read() 会一次性读取文件的全部内容
    # print(f.read())
    for line in f.readlines():
        print(line.strip())  # 把末尾的 \n 删掉
finally:
    if f:
        f.close()

print("========")
# with 语句自动调用 close() 方法
with open('D:\python_code\learn-python\io.txt', 'r') as f1:
    print(f1.read())

# 图片、视频等等，用 rb 模式打开文件
f2 = open('D:\python_code\learn-python\Facebook.png', 'rb')
# 打印出十六进制表示的字节
# rstrip() 删除字符串末尾空行
print(f2.read().rstrip())

# 读取 utf-8 编码的文件，忽略错误
f3 = open('D:\python_code\learn-python\io.txt', 'r', encoding='utf-8', errors='ignore')
print(f3.read())

# 写文件
# w 覆盖文件全部内容，
# a 以追加 append 模式写入，不换行
f4 = open('D:\python_code\learn-python\io.txt', 'a')
f4.write('Hello, world!')
f4.close()

with open('D:\python_code\learn-python\io.txt', 'a') as f5:
    f5.write('Hello, world!')
