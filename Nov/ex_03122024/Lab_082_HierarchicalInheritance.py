class A:

    def methodA(self):
        print("Inside class A")



class B(A):

    def methodB(self):
        print("Inside class B")


class C(A):

    def methodC(self):
        print("Inside class C")

class D(A):

    def methodD(self):
        print("Inside class D")



c1=C()
c1.methodA()
c1.methodC()

d1=D()
d1.methodA()
d1.methodD()

b1=B()
b1.methodA()
b1.methodB()