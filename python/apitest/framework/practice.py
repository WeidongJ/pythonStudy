#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# mangoDB 操作

import pymongo
import random
import datetime
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

print(datetime.datetime.now())
# 建立连接
conn = pymongo.MongoClient('192.168.57.49',20000)
# 链接库
db = conn['testlibrary_test']
# 链接表
zxbSet = db['archive_userarchive']
docList = []
'''
for i in range(10):
    id = 'wdji20190222'+str(i)
    doc = { 
    "_id" : ObjectId(),
    "id" : id, 
    "classId" : "4400000020000017595", 
    "className" : "高一年级2班", 
    "answerRecordCreateTime" : None, 
    "schoolRank" : int(3), 
    "classRank" : int(2), 
    "gradeCode" : "10", 
    "subSubjectCodes" : None, 
    "subjectCode" : "02", 
    "score" : 15.0, 
    "userId" : "4400000020000841138", 
    "userNum" : "49966884", 
    "schoolId" : "2244000001000023457", 
    "topicSetId" : "bc9bc91a-0986-4606-9030-693df86319ca", 
    "topicSetName" : "关岭期中考试语文+数学(数学)", 
    "createTime" : datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 
    "updateTime" : datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 
    "userName" : "张四", 
    "createPaperTime" : datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 
    "topicSetCategory" : "t01Exam", 
    "examId" : "52d46089-71b7-4d7e-b5aa-4f503ef132b4", 
    "examName" : "关岭期中考试语文+数学", 
    "standardScore" : 20.0, 
    "isEnable" : None, 
    "isBeTied" : False, 
    "isSuppportPay" : None, 
    "tiArchive" : "null", 
    "unionRank" : None, 
    "adminClassId" : "4400000020000017595", 
    "adminClassName" : "高一年级2班", 
    "examFlag" : int(0), 
    "preAssignScore" : None, 
    "levelName" : None, 
    "schoolDeptRank" : None, 
    "schoolElectiveRank" : None, 
    "electiveCourses" : None, 
    "electiveType" : None, 
    "schoolDeptRankRate" : None, 
    "schoolElectiveRankRate" : None, 
    "customSchoolRank" : None, 
    "customClassRank" : None, 
    "reportVersion" : int(1), 
    "markingExamTypeCode" : "midtermExam", 
    "markingExamTypeName" : "期中考试", 
    "examCreateDateTime" : datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 
    "examDateTime" : datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}
    
    jsonDoc = json.loads(json.dumps(doc,cls=JSONEncoder)) # dumps用于序列化object对象，再用loads加载json python value
    zxbSet.insert(jsonDoc)'''

del_query =  {"classId":"wdji20190227"}
zxbSet.remove(del_query)

import logging 
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
print(logger)
logger.name




def twoSum(l1,num):
    d ={}
    for i in range(len(l1)):
        if l1[i] in d:
            return (d[l1[i]],i)
        else:
            d[num-l1[i]] = i

print(twoSum([3,2,3],5))