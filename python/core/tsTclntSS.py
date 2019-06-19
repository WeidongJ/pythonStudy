#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    in_data = bytes()
    data = tcpCliSock.recv(BUFSIZ)
    while data:
        in_data += data
        data = tcpCliSock.recv(BUFSIZ)
    with open('new_apple.png', 'wb') as f:
        f.write(in_data)
    print('图片保存成功') # strip() 方法？
    tcpCliSock.close()