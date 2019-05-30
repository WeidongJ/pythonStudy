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
<<<<<<< HEAD
    a = []
    while num > 0:
        a.append(str(num%7))
=======
    newNum = 0
    a = 1
    while num>0:
        temp = num%7
>>>>>>> a265ba3b3187a0d0ce52576e543bb30d625f315c
        num = num //7
        newNum += temp*a
        a *= 10
    if n > 0:
        return newNum
    else:
        return -newNum

<<<<<<< HEAD

print(convert(-17))
=======
print(convert(70))
>>>>>>> a265ba3b3187a0d0ce52576e543bb30d625f315c
    
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