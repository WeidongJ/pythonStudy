#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8900, application)
print('serving http on port 8900...')

httpd.serve_forever()