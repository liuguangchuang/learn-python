# -*- coding: utf-8 -*-
# Time: 2019/6/13 23:22
# Author: laugc
# Email: hahalgc@gmail.com
# File: py85_sqlalchemy.py

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

"""
SQLAlchemy
"""

# 创建对象类
Base = declarative_base()


# 定义 user 对象
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 多的一方的 book 表是通过外键关联到 user 表的
    user_id = Column(String(20), ForeignKey('user.id'))


# 初始化连接
engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/ssm')
# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)

# 创建 session 对象
session = DBSession()
# 创建 user 对象
new_user = User(id='10', name='laugc')
# 添加到 session
session.add(new_user)
# 提交
session.commit()

session1 = DBSession()
# 创建 Query 查询，filter 是 where 条件，最后调用 one() 返回唯一行，如果调用 all() 则返回所有行
user = session1.query(User).filter(User.id == '5').all()
# 打印类型和对象的 name 属性
print('type: ', type(user))
# one()
# print('name: ', user.name)
# all()
for u in user:
    print(u.id, ': ', u.name)

session.close()
session1.close()
