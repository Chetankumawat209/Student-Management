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
        self.df=None
        return

    def addStudent(self):
        self.df=file_handle()
        ID=int(input("Enter Student ID "))
        Name=input("Enter Student name ")
        Age=int(input("Enter Student age "))
        Gender=input("Enter Student gender ")
        course=input("Enter Student course ")
        Email=input("Enter Email")
        Phone=int(input("Enter student phone number"))
        Marks=int(input("Enter student marks"))

        new_df=pd.DataFrame({
            "student ID":[ID],
            "Name":[Name],
            "Age":[Age],
            "Gender":[Gender],
            "Course":[course],
            "Email":[Email],
            "Phone Number":[Phone],
            "Marks":[Marks]
        })
        self.df=pd.concat((self.df,new_df),axis=0)
        self.df.head()
        # self.df.to_csv(r"C:\Users\cheta\OneDrive\Desktop\students.csv",index=False)
        
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
    
    def save(self):
        print("1 Save data")
        print("2 Not save data")
        choice=input("Enter your choice ")
        if choice =="1":
            self.df.to_csv(r"C:\Users\cheta\OneDrive\Desktop\students.csv",index=False)
            print("Data Save successfully")
        else:
            print("Data not save")
