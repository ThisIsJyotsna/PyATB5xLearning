

my_dict = {"a": 3, "b": 1, "c": 2}
print(len(my_dict))
my_dict1={}
my_numList=list(my_dict.values())
print(my_numList)

my_numList.sort()
print(my_numList)

for i in my_numList:
    for key, value in my_dict.items():
        if my_dict[key]==i:
            my_dict1[key]=i

print("sorted dictionary")
print(my_dict1)