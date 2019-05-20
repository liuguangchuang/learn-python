# -*- coding: utf-8 -*-
# Time: 2019/5/19 22:42
# Author: laugc
# Email: hahalgc@gmail.com
# File: py41_stringio_bytesio.py

"""
StringIO 和 BytesIO
"""

from io import StringIO
from io import BytesIO

# StringIO 是指在内存中读写 str
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world'))
# getvalue() 方法用于获得写入后的 str
print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

print("============")
# BytesIO 操作二进制数据，在内存中读写 bytes
f2 = BytesIO()
f2.write('中文'.encode('utf-8'))

print(f2.getvalue())

data = '啊，哈，嘻，呀，嘿。'.encode('utf-8')
f3 = BytesIO(data)
print(f3.read())
