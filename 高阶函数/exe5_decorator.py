#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import functools


# 装饰
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2018-11-28")


f = now
print(f.__name__)
print(now.__name__)
# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# decorator 放置于函数的定义处
print(now())


def log_2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log_2('execute')
def now_2():
    print("2018")


print(now_2.__name__)
print(now_2())

# 每个函数执行之前，打印出该函数的执行时间
import time


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        cur_time = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        print('%s executed in %s' % (func.__name__, cur_time))
        return func(*args, **kw)

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
