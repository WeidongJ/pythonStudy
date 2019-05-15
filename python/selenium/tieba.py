#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

dirver = webdriver.Chrome()
dirver.get('https://tieba.baidu.com/index.html')
time.sleep(1)
target_ele = dirver.find_element_by_partial_link_text('地区')
dirver.execute_script('return arguments[0].scrollIntoView();',target_ele)