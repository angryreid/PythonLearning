"""
iterator - PythonLearning
Author: nick
Date: 2024/12/18
Time: 21:22

Description: 

"""
from collections.abc import Iterator, Iterable


class MyIterator(object):
    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == 2:
            self.num += 1
            return 2
        else:
            while True:
                for i in range(2, self.num):
                    if self.num % i == 0:
                        self.num += 1
                        break
                    # elif self.num - 1 == i:
                    #     self.num += 1
                    #     return self.num - 1
                else:
                    self.num += 1
                    return self.num - 1


def main():
    it = MyIterator()
    print(isinstance(it, Iterable))
    print(isinstance(it, Iterator))
    itr = iter(it)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))


if __name__ == "__main__":
    main()
