"""
generator - PythonLearning
Author: nick
Date: 2024/12/18
Time: 21:43

Description: 

"""
from collections.abc import Iterator, Iterable


def expression_generator():
    numbers = (x for x in range(10) if x % 2 != 0)  # generator
    # numbers = [x for x in range(10)]  # list
    print(type(numbers))  # list
    print(isinstance(numbers, Iterable))  # True
    print(isinstance(numbers, Iterator))  # True
    print(hasattr(numbers, '__iter__'))
    print(hasattr(numbers, '__next__'))
    for x in numbers:
        print(x)
    print(numbers)


def yield_generator():
    yield 0
    yield 1
    yield 2
    yield 3


def generating_prime():
    num = 2
    yield 2
    while True:
        num += 1
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            yield num


if __name__ == "__main__":
    # expression_generator()
    #
    # for x in yield_generator():
    #     print(x)
    g = generating_prime()
    for i in range(10):
        print(next(g))
