# 🎓 Student Management System

A web-based **Student Management System** that lets you add, edit, search, and organize student records through an interactive interface — built with **Python** and **Streamlit**.

---

## 📌 Overview

This project provides a simple, no-database way to manage student records. Users can add new students, edit existing entries directly in a live table, search by ID/Name/Course, find the topper, and import or export the entire dataset as a CSV file — all from the browser.

## ✨ Features

- Add new student records through a simple form
- Editable data table — update, add, or delete rows directly
- Search students by ID, Name (partial match), or Course
- Instantly view the topper (highest marks)
- Upload an existing CSV to continue editing it
- Save or download the dataset as a CSV file

## 🛠️ Tech Stack

- **Python**
- **Pandas** – data handling and CSV I/O
- **Streamlit** – interactive web UI

## 📊 Data Fields

Each student record includes:
- Student ID, Name, Age, Gender
- Course (BCA / BA / B.Com / BBA / B.Tech)
- Email, Phone Number
- Marks (0–100)

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/Chetankumawat209/Student-Management.git
cd Student-Management

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

## 📁 Project Structure

```
├── app.py             # Streamlit application (entry point)
├── student.py         # Add / edit / search / topper logic
├── file_manager.py    # CSV upload, save, and download logic
├── requirements.txt   # Python dependencies
└── README.md
```

## 🙋‍♂️ Author

**Chetan Kumawat**
GitHub: [@Chetankumawat209](https://github.com/Chetankumawat209) · LinkedIn: [chetankumawat](https://linkedin.com/in/chetankumawat)

---
If you found this project useful, consider giving it a star!
