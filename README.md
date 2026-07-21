**Student Management System**

A simple web app to manage student records — add, edit, search, and save data as CSV. Built with Streamlit and Pandas.

What it does


➕ Add new students (ID, Name, Age, Gender, Course, Email, Phone, Marks)
 Edit or delete records directly in a table .
 Search by ID, Name, or Course .
 Show the topper (highest marks) .
 Upload/download data as CSV .


**Requirements**

Python 3.8+
Streamlit
Pandas


How to run

bashgit clone https://github.com/Chetankumawat209/Student-Management.git
cd Student-Management
pip install -r requirements.txt
streamlit run app.py

Then open http://localhost:8501 in your browser.


Files
app.py — main app
student.py — add/edit/search/topper logic
file_manager.py — CSV upload/save logic

Deploy link:- https://ckstudent.streamlit.app/

Author

Chetan Kumawat 
