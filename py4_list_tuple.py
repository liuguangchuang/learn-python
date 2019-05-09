# -*- coding: utf-8 -*-
# @Time : 2019/5/9 21:04
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py4_list_tuple.py

"""
list 与 tuple
"""
# 定义 list，索引从 0 开始，list 是一种有序的集合，可修改
list1 = ['Cap', 'Thor', 'Bruce']
print(len(list1))
print(list1[0])

# -1 表示最后一个元素，-2 表示倒数最后第二个
print(list1[-1])

# 在末尾追加一个元素
list1.append('RDJ')

# 在指定位置添加一个元素
list1.insert(1, 'Rocky')

# pop() 删除 list 末尾的元素
list1.pop()
list1.pop(1)

# 替换
list1[0] = "lau"
print(list1)

list2 = ["lau", 123, True]
list3 = ["lau", 123, True, ['a', 'b', 'c']]
print(len(list3))

print("================================")

# 定义一个 tuple，tuple 一旦初始化就不能修改
people = ('Michael', 'Bob', 'Tracy')
print(people)

# 只有一个元素的 tuple 要加逗号 ,
t = (1,)
print(t)
# 以下非 tuple
t1 = (1)
print(t1)
# 假的可修改 tuple
t2 = ('a', 'b', ['A', 'B'])
