import streamlit as st
import datetime

from google.cloud import firestore

def title():
    st.markdown("## Template 1 \n ---")

def content():
    db = firestore.Client.from_service_account_json("../firestore-key.json")

    with st.form(key = "Form 1"):
        firstName = st.text_input("First name: ")
        lastName = st.text_input("Last name: ")
        studentNumber = st.text_input("Student number: ")
        fatherName = st.text_input("Father name")
        DOB = st.date_input("Date of Birth: ")
        DOB = datetime.datetime(
            DOB.year,
            DOB.month,
            DOB.day
        )
        submit = st.form_submit_button("Submit form")

    # Check requirements function to be included
    if firstName and studentNumber and lastName and DOB and submit:
        doc_ref = db.collection("Template 1").document(studentNumber)
        doc_ref.set({
            "First Name" : firstName,
            "Last Name" : lastName,
            "Student Number" : studentNumber,
            "DOB" : DOB,
            "Father name" : fatherName
        })


def draw_all():
    title()
    content()