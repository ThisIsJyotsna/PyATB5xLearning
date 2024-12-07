#Task 2

'''Create a Class Name API - RestfulBooker

name, list_of_api , links {}

print_apis, print_set()'''

class RestfulBooker:
    Name=None
    ListOfApi=[]
    Links={}

    def __init__(self,Name,ListOfApi,Links):
        self.Name=Name
        self.ListOfApi=ListOfApi
        self.Links=Links

    def DisplayAPI(self):
        for i in self.ListOfApi:
            print(i)

    def DisplayLinks(self):
        for j in self.Links:
            print(j)


API=["Rest","Soap"]

setOfLinks={"https://link1","https://link2"}

r1=RestfulBooker("studentForm",API,setOfLinks)
print(r1.Name)
r1.DisplayLinks()
r1.DisplayAPI()