#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#记录显示登录日志实例
import time
def write_loginfo(user_name):
    #将用户登录信息写入日志
    with open('log.txt','a') as f:
        string = "用户名:{} 登录时间: {}\n".format(user_name,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        f.write(string)

def read_loginfo():
    with open('log.txt','r') as f:
        for line in f.readlines():
            print(line.strip())
    
if __name__ == '__main__':
    _user_name = 'wujie'

    _passwd = '123456'
    user_name = input("输入用户名:")
    while True:
        if len(user_name) < 2:
            print("用户名长度不少于2位")
            user_name = input("输入用户名:")
            continue
        if user_name != _user_name:
            print('用户不存在')
            user_name = input("输入用户名:")
            continue
        break
    passwd = input("输入密码:")
    while True:
        if len(passwd) < 6:
            print('用户密码长度不少于6位')
            passwd = input("输入密码:")
            continue
        if passwd != _passwd:
            print('密码错误')
            continue
        break
    print('登录成功')
    write_loginfo(user_name)
    read_loginfo()