"""
decorator - PythonLearning
Author: nick
Date: 2024/12/26
Time: 18:20

Description: 

"""
import time
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} decorator executed.')
        return func(*args, **kwargs)

    return wrapper


@log
def task():
    time.sleep(1)
    print('task executed.')


def main():
    task()
    print(task.__name__)


if __name__ == "__main__":
    main()
