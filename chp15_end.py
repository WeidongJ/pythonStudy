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

# chp17
from PIL import ImageColor
import os
from PIL import Image

ImageColor.getcolor('red','RGBA') # 获取颜色RGBA值

os.chdir('D:\\workspace\\python\\python_quick_start')

apple = Image.open('apple.png')
print(apple.size)
apple = apple.convert('RGB') # JEPG不支持透明度
apple.save('apple.jpg')

# 创建图像
im = Image.new('RGBA',(100,200),'blue') # 未指定背景色时，默认黑色
im.save('blue.png')

# 裁剪图片
appleNew= apple.crop((100,100,120,120)) # 元组值对应坐标值

# copy图像
anotherApple = apple.copy()
# anotherApple.paste(appleNew,(0,0))
# anotherApple.paste(appleNew,(100,100))

# appleNew铺满原图
appleWidth,appleHeight = apple.size
appleNewWidth,appleNewHeight = appleNew.size
for left in range(0,appleWidth,appleNewWidth):
    for top in range(0,appleHeight,appleNewHeight):
        print(left,top)
        anotherApple.paste(appleNew,(left,top))
anotherApple.save('anotherApple.png')

# 调整图像大小
quartersizedIm = apple.resize((int(appleWidth/2),int(appleHeight/2)))
quartersizedIm.save('quartersizedIm.png')

# 旋转图像 默认逆时针
apple.rotate(90).save('appleRotate.png')

# 镜像翻转图像
apple.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png') # 左右
apple.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png') # 上下

# 更改单个像素
im = Image.new('RGBA',(100,100))
print(im.getpixel((0,0)))
for x in range(100):
    for y in range(50):
        im.putpixel((x,y),(210,210,210))

for x in range(100):
    for y in range(50,100):
        im.putpixel((x,y),ImageColor.getcolor('darkgray','RGBA'))

im.save('putPixel.png')

# 画图
from PIL import ImageDraw
imNew = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(imNew)
draw.line([(0,0),(150,55),(160,60),(199,80)],fill='black')
draw.rectangle((20,30,50,60),fill='blue')
draw.ellipse((20,30,50,60),fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), 
fill='brown')
for i in range(100,200,10):
    draw.line([(i,0),(200,i-100)],fill='green')

im2 = Image.new('RGBA',(200,200),'white')
draw2 = ImageDraw.Draw(im2)
draw2.text((20,150),'Hello',fill='purple') # 加入文本
draw2.text((100,150))

imNew.save('drawing.png')