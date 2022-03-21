class A:
    def __init__(self,a):
        self.a = a
class B(A):
    def __init__(self, a, b):
        self.b = b
        super(A)
class C(A):
    def __init__(self, a, c):
        self.c = c
        A.__init__(self, a)
class D(B,C):
    def __init__(self, a, b, c):
        B.__init__(self, a, b)
        C.__init__(self, a, c)

d = D(1, 2, 3)

print(isinstance(d, A), isinstance(d, B), isinstance(d, C))

print(d.a, d.b, d.c)
