import student
print(2)
print("=====Wellcome to Student management system ========")
# print("chetan")
def main ():
    print(3)
    while True:
       
        print("""
1. Add Student
2. View Students
3. Search Student
4. Update Students
5. Delete Student
6. Sort Students
7. Topper Student
8. Statistics Students
9. Exit Student
                            
""")
        obj=student.StudentManager()
        choice=input("Enter your choice")

        match choice:
            case "1":
                # obj()
                obj.addStudent()
                
                obj.save()
            case "2":
                obj.viewStudent()
            case "3":
                obj.seachStudent()
            case "4":
                obj.updateStudent()
            case "5":
                obj.deleteStudent()
            case "6":
                obj.sortStudent()
            case "7":
                obj.topperStudent()
            case "8":
                obj.studentStatistics()
            case "9":
                break
            case _:
                print("Wrong choice")
                break






if __name__=="__main__":
    print(1)
    main()