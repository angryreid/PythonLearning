"""
server - PythonLearning
Author: nick
Date: 2024/12/3
Time: 20:22

Description: 

"""
import struct
from socket import *

sk = socket(AF_INET, SOCK_DGRAM)

sk.bind(('127.0.0.1', 6009))


def download(file_name, client_ip, client_port):
    download_sk = socket(AF_INET, SOCK_DGRAM)
    try:
        with open(file_name, 'rb') as f:
            num = 0
            while True:
                operate_code = 3
                read_data = f.read(512)
                if len(read_data) < 512:
                    operate_code = 6  # the last file piece
                file_pkg = struct.pack('!HH', operate_code, num) + read_data
                download_sk.sendto(file_pkg, (client_ip, client_port))

                #             receive ack from client
                rcv_ack, (c_ip, c_port) = download_sk.recvfrom(516)
                operate_code, ack_num = struct.unpack('!HH', rcv_ack)
                if operate_code == 4 and ack_num == num:
                    num += 1
                    print(f'Server confirmed send file block {num}')
                else:
                    print(f'Server send file failed {num}')

    except Exception as ex:
        print(f'Server has error {ex}')
    finally:
        if download_sk:
            download_sk.close()


if __name__ == '__main__':
    rcv_pkg, (client_ip, client_port) = sk.recvfrom(516)
    operate_code = struct.unpack('!H', rcv_pkg[:2])
    pkg_suffix = struct.unpack('!b5sb', rcv_pkg[-7:])
    if pkg_suffix == (0, b'octet', 0):
        file_name = rcv_pkg[2:-7].decode('utf8')
        if operate_code == (2, ):
            print(f'Server will start to download {file_name}')
            download(file_name, client_ip, client_port)
