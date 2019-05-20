#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from logger import Logger

class GetTime(object):

    def get_system_time(self):
        print(time.time())
        print(time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(new_time)

localtime = GetTime()
localtime.get_system_time()
mylogger = Logger(logger='get_time').get_log()
mylogger.info('test')