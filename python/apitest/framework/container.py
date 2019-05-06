#!/usr/bin/env python3
# -*- utf-8 -*-

import requests
import configparser
import os
from apitest.framework.logger import Logger

# 容器API
logger = Logger(logger='test-api').get_log()

# 读取配置


def read_config(section, key):
    config = configparser.ConfigParser()
    # 解决不同目录运行文件获取配置文件路径出错的问题
    base_path = os.path.abspath('.').split(os.path.sep+'apitest')
    file_path = base_path[0] + '/apitest/config/config.ini'
    config.read(file_path)
    value = config.get(section, key)
    return value

# api封装


def login(username, password):
    base_url = read_config('testSever', 'baseUrl')
    path = '/container/app/weakCheckLogin'
    url = base_url + path
    logger.info('login url:%s' % url)
    querystring = {'loginName': username, 'password': password}
    response = requests.get(url, params=querystring).json()
    return response['result']

# api封装
def helplist(token):
    base_url = read_config('testSever', 'baseUrl')
    path = '/container/customHelp/getCustomHelpList'
    url = base_url + path
    querystring = {'token': token}
    response = requests.get(url, params=querystring).json()
    return response


