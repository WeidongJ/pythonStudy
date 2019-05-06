#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

url = 'https://test.zhixue.com'
path = '/container/app/weakCheckLogin'

def get_token(username,password):
    r = requests.get(url+path, params = {'loginName': username, 'password': password}).json()
    return r['result']['token']

print(get_token('70968741','aaaaaa'))