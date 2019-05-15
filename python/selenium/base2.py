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

time.sleep(2)
driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__submit']").click()
time.sleep(2)
try:
    error_text = driver.find_element_by_xpath("//span[@id='TANGRAM__PSP_10__error']").text
    assert error_text == u'请您输入手机/邮箱/用户名'
    print('Test Pass.')
except Exception as e:
    print('Test Failed.',format(e))