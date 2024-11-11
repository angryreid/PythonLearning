"""
file_operation - PythonLearning
Author: nick
Date: 2024/11/6
Time: 22:05

Description: 

"""


def read():
    file = open('../assets/sample.txt')
    print(file.read())
    file.close()


def write():
    file = open('../assets/write.txt', 'w')
    for i in range(10):
        file.write('Hello Nick\n')
    file.close()


if __name__ == "__main__":
    read()
    write()
