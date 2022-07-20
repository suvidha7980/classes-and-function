class A():
    def __init__(self,a,b):
        print(a+b)
    def f1(self):
        print("hello")
ob=A(12,3)
ob.f1()

########################################################################################################################

class A():
    a=89
    b=70
    def __init__(self,a,b):
        self.a=a
    def f1(self,a,b):
        print(a+b)
        print(self.a+self.b)
ob=A(12,34)
ob.f1(12,45)

########################################################################################################################

class A():
    a=8
    b=0
    def __init__(self,a,b):
        self.a=a
    def f1(self,a,b):
        print(a + b)
        print(self.a + self.b)
ob=A(5,10)
ob.f1(12,4)