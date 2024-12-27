"""
test - PythonLearning
Author: nick
Date: 2024/10/29
Time: 21:38

Description: 

"""
import re


def main():
    s = 'hello world, today is a new day'
    pattern = 'world'
    res = re.match(pattern, s)
    print(res)


if __name__ == "__main__":
    main()
