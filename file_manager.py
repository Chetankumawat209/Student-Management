

import os
import pandas as pd
import streamlit as st

COLUMNS = [
    "Student ID", "Name", "Age", "Gender",
    "Course", "Email", "Phone Number", "Marks",
]


def empty_df() -> pd.DataFrame:
    """Return a fresh, empty students table with the correct columns."""
    return pd.DataFrame(columns=COLUMNS)


def load_csv(uploaded_file) -> pd.DataFrame:
    """Read an uploaded CSV and make sure all expected columns exist."""
    df = pd.read_csv(uploaded_file)
    for col in COLUMNS:
        if col not in df.columns:
            df[col] = pd.NA
    return df[COLUMNS]


def default_save_path(filename: str) -> str:
    """Suggest Desktop/<filename> if a Desktop folder exists, else just the filename."""
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    if os.path.isdir(desktop):
        return os.path.join(desktop, filename)
    return filename


def sidebar_data_loader(state):
    """
    Sidebar widget: upload an existing CSV, or start fresh.
    `state` is st.session_state - we read/write df, source_filename,
    and loaded_file_id on it directly.
    """
    st.sidebar.header("Data")

    uploaded = st.sidebar.file_uploader("Upload a students CSV (optional)", type=["csv"])

    if uploaded is not None:
        # Only reload if this is a new/different file (avoid wiping edits on every rerun)
        file_id = (uploaded.name, uploaded.size)
        if state.loaded_file_id != file_id:
            state.df = load_csv(uploaded)
            state.source_filename = uploaded.name
            state.loaded_file_id = file_id
            st.sidebar.success(f"Loaded {uploaded.name} ({len(state.df)} rows)")
    else:
        if state.loaded_file_id is not None:
            # User removed the uploaded file from the widget
            state.loaded_file_id = None

    if st.sidebar.button("Start fresh (clear table)"):
        state.df = empty_df()
        state.source_filename = None
        state.loaded_file_id = None
        st.rerun()

    st.sidebar.caption(
        "No file uploaded yet? That's fine - just start adding students below, "
        "then choose where to save at the bottom of the page."
    )


def save_section(state):
    """
    Bottom-of-page widget: choose a save path, save to disk, or download.
    """
    st.subheader("Save")

    default_name = state.source_filename or "students.csv"
    suggested_path = default_save_path(default_name)

    save_path = st.text_input(
        "Save location on this computer (full path, including filename)",
        value=suggested_path,
        help="Example: C:/Users/YourName/Desktop/students.csv (Windows) "
             "or /Users/YourName/Desktop/students.csv (Mac/Linux). "
             "If you uploaded a file, this defaults to that file's name so you can overwrite it.",
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save to this location", use_container_width=True, type="primary"):
            if not save_path.strip():
                st.error("Please enter a file path first.")
            else:
                try:
                    folder = os.path.dirname(save_path)
                    if folder and not os.path.isdir(folder):
                        os.makedirs(folder, exist_ok=True)
                    state.df.to_csv(save_path, index=False)
                    st.success(f"Saved {len(state.df)} rows to:\n{save_path}")
                except Exception as e:
                    st.error(f"Could not save file: {e}")

    with col2:
        csv_bytes = state.df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV instead",
            data=csv_bytes,
            file_name=os.path.basename(save_path) or "students.csv",
            mime="text/csv",
            use_container_width=True,
        )
