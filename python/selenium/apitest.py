#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# first demo auto search on baidu

# driver = webdriver.Firefox() # Firefox()
driver = webdriver.Chrome() # chrome()
# driver = webdriver.Ie()

driver.maximize_window()
driver.implicitly_wait(8) # 设置隐式等待

driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//*[@id='kw']").send_keys('selenium')
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(2)
driver.find_element_by_xpath("//div/h3/a/em[text()='Selenium']").is_displayed()

driver.quit()