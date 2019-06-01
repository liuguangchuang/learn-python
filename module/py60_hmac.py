# -*- coding: utf-8 -*-
# Time: 2019/6/1 22:18
# Author: laugc
# Email: hahalgc@gmail.com
# File: py60_hmac.py

import hmac

"""
hmac 算法: Keyed-Hashing for Message Authentication
它通过一个标准算法，在计算哈希的过程中，把 key 混入计算过程中
"""

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用 h.update(msg)
print(h.hexdigest())
