"""
file_operation - PythonLearning
Author: nick
Date: 2024/11/6
Time: 22:05

Description: 

"""


def main():
    file = open('../assets/sample.txt')
    print(file.read())
    file.close()


if __name__ == "__main__":
    main()
