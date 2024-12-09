"""
process - PythonLearning
Author: nick
Date: 2024/12/9
Time: 19:54

Description: 

"""
import os
from multiprocessing import Process
import time


def sub_process_run(name):
    print(f'Sub process {name} is running!, pid is {os.getpid()}')
    time.sleep(1)


def main():
    # pass  # TODO: Implement your code here
    print(f'Main process id: {os.getpid()}')
    sub_process_name = 'subProcess_1'
    pcs = Process(
        target=sub_process_run,
        args=(sub_process_name,),
        name=sub_process_name
    )
    pcs.start()
    pcs.join()
    print(f'Sub process {sub_process_name} end!')


if __name__ == "__main__":
    main()
