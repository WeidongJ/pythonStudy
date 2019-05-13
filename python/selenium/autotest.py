#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://news.baidu.com')
driver.implicitly_wait(5)

el = driver.find_elements_by_xpath("//li[@class='lavalamp-item']")
for e in el:
    e.click()
    time.sleep(2)

driver.close()