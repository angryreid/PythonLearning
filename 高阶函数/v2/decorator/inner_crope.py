"""
inner_crope - PythonLearning
Author: nick
Date: 2024/12/26
Time: 18:11

Description: 

"""


def outer(x):
    def inner(y):
        return x + y

    return inner


def main():
    print(outer(1)(2))


if __name__ == "__main__":
    main()
