import student
import streamlit as st


def get_manager():
    if "student_manager" not in st.session_state:
        st.session_state.student_manager = student.StudentManager()
    return st.session_state.student_manager


def main():
    st.title("=====Welcome to Student management system ========")

    lst = ["Add Student", "View Students", "Search Student", "Update Students",
           "Delete Student", "Topper Student", "Save data and exit"]
    choice = st.selectbox("Choice what you want", lst, index=None, placeholder="Please select an option")
    if choice:
        choice = lst.index(choice) + 1

    obj = get_manager()

    match choice:
        case 1:
            obj.addStudent()
        case 2:
            obj.viewStudent()
        case 3:
            obj.searchStudent()
        case 4:
            obj.updateStudent()
        case 5:
            obj.deleteStudent()
        case 6:
            obj.topperStudent()
        case 7:
            obj.save()
            st.success("Save completed. You can choose another option or close the app.")
        case _:
            st.info("Please select an option")
            






if __name__=="__main__":
    main()
# st.title("hello")