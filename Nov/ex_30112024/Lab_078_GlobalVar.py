

a=10

class Variable:

    b=11

    def print_info(self):
        c=10

        print(self.b)
        global a
        a=a+1
        print(a)
        print(c)

    def print_myinfo(self):
        global a
        print("--------")
        print("--------")
        print("--------")
        print(a)


v1=Variable()
v1.print_info()
v1.print_myinfo()