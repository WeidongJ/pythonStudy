#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''base operation'''

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

