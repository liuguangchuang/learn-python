# -*- coding: utf-8 -*-
# Time: 2019/6/13 23:02
# Author: laugc
# Email: hahalgc@gmail.com
# File: py83_sqlite_2.py

import sqlite3

"""
SQLite 数据库
"""

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
