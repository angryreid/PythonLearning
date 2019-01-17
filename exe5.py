#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

names = ['apple','pear','banana']
for name in names:
    print(name)

sum = 0
for i in [1,2,3,4,5,6,7]:
    sum += i
print(sum)

# range()函数 生成一个整数序列
print(list(range(5)))
print((range(5)))

# 计算 0 - 100
sum = 0
for i in range(101):
    sum += i
print(sum)

nameArrs = ['foo','bar','foobar']
for name in nameArrs:
    print('hello:'+name)

# 过滤奇数
n = 0
while n<10:
    n=n+1
    if n%2 == 0:
        continue
    print(n)