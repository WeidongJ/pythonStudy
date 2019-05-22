#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException

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

    def find_element(self, **kw):
        element = ''
        if len(kw) != 1:
            raise KeyError('elements is more than 1.')
        elif 'id' in kw:
            try:
                element = self.driver.find_element_by_id(kw['id'])
                mylogger.info('element find: %s' % kw['id'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'name' in kw:
            try:
                element = self.driver.find_element_by_name(kw['name'])
                mylogger.info('element find: %s' % kw['name'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'class_name' in kw:
            try:
                element = self.driver.find_element_by_class_name(kw['class_name'])
                mylogger.info('element find: %s' % kw['class_name'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'partial_link_text' in kw:
            try:
                element = self.driver.find_element_by_partial_link_text(kw['partial_link_text'])
                mylogger.info('element find: %s' % kw['partial_link_text'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'tag_name' in kw:
            try:
                element = self.driver.find_element_by_tag_name(kw['tag_name'])
                mylogger.info('element find: %s' % kw['tag_name'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'link_text' in kw:
            try:
                element = self.driver.find_element_by_link_text(kw['link_text'])
                mylogger.info('element find: %s' % kw['link_text'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'xpath' in kw:
            try:
                element = self.driver.find_element_by_xpath(kw['xpath'])
                mylogger.info('element find: %s' % kw['xpath'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        elif 'css_selector' in kw:
            try:
                element = self.driver.find_element_by_css_selector(kw['css_selector'])
                mylogger.info('element find: %s' % kw['css_selector'])
            except NoSuchElementException as e:
                mylogger.error('element find failed:%s' % e)
        
