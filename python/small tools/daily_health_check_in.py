#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

s = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Content-Type': 'application/json'}
s.post('http://183.129.255.162:81/web/api/login',headers=headers,json={"a":"190473","b":"15755315230"})

payload = {"arrivalCurrentPlaceDate":"2020-02-28","backWorkDate":"2020-02-28","currentCity":"合肥市","currentCounty":"高新区","currentProvince":"安徽省","employeeId":"190473","leavedCurrentPlace":0,"physicalCondition":"有过不适已康复","physicalConditionDetail":"N/A","remark":"N/A","routeAfter":"1/20-1/23 合肥 3天；1/23-2/28,芜湖无为，2/28-至今，合肥高新区","specialCity":"","specialCityDetail":"N/A"}
r_sign_in = s.post('http://183.129.255.162:81/web/api/employee/fill',headers=headers,json=payload)
print(r_sign_in.text)