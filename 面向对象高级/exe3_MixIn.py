#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# 可以多继承
# 一般情况下，主线都是单一继承的，但是中途有可能会增加进来，所以就是MixIn

class Animal(object):
    pass

class Dog(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print("run")
class Cat(Animal,RunnableMixIn):
    pass
