# -*- coding: utf-8 -*-
# Time: 2019/6/1 22:00
# Author: laugc
# Email: hahalgc@gmail.com
# File: py59_hashlib.py

import hashlib

"""
hashlib 提供了常见的摘要算法
摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用 16 进制的字符串表示）
"""

# 摘要算法是 md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 摘要算法是 SHA1
# 比 SHA1 更安全的算法是 SHA256 和 SHA512
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
