class A:
    def __init__(self,a):
        self.a = a
class B(A):
    def __init__(self, b, a):

class C(A):
    def __init__(self, c, a):
class D(B,C):
    def __init__(self,d, a, b, c):