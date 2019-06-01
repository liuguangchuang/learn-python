# -*- coding: utf-8 -*-
# Time: 2019/6/1 21:10
# Author: laugc
# Email: hahalgc@gmail.com
# File: py57_base64.py

import base64

"""
Base64 是一种用 64 个字符来表示任意二进制数据的方法
"""
# 如果要编码的二进制数据不是 3 的倍数，Base64 用 \x00 字节在末尾补足后
# 再在编码的末尾加上 1 个或 2 个 = 号，表示补了多少字节，解码的时候，会自动去掉
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# 由于标准的 Base64 编码后可能出现字符 + 和 /，在 URL 中就不能直接作为参数
# 所以又有一种 url safe 的 base64 编码，其实就是把字符 + 和 / 分别变成 - 和 _
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
