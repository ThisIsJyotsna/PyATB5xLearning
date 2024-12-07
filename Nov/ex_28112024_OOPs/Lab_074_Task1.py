#Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods

'''Use PC - to set the value of the attributes

create a Print student information method/function

3 studetns objects

PyATB().print_student_infomation()'''

class PyATB:
    Name=None
    Age=None
    Employeement=None
    Address=None
    Gender=None

    def __init__(self,Name,Age,Employeement,Address,Gender):
        self.Name=Name
        self.Age=Age
        self.Employeement=Employeement
        self.Address=Address
        self.Gender=Gender



    def StudentInformation(self):
        print("Name of the student",self.Name)
        print("Age of the student",self.Age)
        print("Employeement of the student",self.Employeement)
        print("Address of the student",self.Address)
        print("Gender of the student",self.Gender)


    def CheckEmployeement(self):
        if(self.Employeement==True):
            print("Student is currently working")
        else:
            print("Student is not working")

    def Enrollment(self):
        print("Student has enrolled for the class")


s1=PyATB("John",26,True,"India","Male")
s1.StudentInformation()
s1.CheckEmployeement()
s1.Enrollment()



