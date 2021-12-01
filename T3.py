import streamlit as st

from google.cloud import firestore

STUDENT_NUMBER_FIELD = "Student Number"
SUBMIT_FORM_FIELD = "Submit form"

# Strcutred as {<input field name> : [<function call>, <field value>]}
form_values = {}

def title():
    st.markdown("## Template 3 \n ---")

def content():
    db = firestore.Client.from_service_account_json("../firestore-key.json")

    # To student number and submit button to form
    fix_empty_form()
    # To display the current form with any entered values on the screen
    display_form()
    # If requirement of all boxes satisified, upload
    upload(requirement(), db)
    

def display_form():
    # Value = Function("Input field name")
    for input_field in form_values.keys():
        if input_field != SUBMIT_FORM_FIELD:
            form_values[input_field][1] = form_values[input_field][0](input_field)
    if form_values:
        input_field = SUBMIT_FORM_FIELD
        form_values[input_field][1] = form_values[input_field][0](input_field)

def requirement():
    # If requirements satisfied, submit
    flag = True
    for input_field in form_values.keys():
        if form_values[input_field][1] is None or form_values[input_field][1] == False:
            flag = False
            break
    return flag

def fix_empty_form():
    if not form_values:
        # If form empty, add the required components for submission
        # i.e Student Number and the Submit button
        form_values[STUDENT_NUMBER_FIELD] = [st.text_input, None]
        form_values[SUBMIT_FORM_FIELD] = [st.button, None]

def upload(flag, db):
    if flag:
        # Unique reference used is student number
        if STUDENT_NUMBER_FIELD in form_values.keys():
            st.markdown("Student number is " + form_values[STUDENT_NUMBER_FIELD][1])
            doc_ref = db.collection("Template 3").document(form_values[STUDENT_NUMBER_FIELD][1])
            value_pairs = {}
            for input_field in form_values.keys():
                value_pairs[input_field] = form_values[input_field][1]
            # Upload values
            doc_ref.set(value_pairs)

def draw_all():
    title()
    content()