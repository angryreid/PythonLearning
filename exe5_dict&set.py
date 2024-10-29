#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# dic dictionary map [key,value]
score = {"foo": 100, "bar": 90, "foobar": 80}
print(score["foo"])

score["she"] = 88
print(score)

# print(score["he"]) error
print(score.get("he", -1))

# pop delete
score.pop("she")
print(score)

# set without same key,@param list \
s = set([1, 2, 3])
print(s)

ss = set([1, 2, 2, 3, 4, 2])
print(ss)

# remove key  delete
ss.remove(4)
print(ss)

# set 可以看成无序，无重复的两个元素，因此可以用来做交集，并集的操作
s1 = set([1, 2, 3, 4, 5])
s2 = set([2, 3, 4, 7, 8, 9])
s3 = s1 & s2
s4 = s1 | s2
print(s3)
print(s4)
# print(set([1,2,3,[2,3,4]])) 不能放入可变对象
print(set([1, 2, '1']))
