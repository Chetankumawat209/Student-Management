from file_manager import file_handle
import pandas as pd

class students:
    def __init__(self,StudentID,Name,Age,Gender,Course,Email,Phone_Number,Marks):
        self.StudentID=StudentID
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Course=Course
        self.Email=Email
        self.Phone_Number=Phone_Number
        self.Marks=Marks

    def display(self):
        print("""
Student ID {StudentID}
Name {Name}
Age {Age}
Gender {Gender}
Course {Course}
Email {Email}
Phone {Phone_Number}
Marks {Marks}

              """)


class StudentManager:
    def __init__(self):
        self.file=None
        return

    def addStudent(self):
        file=file_handle()
        file.head()

    def viewStudent(self):
        pass

    def seachStudent(self):
        pass

    def updateStudent(self):
        pass
    def deleteStudent(self):
        pass
    def sortStudent(self):
        pass
    def topperStudent(self):
        pass

    def studentStatistics(self):
        pass
    
