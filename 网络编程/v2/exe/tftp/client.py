"""
client - PythonLearning
Author: nick
Date: 2024/12/3
Time: 20:23

Description: 

"""
import random
import struct
from socket import *

client_sk = socket(AF_INET, SOCK_DGRAM)

server_addr = ('127.0.0.1', 6009)

file_name = input('plz input file name:')

file_name_byte = file_name.encode('utf8')

pkg_format = f'!H{len(file_name_byte)}sb5sb'

pkg_struct = struct.pack(pkg_format, 2, file_name_byte, 0, 'octet'.encode('utf8'), 0)

client_sk.sendto(pkg_struct, server_addr)

new_file_name = file_name[:file_name.rindex('.')] + f'_{random.randint(1, 1000)}_{random.randint(1, 1000)}_' + file_name[file_name.rindex('.'):]


try:
    with open(new_file_name, 'ab') as f:
        while True:
            recv_pkg, server_addr = client_sk.recvfrom(516)
            operate_code, num = struct.unpack('!HH', recv_pkg[:4])
            if operate_code == 3:
                f.write(recv_pkg[4:])
            if operate_code == 6:
                f.write(recv_pkg[4:])
                print('Download completed!')
                f.close()
                break
            else:
                ack_code = 4
                ack_pkg = struct.pack('!HH', ack_code, num)
                client_sk.sendto(ack_pkg, server_addr)
except Exception as ex:
    print(f'Error happened in client {ex}')
finally:
    if f:
        f.close()



