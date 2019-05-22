#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apitest.framework.container import read_config


def sendMail(filename):
    # 编辑邮件内容
    f = open(filename, 'rb')
    mail_body = f.read()
    f.close()
    # 获取邮件收发者信息
    smtp_server = read_config('mailConfig', 'smtp_server')
    from_addr = read_config('mailConfig', 'sender')
    to_addr = read_config('mailConfig', 'receiver')
    password = read_config('mailConfig', 'password')
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    # 邮件正文
    msg = MIMEMultipart()
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('接口自动化测试报告', 'utf-8')
    msg.attach(text)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header('接口自动化测试报告', 'utf-8')
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
