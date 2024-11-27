#Python program to find the sum of all items in a dictionary

'''Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600'''

dictionaryItems={"a": 100, "b":200, "c":300}
sum=0
for key, values in dictionaryItems.items():
    sum=sum+values

print(sum)