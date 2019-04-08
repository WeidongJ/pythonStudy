#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import pickle
import json
# 错误、调试和测试
''' 
 try:就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕,可以在
 expect后加else，没有错误发生会自动执行;
 错误都是class如果先捕获到了父类，则子类永远不会被捕获到;
 try...expect可以跨越多层调用
 '''
try:
    print('try...')
    r = 10/2
    print('result:', r)
except ZeroDivisionError as e:
    print('expect:', e)
else:
    print('No Errors')
finally:
    print('finally...')
print('END')

# logging
# raise：raise语句如果不带参数，就会把当前错误原样抛出
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END2')

#调试：print，assert，logging
logging.basicConfig(level = logging.INFO)

#单元测试：
''' 运行测试集，
1.
if __name__ == '__main__':
    unittest.main()
2.
python -m unittest mydict_test
 断言：assert，另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
with self.assertRaises(KeyError):
    value = d['empty']'''

# 文档测试：注释的测试代码可以用doctest模块来运行
'''import doctest
    doctest.testmod()
    '''


#IO操作
'''读写文件可能会产生IOError，会导致closed操作不会执行，可以用try...finally
便捷的可以使用with方法,且不需要调用closed方法'''
with open('/path/file', 'r') as f:
    print(f.read())

'''read()方法会一次性读取全部内容，可以使用read(size)来限制每次读取的字节数
对于特殊文件的编码可能会不同，可以追加相关参数'''
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

#在内存中读写，StringIO读写str；BytrsIO操作二进制数据；
#序列化：变量从内存中变成可存储或传输的过程,pickle.dumps()方法吧任意对象序列化成一个bytes
#pickle.loads()反序列
#json类型转换

dic=dict(name='Bob', age=20, score=88)
pickle.dumps(dic)
json.dumps(dic)

f = open('dump.txt', 'rb')
d1= pickle.load(f)
f.close()