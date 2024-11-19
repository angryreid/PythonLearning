"""
mutilple-extend - PythonLearning
Author: nick
Date: 2024/11/18
Time: 22:38

Description: 

"""


class Ball:
    __price = ''

    def __init__(self, name, *args, **kwargs):
        self.name = name
        print('Ball init...')


class TableTennis(Ball):
    def __init__(self, name, size, shape, *args, **kwargs):
        self.size = size
        self.shape = shape
        super().__init__(name, size, *args, **kwargs)
        print('TableTennis init...')


class BasketBall(Ball):
    def __init__(self, name, size, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.size = size
        print('BasketBall init...')


class BasketTableTennis(TableTennis, BasketBall):
    def __init__(self, name, size, shape, *args, **kwargs):
        super().__init__(name, size, shape, *args, **kwargs)
        print('BasketTableTennis init...')


def main():
    # Even this is multiple extending, but still as order
    # (<class '__main__.BasketTableTennis'>, <class '__main__.TableTennis'>, <class '__main__.BasketBall'>, <class '__main__.Ball'>, <class 'object'>)
    btt = BasketTableTennis(name='btt', size='small', shape='circle')
    # print(btt.__price)
    # print(btt in Ball) # not working
    print(isinstance(btt, Ball))
    print(isinstance(btt, BasketBall))
    print(isinstance(btt, TableTennis))
    print(BasketTableTennis.__mro__)


if __name__ == "__main__":
    main()
