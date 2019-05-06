#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 将当前工作目录加入到系统路径
import os
import sys
base_path = os.path.abspath('.').split(os.path.sep+'apitest')[0]
print(base_path)
sys.path.append(base_path)

print(sys.path)

from apitest.framework.ciapi import get_buildstatistics_weekly

start_time = '2019-04-12'
end_time = '2019-04-19'
get_buildstatistics_weekly(start_time,end_time)


