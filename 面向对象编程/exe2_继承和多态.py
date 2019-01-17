#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'


class Animal(object):
    def run(self):
        print('Animal is running...')


# () 括号里面的东西表示继承

# 某一个区域什么也不做就执行 pass
# class Cat(Animal):
#     pass
class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


# 理解多态
def run_twice(Animal):
    Animal.run()
    Animal.run()


dog = Dog()
cat = Cat()
dog.run()
cat.run()

# 判断是否是某一个类的实例，使用isinstance
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

run_twice(Animal())
run_twice(Dog())
