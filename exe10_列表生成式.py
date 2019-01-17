#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
list(range(1, 11))
print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 优化方式
nL = [x * x for x in range(1, 11)]
print(nL)

nL = [x * x for x in range(1, 11) if x % 2 == 0]
print(nL)

# 使用两层循环生成全排列
allSort = [m+n for m in 'abc' for n in "cde"]
print(allSort)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
