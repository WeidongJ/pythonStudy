#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a learning record'

__author__ = 'Weidong Ji'


# 类和实例：必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”
class Students(object): # object是继承的父类
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身,创建实例的时候需要传参
# 普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个
# 类的不同实例，但拥有的变量名称都可能不同：


# 访问限制：类中方法属性名称前面加上__,后可写入get方法来提供访问

#type()获取类的type，isinstance()能够判断出继承子类

#dir()获取对象的所有方法
# 类似__xx__的属性或方法在python中有特殊的用途 

#面向对象高级编程：
    #给实例绑定属性，其他实例也会有属性，但时给实例绑定的方法只有这个实例有：可以给class绑定方法
def set_score(self, score):
    self.score = score

Students.set_score = set_score

# __slot__:限制实例可以拥有的属性,example中Student实例只能绑定name，age属性，其对当前实例类有作用，对子类不起作用
class Student(object):
    __slot__=('name','age')

# @property python内置装饰器，可以将方法装饰城属性，

# 多重继承，在object中添加多个父类