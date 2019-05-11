# -*- coding: utf-8 -*-
# @Time : 2019/5/11 15:09
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py13_iterate.py

"""
迭代
"""
# dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    # 加 end=' '，输出不换行
    print(key, end=' ')
print()

for ch in 'ABC':
    print(ch, end=' ')
print()

# enumerate 函数可以把一个 list 变成索引--元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, '-->', value)
