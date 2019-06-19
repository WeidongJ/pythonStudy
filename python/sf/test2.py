class A(object):

    def __init__(self):
        self.name = 'A'


class B(object):

    def __init__(self):
        self.name = 'B'

class C(A, B):
    pass

class D(B, A):
    pass


a = C()
print(a.name)
b = D()
print(b.name)