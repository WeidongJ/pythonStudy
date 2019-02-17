#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# chp15

import time
import datetime

print(time.time())

def calcProd():
    product = 1
    for i in range(1,100000):
        product *= i
    return product

startTime = time.time()
calcProd()
endTime = time.time()
print('total cost %s' %(round(endTime-startTime,2)))

# datetime 格式化时间
now = datetime.datetime.now()
print(now)
print(now.year) # 获取年月日方法

date = datetime.datetime.fromtimestamp(100000)

# date比较
date1 = datetime.datetime(2019,1,1,0,0,0)
date2 = datetime.datetime(2019,1,1,0,0,1)
print(date1>date2)

# 存储时间段 timedalta :可接受的关键字参数，weeks、days、hours、minutes、seconds、milliseconds和microseconds，由于month和year都是会变的
span = datetime.timedelta(days=1,hours=2,seconds=15)
print(span)
print(str(span))
print(span.total_seconds())
print(now+span) # 时间加时间段
print(now-span)

# strftime 将datetime转化成字符串
'''
%Y 带世纪的年份，例如'2014' 
%y 不带世纪的年份，'00'至'99'（1970至2069） 
%m 数字表示的月份, '01'至'12' 
%B 完整的月份，例如'November' 
%b 简写的月份，例如'Nov' 
%d 一月中的第几天，'01'至'31' 
%j 一年中的第几天，'001'至'366' 
%w 一周中的第几天，'0'（周日）至'6'（周六） 
%A 完整的周几，例如'Monday' 
%a 简写的周几，例如'Mon' 
%H 小时（24小时时钟），'00'至'23' 
%I 小时（12小时时钟），'01'至'12' 
%M 分，'00'至'59' 
%S 秒，'00'至'59' 
%p 'AM'或'PM' 
%% 就是'%'字符 '''
formatNow =  now.strftime('%Y/%m/%d %H:%M:%S')
print(formatNow)

# strptime 将成字符串转化datetime

print(datetime.datetime.strptime('2019 01 31','%Y %m %d'))

# 多线程
import threading
print('start program')

def wakeUp():
    time.sleep(3)
    print('Wake Up')

wakingThread =  threading.Thread(target=wakeUp) 
printThread = threading.Thread(target=print,args=['你好','我是','weidong'],kwargs={'sep':' & '})
wakingThread.start()
printThread.start()

print('end of program')