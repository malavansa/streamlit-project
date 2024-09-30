import streamlit as st
import sqlite3
from datetime import datetime


def create_form():
    st.write("Please fill this form")
    with st.form(key="Registration Form"):
        first_name = st.text_input("First Name: ", key="fname")
        last_name = st.text_input("Last Name: ", key="lname")
        dob = st.date_input("Birthday")
        email = st.text_input("Email: ", key="email")
        school = st.text_input("School: ", key="school")
        phone_number = st.text_input("Phone Number: ", max_chars=10, key="phone")
        submit = st.form_submit_button(label="Register")
    if submit == True:
        add_info(first_name, last_name, dob, email, school, phone_number)


def add_info(fname, lname, dob, email, school, phone):
    conn = sqlite3.connect("form.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
                   first_name TEXT,
                   last_name TEXT,
                   dob TEXT,
                   email TEXT,
                   school TEXT,
                   phone_number TEXT
                   )
    """
    )
    if all([fname, lname, dob, email, school, phone]):
        row = cursor.execute(
            "SELECT email FROM students WHERE email=?", (email,)
        ).fetchone()

        if row:
            user_name = row[0]
            if user_name == email:
                st.warning("User is already taken, please try with different email")
            else:
                cursor.execute(
                    """
                INSERT INTO students VALUES(?,?, ?,?,?,?)""",
                    (fname, lname, dob, email, school, phone),
                )
                conn.commit()
                conn.close()
                st.success("Student has been added to SQLite database")
                st.success("Your registration has been successful!")
        else:
            cursor.execute(
                """
                INSERT INTO students VALUES(?,?, ?,?,?,?)""",
                (fname, lname, dob, email, school, phone),
            )
            conn.commit()
            conn.close()
            st.success("Student has been added to SQLite database")
            st.success("Your registration has been successful!")
    else:
        st.error("please fill the form first")
    


st.write("# :green[CodeSpace]")

create_form()

