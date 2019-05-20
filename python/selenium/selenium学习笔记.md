---
title: selenium学习笔记
date: 2019-5-14
categories:
    - 学习
tags: 
    - selenium
    - python
---
# selenium学习笔记

## 问题
### 模拟鼠标点击问题
使用Actions.Keys 模拟键盘组合键ctrl+t 未生效：

        driver.find_element_by_tag_name('body')
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
原因：元素需要被选中，改动如下：

        driver.find_element_by_tag_name('body').click() 
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
### 无法点击
无法点击报错如下：
    
    selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <a id="con_subMenu8" class="icon_f" href="/container/personal/index">...</a> is not clickable at point (201, 279). Other element would receive the click:

原因：

解决方法：

    element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
    driver.execute_script("arguments[0].click();", element)