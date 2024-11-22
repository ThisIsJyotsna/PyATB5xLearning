def addMessage(funct):
    def wrapper():
        print("This Is Jyotsna")
        funct()
    return wrapper()

@addMessage
def sayHello():
    print("Hello")