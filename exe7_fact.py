#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'


# 递归函数

def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


print(fact(5))


# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化
def hano(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        hano(n - 1, a, c, b)
        hano(1, a, b, c)
        hano(n - 1, b, a, c)


hano(5, 'A', 'B', 'C')
