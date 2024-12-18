"""
generator - PythonLearning
Author: nick
Date: 2024/12/18
Time: 21:43

Description: 

"""


def main():
    numbers = (x for x in range(10))
    for x in numbers:
        print(x)
        '''
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
        '''
    print(numbers)


if __name__ == "__main__":
    main()
