grade=int(input("enter grade"))

if grade>=90 and grade<=100:
    print("Grade A")

elif grade>=80 and grade<=89:
    print("Grade B")

elif grade>=70 and grade<=79:
    print("Grade C")

elif grade>=60 and grade<=69:
    print("Grade D")

elif grade>=0 and grade<=59:
    print("Grade F")
elif grade>100 or grade<0:
    print("Enter valid grade")
