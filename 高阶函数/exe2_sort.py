#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# 排序算法
print(sorted([-23, -56, -56, 0, 34, 1, 3]))

# 接受一个key值来进行自定义排序

print(sorted([-23, -56, -56, 0, 34, 1, 3], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    if t[0]:
        return t[0].lower
L2 = sorted(L,key=by_name)
print(L2)
