
import streamlit as st

from file_manager import empty_df, sidebar_data_loader, save_section
from student import add_student_form, editable_table, search_section, topper_section

st.set_page_config(page_title="Student Management System", page_icon="🎓", layout="wide")


def init_state():
    """Set up session_state the first time the app runs."""
    if "df" not in st.session_state:
        st.session_state.df = empty_df()
    if "source_filename" not in st.session_state:
        st.session_state.source_filename = None
    if "loaded_file_id" not in st.session_state:
        st.session_state.loaded_file_id = None


def main():
    st.title("Student Management System")

    init_state()
    state = st.session_state  # short alias passed into every function

    sidebar_data_loader(state)

    add_student_form(state)
    editable_table(state)

    c1, c2 = st.columns(2)
    with c1:
        search_section(state)
    with c2:
        topper_section(state)

    st.divider()
    save_section(state)


if __name__ == "__main__":
    main()
