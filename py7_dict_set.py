# -*- coding: utf-8 -*-
# Time: 2019/5/10 21:25
# Author: laugc
# Email: hahalgc@gmail.com
# File: py7_dict_set.py

"""
dict 和 set
"""

# dict 字典，键--值（key--value）存储
# 定义字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 获取 value
print(d['Michael'])

# 添加
d['Adam'] = 67
d['Adam'] = 6777
print(d)

if 'Thomas' in d:
    print(['Thomas'])

# 若 key 不存在，则输出默认值
print(d.get('Thomas', -1))

# 删除
d.pop('Bob')

# set 集合，没有重复的元素
# 通过 list 创建集合
s = {1, 2, 3}
print(s)
# 和上面的集合相同
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 添加
s.add(4)

# 删除
s.remove(3)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()

