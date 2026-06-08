import pandas as pd
from app import main

def file_handle():
    print("1 Already have")
    print("2 Not created have")
    mode=input("Enter your choice ")

    if mode=="1":
        path=input("Enter file path ")
        df=pd.read_csv(path)
        print("open successfully")
        return df

    elif mode =="2":
        path=r"C:\Users\cheta\OneDrive\Desktop\students.csv"
        columns=['student ID','Name','Age','Gender','Course','Email',"Phone Number","Marks"]
        df=pd.DataFrame(columns=columns)
        df.to_csv(path,index=False)
        print("create Successfully")
        return df
        
    else:
        print("Enter worng mode")
        main()