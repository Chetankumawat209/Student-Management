import pandas as pd
import os
import streamlit as st

def file_handle():
    lst=["Open file","Create file"]
    mode=st.selectbox("choice file options",lst,index=None,placeholder="Choice file")
    if mode is None:
        st.stop()
    mode=lst.index(mode)+1
   

    if mode==1:
        path=st.file_uploader("select file")
        if path is None :
            st.stop()
     
        df=pd.read_csv(path)
        st.write("open successfully")
        if path:
            return df , path
        else:
            st.write(f"The file at {path} was not found. Try again")
            exit()

    elif mode ==2:
        path="C:/Users/cheta/OneDrive/Desktop/students.csv"
        columns=['student ID','Name','Age','Gender','Course','Email',"Phone Number","Marks"]
        df=pd.DataFrame(columns=columns)
        st.write("Create Successfully")
        return df ,path
        
    else:
        st.write("Enter wrong mode")
        return None, None

