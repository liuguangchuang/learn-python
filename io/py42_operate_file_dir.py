# -*- coding: utf-8 -*-
# Time: 2019/5/20 22:01
# Author: laugc
# Email: hahalgc@gmail.com
# File: py42_operate_file_dir.py

"""
操作文件和目录
"""

import os

# 操作系统类型，posix 说明系统是 Linux、Unix 或 Mac OS X，如果是 nt， Windows 系统
print(os.name)

# uname() 函数在 Windows 上不提供
# print(os.uname())

# 查看环境变量
print(os.environ)
print(os.environ.get('PATH'))

# 操作文件和目录
# 查看当前目录绝地路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录
d = os.path.join('D:\python_code\learn-python', 'dir')

# 创建一个目录
os.mkdir(d)

# 删除目录
os.rmdir(d)

# 拆分路径与文件名
print(os.path.split('D:\python_code\learn-python\py8_func_1.py'))

# 拆分后缀
print(os.path.splitext('D:\python_code\learn-python\py8_func_1.py'))

# 重命名，会将文件移动到当前目录下
# os.rename('../file/io.txt', 'io_1.txt')

# 删除文件
# os.remove('io_1.txt')

print("==========")
# 列出所有当前目录下所有的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出当前目录下所有 .py 文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
