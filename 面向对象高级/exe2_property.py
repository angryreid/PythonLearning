#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())


# s.set_score(9999)
# 内置的@property 装饰器就是把一个方法变成一个属性调用

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s3 = Student2()
s3.score = 66
print(s3.score)


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 1920 or value < 1024:
            raise ValueError('width is not fittable')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 1080 or value < 200:
            raise ValueError('height is not fittable')
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


# 测试:
s9 = Screen()
s9.width = 1024
s9.height = 768
print('resolution =', s9.resolution)
if s9.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

