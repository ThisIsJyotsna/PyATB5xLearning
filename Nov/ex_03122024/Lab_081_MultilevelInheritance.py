class A:

    def methodA(self):
        print("Inside class A")



class B(A):

    def methodB(self):
        print("Inside class B")


class C(B):

    def methodC(self):
        print("Inside class C")



c1=C()
c1.methodB()
c1.methodA()