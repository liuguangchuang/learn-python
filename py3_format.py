# -*- coding: utf-8 -*-
# @Time : 2019/5/9 20:48
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py3_format.py

# ord() 函数获取字符的整数表示，chr() 函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

# 十六进制字符串
print('\u4e2d\u6587')

# 'ABC' 和 b'ABC'，前者是 string，bytes 的每个字符都只占用一个字节
# bytes 类型的数据用带 b 前缀的单引号或双引号表示
print(b'ABC')
print("=====")

# string 通过 encode() 方法可以编码为指定的 bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# decode() 方法把 bytes 变为 str
print(b'ABC'.decode('ascii'))

# errors='ignore' 忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len() 函数计算 string 包含多少个字符
print(len('ABC'))
# 1 个中文字符经过 UTF-8 编码后通常会占用 3 个字节，而 1 个英文字符只占用 1 个字节
print(len('中文'.encode('utf-8')))

# 格式化
# 有几个 %? 占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个 %?，括号可以省略
"""
%d	整数
%f	浮点数
%s	字符串，会把任何数据类型转换为字符串
%x	十六进制整数
%% 表示一个 %
"""
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# format() 格式化字符串
print('Hello, {0}, 成绩提升了 {1:.5f}%'.format('小明', 17.125))
