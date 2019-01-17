#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# help(abs) abs返回参数的绝对值 help 查看参数的使用方法
# max
print(max(1, 2, 3, 4, 5))
# min
print(min(1, 2, 3, 4, 5))


# 数据类型转换
# int
# float
# str
# bool

def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-100))


# pass : do nothing

def love():
    pass


print(love())

# isinstance 判断类型
print(isinstance([], list))


def abs_up(x):
    if isinstance(x, (int, float)):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise TypeError("wrong type")


# print(abs_up('123'))
# print(abs_up(12.45))
import math


def move(x, y, step, angle=0):
    newX = x + step * math.cos(angle)
    newY = y + step * math.sin(angle)
    return newX, newY


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)
print(isinstance((), tuple))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 2))
print(power(2))


# 只有与默认参数不符的学生才需要提供额外的信息：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())
print(add_end())


# 可变参数 *
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4, 5))


# 关键字参数 **
def person(name, age, **city):
    print({"name": name, "age": age, "other": city})


print(person('michael', 30))


# 如果要限制传入的参数名称，只接收特定的参数
# 使用 *，
def person2(name, age, *, city, job):
    print(name, age, city, job)
# 命名关键字参数必须传入参数名
print(person2("axin",12,city='suzhou',job='it'))
def product(*numbers):
    s = 1
    if not numbers:
        raise TypeError("error")
    for num in numbers:
        s = s*num
    return s
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')