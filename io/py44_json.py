# -*- coding: utf-8 -*-
# Time: 2019/5/20 23:06
# Author: laugc
# Email: hahalgc@gmail.com
# File: py44_json.py

"""
json
"""

import json

d = dict(name='lau', age=12, score=85)
# 转为 json
print(json.dumps(d))

# json.dump() 存储数据至 .json
# json.load() 读取数据至内存

# 反序列化
json_str = '{"age":20,"score":55,"name":"lau"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
        }


# 可选参数 default 就是把任意一个对象变成一个可序列为 JSON 的对象
# Student 实例首先被 student2dict() 函数转换成 dict，然后再被顺利序列化为 JSON
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

# 通常 class 的实例都有一个 __dict__ 属性，它就是一个 dict，用来存储实例变量
# 把任意 class 实例变为 dict
print(json.dumps(s, default=lambda obj: obj.__dict__))


# json 转换为 Student 对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str1 = '{"age": 20, "score": 88, "name": "Bob"}'
# object_hook 函数负责把 dict 转换为 Student 实例
print(json.loads(json_str1, object_hook=dict2student))
