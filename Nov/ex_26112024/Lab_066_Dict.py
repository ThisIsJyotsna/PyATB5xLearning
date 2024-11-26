my_Dictionary={
    "name":"Jyotsna",
               "age":26,
               "role":"Automation tester",
               "experience":5
               }

print(my_Dictionary["name"])
print(my_Dictionary.get("name"))

my_Dictionary["country"]="India"
print(my_Dictionary)

for key,value in my_Dictionary.items():
    print(key,"->",value)