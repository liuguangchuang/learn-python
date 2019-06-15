# -*- coding: utf-8 -*-
# Time: 2019/6/13 22:45
# Author: laugc
# Email: hahalgc@gmail.com
# File: py82_sqlite_1.py

import sqlite3

"""
SQLite 数据库
"""

# 连接到 SQLite 数据库
# 数据库文件是 test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')

# 创建 Cursor
cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values(\'1\',\'laugc\')')

print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()
