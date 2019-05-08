#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(8)

driver.find_element_by_xpath("//div[@id='u1']/a[contains(text(),'登录')]").click()

driver.implicitly_wait(2)
driver.find_element_by_xpath("//p[contains(text(),'用户名登录')]").click()