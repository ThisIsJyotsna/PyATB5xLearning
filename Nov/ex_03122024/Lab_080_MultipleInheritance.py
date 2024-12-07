class A:

    def method_a(self):
        print("Method A")

    def commonMethod(self):
        print("Inside class A")

class B:

    def method_b(self):
        print("Method B")

    def commonMethod(self):
        print("Inside class B")

class C(B,A):

    def method_c(self):
        print("Method C")


c1=C()
c1.method_a()
c1.method_b()
c1.commonMethod()