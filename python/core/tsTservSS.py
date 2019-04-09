#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

# 重写了流处理方法
class MyRequestHandler(SRH):

    def handle(self):
        print('... connected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline())).encode())

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()