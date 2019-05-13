#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window() # 最大化窗口
driver.set_window_size(1280,800) # 设置窗口大小
print(driver.get_window_size())
driver.find_element_by_xpath("//a[text()='关于百度']").click()
driver.back() # 后退
driver.forward() # 前进
# driver.find_element_by_css_selector('#kw').clear() # 清除文本框内容
time.sleep(4)
driver.find_element_by_xpath("//ul[@class='bd-nav']/li[4]").click()
handles2 = driver.window_handles # 获取当前浏览器所有句柄
for handle in handles2:
    if handle != driver.current_window_handle:
        driver.close
        try:
                driver.switch_to.window(handle) # use driver.switch_to.window instead driver.switch_to_window(handle)
        except Exception as e:
                print('e:',format(e))

emailRegex = re.compile(r'\w+@\w+\.\w+')
doc = driver.page_source
a = emailRegex.findall(doc)
print(a)
driver.refresh()
time.sleep(8)
print(driver.capabilities['version']) # 打印版本
print(driver.current_url) # 打印当前url
print(driver.title) # 打印 title
try:
        assert u'联系百度'==driver.title
        print('pass')
except Exception as e:
        print('Assertion test faild',format(e))
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
time.sleep(4)
driver.find_elements_by_xpath("//*[@type='radio']")
driver.quit() 
# driver.close() # quit后退出了浏览器


    

