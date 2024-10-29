#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

if 1 > 2:
    print(True)
elif 1 == 1:
    print(True)
else:
    print(False)

# and or not
# None 代表一个特殊的空值
a = 123
print(a)
a = 'asd'
print(a)
#
b = a
a = 'sdfsdfsdf'
print(b)

print('到合肥京东方活动经费')

print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u56fd')
# 转字节
print('ABC'.encode('ascii'))
print('中国'.encode('utf-8'))
# 转字符
print(b'abc'.decode('ascii'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8', errors='ignore'))
# length
print(len('asdf'))
print(len('中国'))
