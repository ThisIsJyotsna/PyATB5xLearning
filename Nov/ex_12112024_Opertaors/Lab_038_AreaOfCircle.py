import math

r=float(input("Enter the radius of a circle"))
piValue=math.pi
radiusSquare=pow(r,2)
#print(radiusSquare)
area=piValue*radiusSquare
print(area)

if area>10:
    print("area is greater than 10")

elif area==10:
    print("area is equal to 10")

else:
    print("area is less than 10")


