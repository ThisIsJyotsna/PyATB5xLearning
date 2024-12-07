from dotenv import load_dotenv
import os

class Auth:

    def __init__(self,username,password):

        self.username=username
        self.password=password

    def checkAuth(self):
        if self.username=="john" and self.password=="pass123":
            print("login successfull")

        else:
            print("login failed")



load_dotenv()
username=os.getenv("Username")
password=os.getenv("Password")

a1=Auth(username,password)
a1.checkAuth()
