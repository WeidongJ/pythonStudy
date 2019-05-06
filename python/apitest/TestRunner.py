#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import sys
import os
base_path = os.path.abspath('.').split(os.path.sep+'apitest')[0]
sys.path.append(base_path)
print(sys.path)

from apitest.testsuits.getCustomHelpList import GetCustomHelpList
import HTMLTestRunner
import time
from apitest.framework.sendMail import sendMail


def run():
    # 测试报告
    report_path = os.getcwd().split(os.path.sep + 'apitest')[0] + '/apitest/test_report/'
    title = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    report_file = report_path + title + 'report.html'
    fp = open(report_file, 'wb')
    # 加载测试用例
    suite = unittest.TestSuite()
    suite.addTest(GetCustomHelpList('test_tokenCheck1'))
    suite.addTest(GetCustomHelpList('test_tokenCheck2'))
    suite.addTest(GetCustomHelpList('test_numCheck1'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口自动化测试报告', description='用例执行情况')
    runner.run(suite)
    # 关闭文件
    fp.close()
    sendMail(report_file)


if __name__ == '__main__':
    run()
