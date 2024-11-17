

name=input("enter name")
letter=""
for i in range(len(name)-1,-1,-1):
    letter=letter+name[i]

if letter.upper()==name.upper():
    print("is palindrome")

else:
    print("not a palindrome")
