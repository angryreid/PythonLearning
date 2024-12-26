"""
class_decorator - PythonLearning
Author: nick
Date: 2024/12/26
Time: 18:27

Description: 

"""
import time


class Log():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'{self.func.__name__} decorator executed.')
        return self.func(*args, **kwargs)


@Log
def task():
    time.sleep(1)
    print('task executed.')


def main():
    task()  # TODO: Implement your code here


if __name__ == "__main__":
    main()
