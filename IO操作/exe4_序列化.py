#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# 序列化
# 我们把变量从内存中变成可存储的，或者可传输的过程称之为序列化
# picking
# 序列化之后，可以把序列化的内容写入磁盘，或者通过网络传输到网络的别的机器上面

# 变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

import pickle

d = dict(name="oooh", age=20, score=0)

print(pickle.dumps(d))  # pickle.dumps()方法把任意对象序列化成一个bytes

# pickle.dumps()方法把任意对象序列化成一个bytes
# wb 写入二进制
import shutil

f = open('C:/Users/admin/Desktop/py.txt', 'wb')
pickle.dump(d, f)  # pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()

f2 = open('C:/Users/admin/Desktop/py.txt', 'rb')
d2 = pickle.load(f2)
f2.close()
print(d)

import json

print(json.dumps(d))#dumps()方法返回一个str

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# 要把JSON反序列化为Python对象
print(json.loads(json_str))
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
