#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClassA(object):
    string1 = '123'

    def method(self):
        print('一个 实例')
        print(self)


test = ClassA()
test.method()
