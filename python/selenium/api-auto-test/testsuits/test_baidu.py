#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])

import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger

mylogger = Logger(logger='baidu_unittest').get_log()

class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        mylogger.info('search selenium')
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test fail.',format(e))

if __name__ == '__main__':
    unittest.main()