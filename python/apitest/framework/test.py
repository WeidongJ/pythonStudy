#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
import requests
import os

conn = pymysql.connect(host="localhost", user="wdji", password="123456", database="webapp", charset="utf8")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
try:
    # 执行sql语句，并提交
    cursor.execute('select * from jcfw_ci')
    data = cursor.fetchall()
    # print(data)
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

cursor.close()

url = 'http://api.iflytek.com/findBuildStatBeanList.do'

def get_buildstatistics_weekly(starttime,endtime):
    d = {}
    total = 0
    for raw_param in data:
        # 删除id
        raw_param.pop('id')
        raw_param['startTime'] = starttime
        raw_param['endTime'] = endtime
        jcfw = requests.get(url, params=raw_param).json()['data']['list']
        for tg in jcfw:
            if tg['totalNum']!=0:
                d[tg['thirdGroup']] =  tg['totalNum']
                total += tg['totalNum']
        
    s = sorted(d.items(),key = lambda t:t[1],reverse=True)
    # print(s)
    # 打印
    for l in s:
        print('{key}  :  {value}'.format(key=l[0],value=l[1]))

    print("total:%s" % total )

start_time = '2019-04-22'
end_time = '2019-04-26'
get_buildstatistics_weekly(start_time,end_time)

        

