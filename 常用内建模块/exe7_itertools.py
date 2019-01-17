#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

# itertools提供了非常有用的用于操作迭代对象的函数

import itertools

# 无限的迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ASD')
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns = itertools.repeat('o',8)
# for n in ns:
#     print(n)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来
for c in itertools.chain('ABC','XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
    print(key,list(group))

from functools import reduce
# 计算圆周率
def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x <= 2*N-1, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    c = itertools.cycle([1, -1])
    ns = map(lambda x: (4 / x) * next(c), ns)
    # step 4: 求和:
    sums = reduce(lambda x, y: x+y, ns)
    return sums
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')