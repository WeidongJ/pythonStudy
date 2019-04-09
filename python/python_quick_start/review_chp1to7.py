#!/usr/bin/env python3
# *-* coding:utf-8 *-*

# 变量风格使用驼峰式

import re
import copy

nameRegex = re.compile(r'(\d\d\d)-(\d\d\d)')
name = nameRegex.search("中国人民站起来了199-1245")
print(name.group(0))
print(name.group(1))