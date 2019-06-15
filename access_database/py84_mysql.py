# -*- coding: utf-8 -*-
# Time: 2019/6/13 23:00
# Author: laugc
# Email: hahalgc@gmail.com
# File: py84_mysql.py

import mysql.connector

"""
MySQL
"""

connect = mysql.connector.connect(user='root', password='123', database='ssm')
cursor = connect.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user(id, name) values(%s, %s)', ['1', 'laugc'])
print(cursor.rowcount)
connect.commit()
cursor.execute('select * from account')
values = cursor.fetchall()
print(values)

cursor.close()
connect.close()
