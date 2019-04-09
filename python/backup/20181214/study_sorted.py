#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip
spam = 'Hello'
print(spam.upper()) # 转换成大写
print(spam.lower()) # 转换成小写
print(spam.islower()) # 是否全小写
print(spam.isupper()) # 是否全大写
print(spam.isalnum()) # 是否只包含字母和数字
print(spam.isalpha()) # 是否只包含字母
print(spam.isdecimal()) # 是否只包含数字字符
print(spam.istitle()) # 是否仅包含大写字母开头，后面全是小写字母开头的单词
print(spam.isspace()) # 是否全是空格、制表符和换行
print(spam.startswith('123')) # 是否已传入的字符串开始或结束
print(spam.endswith('123'))

spamList = ['china','anhui','wuhu']
newSpamList = ','.join(spamList)
print(newSpamList)
print(newSpamList.split(','))
print(spam.rjust(10,'*')) # 右对齐
print(spam.ljust(10,'*')) # 左对齐
print(spam.center(20,'*')) # 右对齐
aSpam = ' hello world '
print(aSpam.strip()) # 去除首尾空格

# pyperclip模块用户拷贝粘贴字符串
pyperclip.copy(aSpam)
print(pyperclip.paste())
