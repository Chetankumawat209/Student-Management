"""
student.py
-----------
Everything about students lives here:
- add_student_form():  the "Add a new student" form
- editable_table():    View + Update + Delete, all in one table
- search_section():    search by ID / Name / Course
- topper_section():    highest-marks student
"""

import pandas as pd
import streamlit as st

COURSES = ["BCA", "BA", "B.Com", "BBA", "B.Tech"]
GENDERS = ["Male", "Female", "Other"]


# --------------------------------------------------------------------------
# Add
# --------------------------------------------------------------------------

def add_student_form(state):
    with st.expander("➕ Add a new student", expanded=state.df.empty):
        with st.form("add_student_form", clear_on_submit=True):
            c1, c2, c3 = st.columns(3)
            with c1:
                sid = st.number_input("Student ID", min_value=0, step=1, value=0)
                age = st.number_input("Age", min_value=0, step=1, value=18)
            with c2:
                name = st.text_input("Name")
                gender = st.selectbox("Gender", GENDERS, index=None, placeholder="Select gender")
            with c3:
                course = st.selectbox("Course", COURSES, index=None, placeholder="Select course")
                marks = st.number_input("Marks", min_value=0.0, max_value=100.0, step=0.5, value=0.0)

            c4, c5 = st.columns(2)
            with c4:
                email = st.text_input("Email")
            with c5:
                phone = st.text_input("Phone Number")

            submitted = st.form_submit_button("Add Student", use_container_width=True)

            if submitted:
                _handle_add(state, sid, name, age, gender, course, email, phone, marks)


def _handle_add(state, sid, name, age, gender, course, email, phone, marks):
    if not name.strip():
        st.warning("Please enter a name before adding the student.")
        return

    if sid in state.df["Student ID"].values:
        st.warning(
            f"Student ID {sid} already exists. Use a different ID, "
            f"or edit that row directly in the table below."
        )
        return

    new_row = pd.DataFrame([{
        "Student ID": sid,
        "Name": name.strip(),
        "Age": age,
        "Gender": gender,
        "Course": course,
        "Email": email.strip(),
        "Phone Number": phone.strip(),
        "Marks": marks,
    }])
    state.df = pd.concat([state.df, new_row], ignore_index=True)
    st.success(f"Added {name.strip()} (ID {sid}).")


# --------------------------------------------------------------------------
# View + Update + Delete (one editable table)
# --------------------------------------------------------------------------

def editable_table(state):
    st.subheader("📋 Students")

    if state.df.empty:
        st.info("No students yet. Add one above, or upload a CSV from the sidebar.")
        return

    st.caption(
        "Edit any cell directly. Check the box on the left of a row and press "
        "**Delete** (trash icon) to remove it. Use the row at the bottom to add a row here too."
    )

    edited_df = st.data_editor(
        state.df,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="student_editor",
        column_config={
            "Student ID": st.column_config.NumberColumn(step=1),
            "Age": st.column_config.NumberColumn(step=1),
            "Gender": st.column_config.SelectboxColumn(options=GENDERS),
            "Course": st.column_config.SelectboxColumn(options=COURSES),
            "Marks": st.column_config.NumberColumn(step=0.5, min_value=0, max_value=100),
        },
    )
    state.df = edited_df


# --------------------------------------------------------------------------
# Search
# --------------------------------------------------------------------------

def search_section(state):
    df = state.df
    if df.empty:
        return

    with st.expander("🔎 Search students"):
        mode = st.radio(
            "Search by", ["Student ID", "Name", "Course"],
            horizontal=True, key="search_mode",
        )

        if mode == "Student ID":
            sid = st.number_input("Enter Student ID", min_value=0, step=1, key="search_sid")
            if st.button("Search", key="search_btn_id"):
                result = df[df["Student ID"] == sid]
                _show_search_result(result)

        elif mode == "Name":
            name_q = st.text_input("Enter name (or part of it)", key="search_name")
            if st.button("Search", key="search_btn_name"):
                result = df[df["Name"].astype(str).str.contains(name_q, case=False, na=False)]
                _show_search_result(result)

        else:
            course_q = st.selectbox("Select course", COURSES, index=None, key="search_course")
            if st.button("Search", key="search_btn_course"):
                result = df[df["Course"] == course_q]
                _show_search_result(result)


def _show_search_result(result: pd.DataFrame):
    if result.empty:
        st.warning("No matching student found.")
    else:
        st.table(result.reset_index(drop=True))


# --------------------------------------------------------------------------
# Topper
# --------------------------------------------------------------------------

def topper_section(state):
    df = state.df
    if df.empty:
        return

    with st.expander("🏆 Topper student"):
        marks_numeric = pd.to_numeric(df["Marks"], errors="coerce")
        if marks_numeric.notna().any():
            top_idx = marks_numeric.idxmax()
            st.table(df.loc[[top_idx]].reset_index(drop=True))
        else:
            st.info("No marks recorded yet.")
