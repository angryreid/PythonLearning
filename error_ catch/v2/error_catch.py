"""
error_catch - PythonLearning
Author: nick
Date: 2024/11/23
Time: 21:30

Description: 

"""


def main():
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print("Error:", e)
    finally:
        print('finally...')


if __name__ == "__main__":
    main()
