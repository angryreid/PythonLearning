"""
server - PythonLearning
Author: nick
Date: 2024/12/17
Time: 11:51

Description: 

"""

import time
from threading import Thread
import os
import wx
from socket import *


# 采用Python语言开发GUI：pyqt5, tkinter, wxpython

class MsbServer(wx.Frame):
    """
    只要继承了Frame,那么当前类就是一个窗口类。
    """

    def __init__(self):
        """初始化窗口"""
        print(MsbServer.__mro__)
        print(super())
        super().__init__(None, id=102, title='老肖的服务器界面', pos=wx.DefaultPosition, size=(400, 470))

        pl = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板里面会放一些按钮，文本框，文本输入框等，把这些对象统一放入一个盒子里面
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版

        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 可升缩的网格布局,水平方向
        # 创建三个按钮
        start_server_button = wx.Button(pl, size=(133, 40), label="启动")
        record_save_button = wx.Button(pl, size=(133, 40), label="聊天记录保存")
        stop_server_button = wx.Button(pl, size=(133, 40), label="停止")
        g1.Add(start_server_button, 1, wx.TOP)
        g1.Add(record_save_button, 1, wx.TOP)
        g1.Add(stop_server_button, 1, wx.TOP)
        box.Add(g1, 1, wx.ALIGN_CENTER)  # ALIGN_CENTER 联合居中

        # 创建只读的文本框,显示聊天记录
        self.text = wx.TextCtrl(pl, size=(400, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)
        pl.SetSizer(box)
        '''以上代码窗口结束 '''

        # 给每个绑定按钮一个点击事件
        self.Bind(wx.EVT_BUTTON, handler=self.start_server, source=start_server_button)
        self.Bind(wx.EVT_BUTTON, handler=self.save_message_to_file, source=record_save_button)

        self.server_socket: socket = None  # 服务器的socket
        self.client_dict = {}  # 所有在线的客户端 , 字典中存放是多个独立的子线程

    def start_server(self, event):
        """启动服务端的socket"""
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('', 8008))
        self.server_socket.listen(3)

        # 创建一个子线程，让子线程调用accept。 等着有客户端连接进来。
        server_thread = Thread(target=self.do_work)
        server_thread.daemon = True
        server_thread.start()

    def do_work(self):
        print('服务器开始启动，并准备接受客户端的连接')
        while True:
            # 如果有10个客户端，accept就会调用10次，每一次都创建一个新的session_socket
            session_socket, client_addr = self.server_socket.accept()
            # 只接受客户端的名字。其他的聊天信息不在这里接受
            username = session_socket.recv(1024).decode('utf8')
            welcome_message = f'服务器通知：欢迎{username}进入聊天室！'
            # 服务器需要把这个欢迎的通知，发送每个一个客户端。
            # 每一个session_socket都会执行recv函数，为了不影响后面的代码执行，需要采用单独的一个线程来处理
            # 以此内推：每一个客户端 <---> session_socket <---> 独立子线程

            # 每个客户端都创建一个独立的子线程 ，专门和当前的客户端进行通信
            session_thread = SessionThread(session_socket, username, self)
            self.client_dict[username] = session_thread
            session_thread.start()
            self.show_message_and_send_message(message=welcome_message)

    def show_message_and_send_message(self, message):
        """
        专门负责显示和发送信息(通知)的函数
        第一步：在服务器自己的文本框中显示message；
        第二步：把这条message发给所有在线的客户端
        :param message:
        :return:
        """
        # 一条message 是由 ：message的主题 + 当前时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        full_message = f'{message} \n 时间：{current_time} \n'
        self.text.AppendText(f'{full_message} ---------------------------- \n')
        # 第二步：
        for client_thread in self.client_dict.values():
            if client_thread.isOn:
                # 发送通知到客户端
                client_thread.session_socket.send(full_message.encode('utf8'))

    def dis_client(self, username):
        """
        把当前要离开的客户端，从字典中删除
        :param username:
        :return:
        """
        if username in self.client_dict:
            self.client_dict.pop(username)

    def save_message_to_file(self, event):
        """
        保存所有的聊天记录到文件中
        :param event:
        :return:
        """
        data = self.text.GetValue()
        # 规定一个保存的文件： log-当前系统时间.txt
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        file_name = f'log-{current_time}.txt'
        with open(file_name, 'w', encoding='utf8') as f:
            f.writelines(data)


class SessionThread(Thread):
    """
    这是一个独立的子线程，专门和某一个客户端通信
    """

    def __init__(self, session_socket, username, server):
        super().__init__()
        self.session_socket = session_socket
        self.username = username
        self.isOn = True  # 会话线程是否启动
        self.server = server

    def run(self) -> None:
        while self.isOn:
            recv_message = self.session_socket.recv(1024).decode('utf8')
            # 收到客户端发送过来的聊天消息
            if recv_message == 'A^disconnect^B':
                # 当前客户端要离开
                self.isOn = False
                # 确认客户端的离开
                self.session_socket.send('A^disconnect^B'.encode('utf8'))
                message = f'服务器通知：{self.username}离开聊天室！'
                self.server.dis_client(self.username)
                self.server.show_message_and_send_message(message)
            else:
                #  需要把这一条消息显示在服务器界面中，并发送给所有的客户端
                full_message = f'{self.username}：{recv_message}'
                self.server.show_message_and_send_message(full_message)
        self.session_socket.close()


if __name__ == '__main__':
    app = wx.App()
    frame = MsbServer()
    frame.Show()
    app.MainLoop()  # GUI不断的刷新
