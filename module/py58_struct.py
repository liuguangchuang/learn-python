# -*- coding: utf-8 -*-
# Time: 2019/6/1 21:43
# Author: laugc
# Email: hahalgc@gmail.com
# File: py58_struct.py

import struct

"""
struct
"""

# >I 的意思是：> 表示字节顺序是 big-endian，也就是网络序，
# I 表示 4 字节无符号整数。后面的参数个数要和处理指令一致
print(struct.pack('>I', 10240099))
# 根据 >IH 的说明，后面的 bytes 依次变为 I：4 字节无符号整数和 H：2 字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02' \
    b'\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# 两个字节： BM 表示 Windows 位图，BA 表示 OS/2 位图； 一个 4 字节整数：表示位图大小； 一个4字节整数：保留位，始终为 0；
# 一个 4 字节整数：实际图像的偏移量； 一个 4 字节整数：Header 的字节数； 一个4字节整数：图像宽度； 一个 4 字节整数：图像高度；
# 一个 2 字节整数：始终为 1； 一个 2 字节整数：颜色数
print(struct.unpack('<ccIIIIIIHH', s))
