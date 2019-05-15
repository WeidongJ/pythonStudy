#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

url = 'https://www.zhixue.com'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_id("txtUserName").send_keys('43260329')
driver.find_element_by_id('txtPassword').send_keys('aaaaaa')
driver.find_element_by_id('signup_button').click()
time.sleep(4)
driver.find_element_by_class_name('aui_close').click()
driver.implicitly_wait(5)
element = driver.find_element_by_xpath("//a[contains(text(),'私信')]")
driver.execute_script("arguments[0].click();", element)
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'发起私信')]").click()
driver.find_element_by_xpath("//div[@class='receiver_man']/a").click()
select = driver.find_element_by_xpath("//ul[@id='had_selected_1']/li[1]")
print(select.size) # 打印元素大小

# 模拟键盘事件
element_1 = driver.find_element_by_tag_name('body')
element_1.click()
element_1.send_keys(Keys.CONTROL + 'a')
time.sleep(3)
select.click()
try:
    assert select.is_selected()
    print('Test pass.')
except Exception as e:
    print('Test fail.',format(e))
driver.close()



