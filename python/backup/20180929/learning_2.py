#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Iterable,Iterator

#可变参数*args，定义时加*,调用函数时可输入多个参数（常用于传递list或tuple）
def calc(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(calc(1,2,3))
# 当参数时list或者元组时,可以用*变量名

li = [1,2,4]
print(calc(*li))

#关键字参数**kw，调用类似可变参数，可以限制关键字参数的命名

#递归函数：函数内部调用自己本身，尾递归，return语句不能包含表达式

#切片

#迭代：dict可以用d.values获得value或者d.items同事迭代key和value

#判断对象是否可迭代Iterable,from collections import Iterable
print(isinstance('abc', Iterable))

#enumerate可以将list变成索引-元素对形式
for i, value in enumerate([3,2,1]):
    print(i,value)

#列表生成式[]：生成式在前面，后面接for循环
li1 = [x * x for x in range(1, 11) if x % 2 == 0]

# 生成器(),generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

#打印杨辉三角
def triagnles():
    row = [1]
    while True:
        yield(row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]


#迭代器Iterator：凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
isinstance(iter([]), Iterator)

#高阶函数：把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
