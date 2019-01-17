#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# list use
classmates = ['xiaoming','xiaomei']
print(classmates)
print(len(classmates))
print(classmates[0]+' '+classmates[1])
# print(classmates[2]) out od range
# add a item
classmates.append('xiaohong')
print(classmates)
# insert a item
classmates.insert(2,'xiaozhu')
print(classmates)
#delete a item
classmates.pop(len(classmates)-1)
print(classmates)
classmates[0] = 'xiaogou'
print(classmates)
classmates[2] = True
print(classmates)

# tuple
t = (1,2,3)
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])