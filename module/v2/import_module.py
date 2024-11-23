"""
import_module - PythonLearning
Author: nick
Date: 2024/11/23
Time: 20:32

Description: 

"""
from math import log2
from mutilple_extend import BasketTableTennis


def main():
    print(f'log2(8): {log2(8)}')
    btt = BasketTableTennis(name='btt', size='large', shape='parallelbox')
    print(btt)


if __name__ == "__main__":
    main()
