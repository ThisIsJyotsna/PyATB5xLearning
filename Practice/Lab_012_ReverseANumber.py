number=int(input("enter a number"))
num=0
while(number>0):
    rev=number%10
    num=num*10+rev
    number=number//10

print(num)

