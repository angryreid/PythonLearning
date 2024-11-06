#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

f = open('C:/Users/admin/Desktop/ads.txt', 'r', encoding='utf-8')

print(f.read())

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# except IOError as e:
#     print(e)
# finally:
#     if f:
#         f.close()
#
# with open('/path/to/file', 'r') as f:
#     print(f.read())
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用
print(f.readline())
f.close()

# 要读取二进制文件，图片，视频，用‘rb’模式打开

png = open('C:/Users/admin/Desktop/fan.png', 'rb')

print(png.read())
png.close()

#  f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

f2 = open('C:/Users/admin/Desktop/ads.txt', 'w')
f2.write('hello ooohenenen')
_f2 = open('C:/Users/admin/Desktop/ads.txt', 'r', encoding='')
print(_f2.read())

# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')
