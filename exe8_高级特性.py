#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2
print(L)

# 列表 切片方法 slice
print(L[:3])  # L[0:3] 不包括后面的元素 可省略开头和省略结尾
print(L[-10:])  # 倒数十个数
print(L[:10:2])  # 每间隔2取一个数值
print(L[::5])  # 所有数字，每间隔5取一个
print(L)

# tuple 元祖切片方法也是一样
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[::2])
str = 'asdfjkl;'
print(str[::2])


def trim(L):
    start = 0
    end = len(L)
    i = 0
    for i in range(end):
        if L[start] == ' ':
            start = start + 1
        elif L[end - 1] == ' ':
            end = end - 1
    return L[start:end]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
