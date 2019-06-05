#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connection from :', addr)

    with open('apple.png', 'rb') as f:
        data = f.read()
    # data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    tcpCliSock.send(data)

    tcpCliSock.close()
tcpSerSock.close()
