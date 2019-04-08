#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# callback function 

def double(x):
    return x * 2

def quadruple(x):
    return x * 4

# middle function
def getOddNumber(k,getEventNumber):
    return 1 + getEventNumber(k)

# main function 
def main():
    k = 3
    i = getOddNumber(k,double)
    print(i)

main()

# python 调用流程
import inspect # 获取源码信息
frame = None
def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

foo()
# 堆栈比方法调用存在的时间长
frame.f_code.co_name # 打印函数名bar
caller_frame = frame.f_back # 回到上一桢 foo
caller_frame.f_code.co_name # 打印函数名foo
import dis
dis.dis(foo)
# 位运算
generator_bit = 1<<5 # x<<y: x*2**y,x>>y:x/2**y
print(generator_bit)


# &逻辑与运算（位运算）
1&3 # True ，1&2 False
# generator 
def gen_fn():
    result = yield 1
    print('result of yield:{0}'.format(result))
    result2 = yield 2
    print('result of 2nd yield:{0}'.format(result2))
    return 'Done'

bool(generator_bit&gen_fn.__code__.co_flags)
gen = gen_fn() # 调用生成器方法时，python实际上不运行这个方法而是创建一个生成器
gen.gi_frame.f_lasti
gen.send(None)
gen.gi_frame.f_lasti
gen.send('Heool')


# generator from 代表他继承的
def caller_fn():
    gen = gen_fn()
    rv = yield from gen
    print('return value of yield-from :{}'.format(rv))

caller = caller_fn()