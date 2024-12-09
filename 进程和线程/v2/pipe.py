"""
pipe - PythonLearning
Author: nick
Date: 2024/12/9
Time: 21:10

Description: 

"""

import os
import time
from multiprocessing import Pool, Pipe


def product(name: str, send_pipe: Pipe) -> None:
    print(f'Sub process {name} is running!, pid is {os.getpid()}')
    for p in ['Apple', 'Banana', 'Cherry']:
        time.sleep(2)
        send_pipe.send(p)
        print(f'Product {p} is ready')
    send_pipe.send('SOLD_OUT')
    time.sleep(2)
    print(f'{name} process end!, pid is {os.getpid()}')


def consumer(name: str, recv_pipe: Pipe):
    print(f'Sub process {name} is running!, pid is {os.getpid()}')
    while True:
        time.sleep(1)
        product_info = recv_pipe.recv()
        if product_info != 'SOLD_OUT':
            print(f'Product {product_info} is sold.')
        else:
            break


def main():
    main_pic = os.getpid()
    print(f'Main process id: {main_pic}')
    send_pipe, recv_pipe = Pipe()
    pool = Pool(2)
    pool.apply_async(product, ('Product', send_pipe,))
    pool.apply_async(consumer, ('Consumer', recv_pipe,))
    pool.close()
    pool.join()
    print(f'Main process {main_pic} end!')


if __name__ == "__main__":
    main()
