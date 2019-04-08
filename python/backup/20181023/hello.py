#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#响应http请求的函数

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello,<h1>']