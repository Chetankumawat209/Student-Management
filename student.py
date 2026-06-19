from file_manager import file_handle
from tabulate import tabulate
import pandas as pd
import streamlit as st
from app import main




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
        self.df=pd.DataFrame()
        self.path=""
    
    def addStudent(self):
        self.df,self.path=file_handle()
        # st.write(self.path)
        # st.table(self.df)
        with st.form("addStudent"):
 
            ID=st.number_input("Enter student ID",value=0)
            
            Name=st.text_input("Enter Student name ")
            Age=st.number_input("Enter Student age ",value=0)
            
            Gender=st.selectbox("select gender",["Male","Female"],index=None)
            
            course=st.selectbox("Enter Student course ",["BCA","BA","B.Com,","BBA","B.tech"],index=None,placeholder="select course")
            
            Email=st.text_input("Enter Email ")
            
            Phone=st.number_input("Enter student phone number ",placeholder="Enter 10 digit",value=None,step=1)
            
            
            Marks=st.number_input("Enter student marks ")
            
            submit=st.form_submit_button("Add Student")
        
        new_df=pd.DataFrame({
            "Student ID":[ID],
            "Name":[Name],
            "Age":[Age],
            "Gender":[Gender],
            "Course":[course],
            "Email":[Email],
            "Phone Number":[Phone],
            "Marks":[Marks]
        })

        if submit==True:
            self.df=pd.concat((self.df,new_df),axis=0,ignore_index=True)
            st.table(self.df)
            
    def viewStudent(self):
        if self.df.empty:
            self.df, self.path = file_handle()
            st.table(self.df)
            # print(tabulate(self.df, headers=self.df.columns, tablefmt="grid"))
        
        elif not self.df.empty:
            st.table(self.df)
            # print(tabulate(self.df, headers=self.df.columns, tablefmt="grid"))
        else:
            st.write("No students found")


    def searchStudent(self):
        st.write("Which option do you choose to find a student?")
        lst=["Search by student ID","Search by phone number"]
        choice=st.selectbox("Choice",lst)   
        choice=lst.index(choice)+1

        if choice==1:
            stid=st.number_input("Enter student",value=None,step=1,placeholder="Enter ID of student")
            if self.df.empty:
                self.df,self.path=file_handle()
                st.table(self.df[self.df["Student ID"]==stid],file_handle=self.df.coumns)
                # print(tabulate(self.df[self.df['Student ID']==stid],headers=self.df.columns,tablefmt="grid"))
            else:
                # print(tabulate(self.df[self.df['Student ID']==stid],headers=self.df.columns,tablefmt="grid"))
                st.table(self.df[self.df["Student ID"]==stid],file_handle=self.df.coumns)


    def updateStudent(self):
        pass
    def deleteStudent(self):
        pass
    def topperStudent(self):
        pass

    def save(self):
        lst=["Save","Not save"]
        choice=st.selectbox("choice",lst)
        choice=lst.index(choice)+1
        # print("1 Save data")
        # print("2 Not save data")
        # choice=input("Enter your choice ")
        st.write(self.df)
        if choice ==1:
            self.df.to_csv(self.path,index=False)
            st.write("Data Save successfully")
        elif choice==2 :
            st.write("Data not save")
        else:
            st.write("you don't choice")
