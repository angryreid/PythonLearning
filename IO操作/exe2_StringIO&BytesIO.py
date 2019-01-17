#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

# 在内存中进行文件读写
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())#getvalue()方法用于获得写入后的str。

f2 = StringIO("hello\nhi\ngoodbey")
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

# 如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO
f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())