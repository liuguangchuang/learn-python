# -*- coding: utf-8 -*-
# Time: 2019/6/1 20:34
# Author: laugc
# Email: hahalgc@gmail.com
# File: py56_collections.py

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os
import argparse

"""
collections 是 Python 内建的一个集合模块，提供了许多有用的集合类
"""

# namedtuple 是一个函数，它用来创建一个自定义的 tuple 对象，
# 并且规定了 tuple 元素的个数，并可以用属性而不是索引来引用 tuple 的某个元素
# 创建的 Point 对象是 tuple 的一种子类
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p, Point))
# 圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key'] = 'abc'
print(dd['key'])
# 不存在 key 返回 N/A
print(dd['key1'])

# ===============================================================
# OrderedDict 的 Key 会按照插入的顺序排列，不是 Key 本身排序
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od1 = OrderedDict()
od1['z'] = 1
od1['y'] = 2
od1['x'] = 3
print(od1)
print("==============================")


# OrderedDict 可以实现一个 FIFO（先进先出）的 dict，当容量超出限制时，先删除最早添加的 Key
class LastUpdateOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove: ', last)
        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ===============================================================
# ChainMap 可以把一组 dict 串起来并组成一个逻辑上的 dict
# ChainMap 本身也是一个 dict，但是查找的时候，会按照顺序在内部的 dict 依次查找
# 构造默认参数
defaults = {
    'color': 'red',
    'user': 'laugc'
    }

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# 组合成 ChainMap，优先级：command_line_args > os.environ > defaults
combine = ChainMap(command_line_args, os.environ, defaults)
print('color=%s' % combine['color'])
print('user=%s' % combine['user'])

# Counter 是一个简单的计数器
counter = Counter()
for ch in 'programming':
    counter[ch] = counter[ch] + 1
print(counter)
