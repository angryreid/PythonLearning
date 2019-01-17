#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

class Student(object):
    pass
# 创建一个实例，并绑定方法
s = Student()
s.name = 'fengyoujin'
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)
# 但是仅对当前的实例有用，别的实例是没有用的
# 可以对所有的实例生效，需要对类本身进行绑定
s2 = Student()
# print(s2.age)
def set_score(self,score):
    self.score = score
Student.set_score = set_score

s.set_score(0)
s2.set_score(-1)
print(s.score)
print(s2.score)

# 限制属性的使用，只允许操作允许修改的属性
class Animal(object):
    __slots__ = ('name','age')

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的