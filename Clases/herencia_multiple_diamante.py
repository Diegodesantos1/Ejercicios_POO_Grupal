class A:
    def __init__(self,a):
        self.a = a
class B(A):
    def __init__(self, b, a):
        self.b = b
        A.__init__(self, a)
class C(A):
    def __init__(self, c, a):
        self.c = c
        A.__init__(self, a)
class D(B,C):
    def __init__(self,d, a, b, c):
        self.d = d
        B.__init__(self, a, b)
        C.__init__(self, a, c)