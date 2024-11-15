side1=int(input("enter first side"))
side2=int(input("enter second side"))
side3=int(input("enter third side"))

if side1==side2 and side1==side3:
    print("equilateral triangle")

elif side1==side2 or side1==side3 or side2==side3:
    print("isosceles triangle")

else:
    print("scalene triangle")