#!/usr/bin/env python3
# -*-coding: utf-8-*-

import socket

def threaded_method():
    sock = socket.socket()
    sock.connect(('www.sina.com.cn',80))
    request = b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
    sock.send(request)
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    print(response)
    print('123')

threaded_method()