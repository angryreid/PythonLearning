#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
from functools import reduce


def fn(x, y):
    return x * 10 + y


def charToNum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(charToNum, '1234567')))

# 一个完整的方法
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('988347847'))


# 生成器 无线序列 返回素数
def _odd_iter():
    n = 1
    while 1:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()
    while 1:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it) #构造新的序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break
