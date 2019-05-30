#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from framework.logger import Logger


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


def convert(n):
    num = abs(n)
    a = []
    while num > 0:
        a.append(str(num%7))
        num = num //7
    if n > 0:
        return int(''.join(a[::-1]))
    else:
        return -int(''.join(a[::-1]))


print(convert(-17))
    
int('021')


class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))
        if x>=0:
            return int(num[::-1])*(int(num[::-1])<2**31)
        else:
            return -int(num[::-1])*(int(num[::-1])<2**31)
a=Solution()
print(a.reverse(-120))

def isPalindrome(x):
    if x<0:
        return False
    elif x[::-1]==x:
        return True
    else:
        return False