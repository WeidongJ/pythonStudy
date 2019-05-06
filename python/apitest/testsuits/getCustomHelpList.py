#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 将当前工作目录加入到系统路径
import os
import sys
base_path = os.path.abspath('.').split(os.path.sep+'apitest')[0]
sys.path.append(base_path)


from apitest.framework.container import login
from apitest.framework.container import helplist
import unittest



class GetCustomHelpList(unittest.TestCase):

    def setUp(self):
        self.username = '70968741'
        self.password = 'aaaaaa'

    def test_tokenCheck1(self):
        self.token = ''
        r = helplist(self.token)
        self.assertEqual(r['errorCode'], 0)

    def test_tokenCheck2(self):
        self.token = '66fff67b-f264-485f-a0aa-c45bcd9ff03c'
        try:
            r = helplist(self.token)
            self.assertEqual(r['errorCode'], 0)
        except Exception as e:
            print('请求异常', format(e))

    def test_numCheck1(self):
        self.token = login(self.username, self.password)['token']
        r = helplist(self.token)
        self.assertEqual(r['errorCode'], 0)
        self.assertEqual(r['result'][0]['title'], '口袋直播是什么？')

    def tearDown(self):
        self.countTestCases()


if __name__ == '__main__':
    unittest.main()
