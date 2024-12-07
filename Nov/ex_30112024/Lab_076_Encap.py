class Bank:

    def __init__(self,accountNumber,balance):
        self.__accountNumber=accountNumber #private variable
        self.balance=balance


    def depositeMoney(self,deposite):
        self.balance=self.balance+deposite
        print(self.balance)

    def accountNumberrest(self):
        print(self.__accountNumber)


b1=Bank(123456,12309738)
b1.depositeMoney(500)
b1.accountNumberrest()


