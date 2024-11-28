stringcheck=input("enter the string")

str1=""

for i in range(len(stringcheck)-1,-1,-1):
    str1=str1+stringcheck[i]
print(str1)

if str1.lower()==stringcheck.lower():
    print("its a palindrome")
else:
    print("not a palindrome")