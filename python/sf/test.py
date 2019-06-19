import functools

def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax
    return sum

nums = [1, 4, 6, 8]
f = lazy_sum(*nums)
print(f)
print(f())
print('你好')


def createCounter():
    li = [0]
    def counter():
        li[0] += 1
        return li[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA())

# 装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('Hello World!')

now()

def log_text(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_text('调用')
def new_now():
    print('Hello World!')

new_now()

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())

class Timer(object):
    def run(self):
        print('start...')

run_twice(Timer())

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1 # 访问类属性
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

print(Student('wdji'))
Student('wdji2')


class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a , self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a



for n in Fib():
    print(n, end=' ')
f = Fib()
print(f[5:10])

