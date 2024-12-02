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
    client_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind
    # client_server.bind(('192.168.1.3', 6002))

    # Send
    send_msg = input('Plz input msg to server:')
    client_server.sendto(send_msg.encode('utf8'), ('192.168.1.3', 6001))

    # Receive
    msg, addr = client_server.recvfrom(10 * 1024)
    print(f'Received msg from IP: {addr[0]}, port: {addr[1]}')
    print(f'Msg: {msg.decode("utf8")}')

    client_server.close()


if __name__ == "__main__":
    main()
