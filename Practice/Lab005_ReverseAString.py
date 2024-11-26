#we cane reverse a string by using slicing

'''statement="I am wonder woman"
print(statement[0:2])

statement2=statement[::-1]
print(statement2)'''


statement="I am wonder woman"
statement2=""
for i in range(len(statement)-1,-1,-1):
    statement2=statement2+statement[i]

print(statement2)

