"""
client - PythonLearning
Author: nick
Date: 2024/12/4
Time: 22:14

Description: 

"""
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('127.0.0.1', 6666))

while True:
    msg = input('Client send msg:')
    client_socket.send(msg.encode('utf8'))
    if msg == 'exit':
        break
    rcv_pkg = client_socket.recv(1024).decode('utf8')
    print(f'Server: {rcv_pkg}')

client_socket.close()