#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# chp16
import smtplib

smtpObj = smtplib.SMTP('smtp.qq.com',587)
# 建立smtp连接 smtpObj.ehlo()

if smtpObj.ehlo()[0]==250:
    print('connect successful')
    # 587 端口加密
    smtpObj.starttls()
    # 登录
    loginStatus = smtpObj.login('1287424961@qq.com','zmkm1234')
    if loginStatus[0]==235:
        print('login successful')
        # 发送邮件
        recevier = smtpObj.sendmail('1287424961@qq.com','sounddone@hotmail.com','Subject: Test Mail!\nDear Weidong,It is a test mail!')
        print(recevier)
        # 断开连接
        smtpObj.quit()


# imapclient 接受邮件

import imapclient
imapObj = imapclient.IMAPClient('imap.qq.com',ssl=True)
imapObj.login('1287424961@qq.com','zmkm1234')
print(imapObj.list_folders())
# 选择文件夹
imapObj.select_folder('INBOX',readonly=True)
# 搜索邮件唯一id
UIDs = imapObj.search(['SINCE 17-Feb-2019'])
print(UIDs)
# 获取邮件对象内容
rawMessages = imapObj.fetch([838],[b'BODY[]','FLAGS'])
# 解析模块pyzmail
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[838][b'BODY[]'])
print(message.get_subject()) # 获取主题
print(message.get_address('from')) # 获取发件人
print(message.get_address('to')) # 获取收件人

# imapObj.delete_messages([838]) 删除电子邮件

# 原始邮件获取正文：邮件格式可能是text/html 或者2者的混合
# 纯文本电子邮件：PyzMessage.html_part = None,纯html邮件PyzMessage.text_part = None
print(message.text_part == None)
# decode原始bytes数据
message.html_part.get_payload().decode(message.html_part.charset)
# 断开连接
imapObj.logout()