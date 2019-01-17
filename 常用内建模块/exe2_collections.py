#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

# namedtuple
# tuple 表示一个不可变得集合
# 定义一个坐标点
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))  # 这是一个元组

# 定义一个圆什么的
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# list是线性存储，数据量较大时，插入和删除的效率低
# deque 是为了实现插入和删除的操作的双向列表，适用于队列和栈

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时候，引用的值不存在，就会抛出一个KeyError，如果希望值不存在时候，抛出一个默认值，就是用defaultddict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['name'] = 'oooh'
print(dd['dfdfd'])

# 使用dict时，Key是无序的，在对dict做迭代，可以使用OrderedDict
from collections import OrderedDict
ddd = dict([('a',1),('c',2),('b',3)])
print(ddd)
# Key会按照插入的顺序排列，不是Key本身排序：
orderDDD = OrderedDict([('a',4),('c',3),('b',7)])
print(orderDDD)

# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

# Counter
# 统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)
print(c['r'])