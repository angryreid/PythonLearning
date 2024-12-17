"""
client - PythonLearning
Author: nick
Date: 2024/12/17
Time: 11:51

Description: 

"""

from socket import *
from threading import Thread

import wx


class MsbClient(wx.Frame):

    def __init__(self, c_name):  # c_name:客户端名字
        # 调用父类的初始化函数
        wx.Frame.__init__(self, None, id=101, title='%s的客户端界面' % c_name, pos=wx.DefaultPosition, size=(400, 470))

        pl = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板里面会放一些按钮，文本框，文本输入框等，把这些对象统一放入一个盒子里面
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版

        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 可升缩的网格布局,水平方向
        # 创建两个按钮
        conn_button = wx.Button(pl, size=(200, 40), label="连接")
        dis_conn_button = wx.Button(pl, size=(200, 40), label="离开")
        g1.Add(conn_button, 1, wx.TOP | wx.LEFT)  # 连接按钮布局在左边
        g1.Add(dis_conn_button, 1, wx.TOP | wx.RIGHT)  # 断开按钮布局在右边
        box.Add(g1, 1, wx.ALIGN_CENTER)  # ALIGN_CENTER 联合居中

        # 创建聊天内容的文本框，不能写消息 :TE_MULTILINE -->多行  TE_READONLY-->只读
        self.text = wx.TextCtrl(pl, size=(400, 250), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)

        # 创建聊天的输入文本框,可以写
        self.input_text = wx.TextCtrl(pl, size=(400, 100), style=wx.TE_MULTILINE)
        box.Add(self.input_text, 1, wx.ALIGN_CENTER)

        # 最后创建两个按钮，分别是发送和重置
        g2 = wx.FlexGridSizer(wx.HORIZONTAL)
        clear_button = wx.Button(pl, size=(200, 40), label="重置")
        send_button = wx.Button(pl, size=(200, 40), label="发送")
        g2.Add(clear_button, 1, wx.TOP | wx.LEFT)
        g2.Add(send_button, 1, wx.TOP | wx.RIGHT)
        box.Add(g2, 1, wx.ALIGN_CENTER)

        pl.SetSizer(box)  # 把盒子放入面板中

        # 给所有按钮绑定鼠标点击事件
        self.Bind(wx.EVT_BUTTON, handler=self.connect_server, source=conn_button)
        self.Bind(wx.EVT_BUTTON, handler=self.send_message, source=send_button)
        self.Bind(wx.EVT_BUTTON, handler=self.dis_connection, source=dis_conn_button)

        self.username = c_name  # 定义一个用户名属性
        self.isConnect = False  # 是否已经连上服务器了
        self.client_socket = None

    def connect_server(self, event):
        """客户端连接服务器，并把自己的用户名发给服务器"""
        print(f'客户端{self.username}, 开始连接服务器！')
        if not self.isConnect:
            self.client_socket = socket(AF_INET, SOCK_STREAM)
            self.client_socket.connect(('127.0.0.1', 8008))
            self.isConnect = True
            # 客户端连接成功之后，立马就发送用户名给服务器。
            self.client_socket.send(self.username.encode('utf8'))
            # 接下来就可以正常聊天了。 需要一个独立的子线程，专门负责服务器的信息收发
            t = Thread(target=self.receive_and_send_data)
            t.daemon = True
            t.start()

    def receive_and_send_data(self):
        """
        客户端专门和服务器之间，收信息(通知)的函数
        :return:
        """
        while self.isConnect:
            message = self.client_socket.recv(1024).decode('utf8')
            if not message:
                self.isConnect = False
            elif message == 'A^disconnect^B':
                # 服务已经确认我的客户端离开
                self.isConnect = False
            else:
                # 展示出来
                self.text.AppendText(f'{message}')
                self.text.AppendText('------------------------------------- \n')
        self.client_socket.close()
        self.client_socket = None

    def send_message(self, event):
        """
        专门负责 发送客户端消息的函数
        :return:
        """
        if self.isConnect:
            s_m = self.input_text.GetValue().strip()  # 获取输入文本框的内容
            if s_m:
                self.client_socket.send(s_m.encode('utf8'))
                self.input_text.SetValue('')

    def dis_connection(self, event):
        """
        客户端离开聊天室， 一定要发一条（特定）消息给服务器，
        规定：当客户端发送： A^disconnect^B . 就代表客户端要离开。
        :param event:
        :return:
        """
        self.client_socket.send('A^disconnect^B'.encode('utf8'))


if __name__ == '__main__':
    cname = input('请输入一个用户名:')
    app = wx.App()
    frame = MsbClient(c_name=cname)
    frame.Show()
    app.MainLoop()  # GUI不断的刷新
