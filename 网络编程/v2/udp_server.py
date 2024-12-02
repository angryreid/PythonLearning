"""
udp - PythonLearning
Author: nick
Date: 2024/12/2
Time: 20:42

Description: 

"""
import socket


def main():
    # Create
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind
    server_socket.bind(('192.168.1.3', 6001))

    # Receive
    msg, addr = server_socket.recvfrom(10 * 1024)
    print(f'Received msg from IP: {addr[0]}, port: {addr[1]}')
    print(f'Msg: {msg.decode("utf8")}')

    # Send
    send_msg = input('Plz input msg to client:')
    server_socket.sendto(send_msg.encode('utf8'), addr)

    server_socket.close()


if __name__ == "__main__":
    main()
