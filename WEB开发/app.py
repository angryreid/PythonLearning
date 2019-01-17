#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def homo():
    return '<h1>Home</h1>'

@app.route('/singin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h1>Welcome ! admin</h1>'
    return '<h1>BAD</h1>'

if __name__ == "__main__":
    app.run()