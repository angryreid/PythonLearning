"""
server - PythonLearning
Author: nick
Date: 2024/12/4
Time: 22:08

Description: 

"""
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 6666))
server_socket.listen(5)

# create session
while True:
    session_socket, client_addr = server_socket.accept()

    while True:
        rcv_pkg = session_socket.recv(1024)
        msg = rcv_pkg.decode('utf8')
        print(f'Client-{client_addr[1]}: {msg}')
        if msg == 'exit':
            break
        reply = input('Server reply msg:')
        session_socket.send(reply.encode('utf8'))

    session_socket.close()

server_socket.close()
