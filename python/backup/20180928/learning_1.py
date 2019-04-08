#!/usr/bin/env python3
#coding=utf-8

# 基础知识和小细节

# 将输入的值作变量，并在行前添加说明

name = input('please type your name here :')
print('your name:', name) 

# 浮点数的表示方法
111
floatNum = 12.2e16
print(floatNum)

# 变量关系：变量指向字符串

# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

#字符编码：ASCII编码 A的编码是65 z是122
#字符转换：ord()将字符转换成编码表示，chr()酱编码转换成对应的字符
print(ord('A'))
print(chr(20013))

x = b'ABC'
print(x)

# list常用方法，list和tuple的区别在于tuple不可变，更加安全
animals = ['dogs', 'cats', 'mouse']
animals.append('panda')
animals.insert(1, 'fish')
animals.pop() #删除，可传入index删除指定元素
animals.sort() #排序
print(animals)

#循环中break和continue的差别：break退出循环，continue跳过当前循环

#dict类似于其他语言中的map

#dict常用方法
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 查询key
print('xxx' in d) 
print(d.get('ccc',-1))

#set是一组key的集合，但是不会存储value，key不会重复(数学上无序，无重复的元素集合)，可以进行交集并集操作
# 常用方法：add(),remove()

#函数没有return时是省略了return None；
#空函数，先定义
def nop():
    pass

#避免函数参数数量问题，可以对参数设置默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2))
print(power(2,3))

#有多个默认参数时，仅传参是按顺序给默认参是赋值，或者传参时带上参数名
#默认参数必须指向不可变对象