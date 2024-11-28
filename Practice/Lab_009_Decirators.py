


def decoratorFunct(funct):
    def wrapper():
        print("I am inside decorator function")
        funct()
        print("Welcome")

    return wrapper()





@decoratorFunct
def Say_hello():
    print("Hello!!! Welcome!!!")

