year=int(input("Please enter a year to check"))

if year%4==0 or year%400==0 and year%100!=0:
    print("its a leap year")
else:
    print("its not a leap year")
