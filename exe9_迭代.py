#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# iteration

s = '123456789'
# for ch in s:
#     print(ch)

# 字典
d = {'name':'ddd','age':34,'sex':'woman'}

for key in d:
    print(key)

print('----')
for val in d.values():
    print(val)
print(d.items())
for k,v in d.items():
    print(k,'--',v)

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)

# def findMinAndMax(L):
#     if len(L) == 0:
#         return (None,None)
#     min = L[0]
#     max = L[0]
#     for i in L:
#         if min >= i:
#             min = i
#         if max <= i:
#             max = i
#     return (min,max)

def findMinAndMax(L):
    if L == []:
        return (None, None)
    sL = sorted(L)
    minl = sL[0]
    maxl = sL[-1]
    return (minl, maxl)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')