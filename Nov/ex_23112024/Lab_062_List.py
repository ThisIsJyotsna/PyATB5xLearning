from itertools import count

my_list=["john","derek","cleon","deman"]
count=0
print(my_list[1])
for i in my_list:
    count+=1
    print(i,count)

print(len(my_list))