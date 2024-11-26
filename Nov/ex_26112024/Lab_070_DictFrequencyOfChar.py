statement="I am wonder woman"
statement2=statement.replace(" ","")
print(statement2)
char_Frequency={}

for char in statement2:
    if char not in char_Frequency:
        char_Frequency[char]=1
    else:
        char_Frequency[char]=char_Frequency[char]+1

print(char_Frequency)