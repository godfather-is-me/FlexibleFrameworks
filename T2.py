import datetime
import streamlit as st
import Authentication as A

from google.cloud import firestore

def title():
    st.markdown("## Template 2 \n ---")

def content():
    db = A.auth_DB()

    with st.form(key = "Form 2"):
        firstName = st.text_input("First name: ")
        lastName = st.text_input("Last name: ")
        studentNumber = st.text_input("Student number: ")
        DOB = st.date_input("Date of Birth: ")
        DOB = datetime.datetime(
            DOB.year,
            DOB.month,
            DOB.day
        )
        grade = st.text_input("Grade input")
        submit = st.form_submit_button("Submit form")

    # Check requirements function to be included
    if firstName and studentNumber and lastName and DOB and grade and submit:
        doc_ref = db.collection("Template 2").document(studentNumber)
        doc_ref.set({
            "First Name" : firstName,
            "Last Name" : lastName,
            "Student Number" : studentNumber,
            "Grade" : grade,
            "DOB" : DOB
        })
    

def draw_all():
    title()
    content()