#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# map 接收两个参数，一个是函数，一个是Iterable
L = [1,2,3,4,5]

def f(x):
    return x*x
L2 = map(f,L)
# 使用list方法展示map
print(list(L2))

# 快速将数组元素转换为字符串
# str

# reduce
# 把一个函数作用在一个序列上，reduce，把结果继续和序列的下一个元素做累计运算

R = [9,8,7,6,5,4,3,2,1]
def add(x,y):
    return x + y
from functools import reduce
print(reduce(add,R))

# 把一个序列变换成一个整数
def fn(x,y):
    return x*10 + y
num = [1,2,3,4,5]
print(reduce(fn,num))
