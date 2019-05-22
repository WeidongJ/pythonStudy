#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(__file__).split('csdn')[0])
print(sys.path)
import time
from selenium import webdriver
from framework.basepage import BasePage
from framework.logger import Logger

mylogger = Logger(logger='TestMyLog').get_log()

class BaiduSearch(object):

    driver = webdriver.Chrome()
    url = 'https://www.baidu.com'
    driver.maximize_window()
    driver.implicitly_wait(10)
    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url(self.url)
        time.sleep(1)

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

    
    def get_search_result(self):
        search_result = self.driver.find_element_by_xpath("//span[@class='nums_text']").text.split('约')[1]
        num = search_result.split('个')[0]
        print(num)
        self.basepage.take_screenshot()
        self.basepage.quit_browser()

baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()
baidu.get_search_result()