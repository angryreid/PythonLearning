#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。