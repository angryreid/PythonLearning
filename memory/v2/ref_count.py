"""
ref_count - PythonLearning
Author: nick
Date: 2024/12/28
Time: 21:23

Description: 

"""
from sys import getrefcount


def main():
    n = 1
    # del n
    print(getrefcount(n))
    x = 'abc'
    y = 'abc'
    print(id(x))  # 4343262576
    print(id(y))  # 4343262576


if __name__ == "__main__":
    main()
