# -*- coding: utf-8 -*-
# Time: 2019/5/20 22:40
# Author: laugc
# Email: hahalgc@gmail.com
# File: py43_serialize.py

"""
序列化：把变量从内存中变成可存储或传输的过程称之为序列化，pickling
反序列化：把变量内容从序列化的对象重新读到内存里称之为反序列化，unpickling
"""

import pickle

d = dict(name='Bob', age=20, score=88)

# pickle.dumps() 方法把任意对象序列化成一个 bytes
print(pickle.dumps(d))

# pickle.dump() 直接把对象序列化后写入一个 file-like Object
f = open('io.txt', 'wb')
# 乱码
data = pickle.dumps(d)
print(data)

d1 = pickle.loads(data)
f.close()
print(d1)
