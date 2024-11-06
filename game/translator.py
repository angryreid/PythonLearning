"""
translator - PythonLearning
Author: nick
Date: 2024/11/5
Time: 22:16

Description: 

"""
import time


def main():
    trans_dict = {'baby': 'bebe', 'university': 'universidad', 'ten': 'diez', 'honey': 'Mi amor'}
    sec = int(input('Plz input the translation waiting time:'))
    for key in trans_dict:
        print(f'{key}')
        time.sleep(sec)
        print(f'{trans_dict[key]}')
        time.sleep(sec)

    for k, v in trans_dict.items():
        print(f'{k}:', end=' ')
        time.sleep(sec)
        print(f'{v}')
        time.sleep(sec)


def fib(n: int) -> int:
    """
    This function is to return the fib of n
    :param n:
    :return:
    """
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    main()
    print(fib(4))
