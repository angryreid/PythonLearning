"""
process - PythonLearning
Author: nick
Date: 2024/12/9
Time: 19:54

Description:

"""
import os
from multiprocessing import Pool
import time


def sub_process_run(name):
    print(f'Sub process {name} is running!, pid is {os.getpid()}')
    time.sleep(2)

    print(f'Sub process {name} end!, pid is {os.getpid()}')


def main():
    # pass  # TODO: Implement your code here
    print(f'Main process id: {os.getpid()}')

    pl = Pool(5)
    for i in range(10):
        sub_process_name = f'subProcess_{i}'
        pl.apply_async(sub_process_run, args=(sub_process_name,))
    pl.close()
    pl.join()
    print(f'Main process end!')


if __name__ == "__main__":
    main()
