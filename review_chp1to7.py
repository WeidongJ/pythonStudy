#!/usr/bin/env python3
# *-* coding:utf-8 *-*

# 变量风格使用驼峰式

import random
import copy
import pyperclip

print(random.randint(-1,5000))


try:
    a = 5/0
except ZeroDivisionError: # 异常类型要正确
    print('Wrong')


# chp3.11.1 Collatz序列
def collatz(number):
    if number%2==0:
        return number//2
    else:
        return number*3+1

print('请输入一个数：')
num = input()
try:
    numInt = int(num)
    while numInt!=1:
        print(numInt)
        numInt = collatz(numInt)
    print(numInt)
except ValueError:
    print('请输入数字！')


# chp4
person = ['1.65','male','asian']
height,gender,country = person # 批量赋值
print(height+gender+country)

# 方法和函数是一回事，只是他调用在一个值上 如：
print(person.index('1.65'))
print('Four score and seven ' + \
'years ago...') # 续行字符\

# 列表值可变，字符串、元组为不可变序列，python内部可以实现一些优化，让使用元组的代码比列表的更快，
# 列表和元组可以相互转换  如:
newPerson = tuple(person)
print(newPerson)

# 列表（字典）赋值时用的是引用 如：
otherPerson = person
otherPerson[1] = 'female'
print(person) # person = ['1.65', 'female', 'asian']

# 列表copy
anotherPerson = copy.copy(person)
anotherPerson[2] = 'EU'
print(anotherPerson) # anotherPerson = ['1.65', 'female', 'EU']
print(person) # person = ['1.65', 'female', 'asian']

# chp 4.10.1
def printList(l):
    s = ''
    try:
        for i in range(0,len(l)-1):
            s = s + l[i] + ','
        s = s + 'and '+l[-1]
        print(s)
    except IndexError:
        print('空list！')

spam = []
printList(spam)

# chp 4.10.2
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

for y in range(0,len(grid[1])):
    for x in range(0,len(grid)):
        print(grid[x][y],end='')
    print('')


# chp5 dict
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
if 'Alice' in birthdays:
    print('1')
if 'Apr 1' in birthdays:
    print('1') # 判断key是否存在

# .keys()方法返回字典key列表    get()方法:它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值
# setdefault()方法 ：是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值
print(birthdays.get('111',0))
birthdays.setdefault('weidong','jen 1')
print(birthdays)

# chp5
def dispalyInventory(inventory):
    print('inventory')
    totalItems = 0
    for k, v in inventory.items():
        print('{value} {key}'.format(value=v,key=k))
        totalItems += v
    print('totalItems : %d' %(totalItems))

def addInventory(inventory,addedItems):
    for k,v in addedItems.items():
        inventory.setdefault(k,0)
        inventory[k] += v
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
newStuff = {'apple': 1, 'torch': 3, 'gold coin': 42}
addInventory(stuff,newStuff)
dispalyInventory(stuff)



#chp 6
# 字符串方法： 
spam = 'Hello'
print(spam.upper()) # 转换成大写
print(spam.lower()) # 转换成小写
print(spam.islower()) # 是否全小写
print(spam.isupper()) # 是否全大写
print(spam.isalnum()) # 是否只包含字母和数字
print(spam.isalpha()) # 是否只包含字母
print(spam.isdecimal()) # 是否只包含数字字符
print(spam.istitle()) # 是否仅包含大写字母开头，后面全是小写字母开头的单词
print(spam.isspace()) # 是否全是空格、制表符和换行
print(spam.startswith('123')) # 是否已传入的字符串开始或结束
print(spam.endswith('123'))

spamList = ['china','anhui','wuhu']
newSpamList = ','.join(spamList)
print(newSpamList)
print(newSpamList.split(','))
print(spam.rjust(10,'*')) # 右对齐
print(spam.ljust(10,'*')) # 左对齐
print(spam.center(20,'*')) # 右对齐
aSpam = ' hello world '
print(aSpam.strip()) # 去除首尾空格

# pyperclip模块用户拷贝粘贴字符串
pyperclip.copy(aSpam)
print(pyperclip.paste())
