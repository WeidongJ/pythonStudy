#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from framework.logger import Logger

'''base operation'''

mylogger = Logger(logger='BasePage').get_log()

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def take_screenshot(self):
        img_path = os.path.split(os.path.dirname(__file__))[0] + '/screenshots/'
        current_time = time.strftime('%Y%m%d%H%M', time.localtime())
        screen_name = img_path + current_time + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylogger.info('开始截图并保存')
        except Exception as e:
            print('截图失败', format(e))


