#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.126.com')
time.sleep(1)
driver.execute_script("window.alert('1234.');")
# switch to alert -- accept
# driver.switch_to.alert().accept()
# --dismiss
# driver.switch_to_alert().dismiss() # 实测switch_to.alert()会报错：TypeError: 'Alert' object is not callable

driver.switch_to.alert.dismiss()
iframe = driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//input[contains(@id,'auto-id')]").send_keys('123123')
# 截图
driver.get_screenshot_as_file('126.png')