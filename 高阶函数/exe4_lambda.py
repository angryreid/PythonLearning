#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# lambda 表达式 匿名函数
L = [1, 2, 3, 4, 5, 6]
print(list(L))
L2 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
print(L2)


# 实际上，lambda表达式就是
def f(x):
    return x * x


f2 = lambda x: x * x
print(f2(5))

L3 = list(filter(lambda x:x%2==1,range(1,20)))
print(L3)