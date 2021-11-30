import streamlit as st
import datetime

from google.cloud import firestore

# Strcutred as {input_field : (function call, value)}
form_values = {}

def title():
    st.markdown("## Template 3 \n ---")

def content():
    db = firestore.Client.from_service_account_json("../firestore-key.json")

    visual_form()
    # If requirement of all boxes satisified, upload
    upload(requirement(), db)
    

    
    
    

def visual_form():
    for input_field in form_values.keys():
        form_values[input_field][1] = form_values[input_field][0](input_field)

def requirement():
    # If requirements satisfied, submit
    flag = True
    for input_field in form_values.keys():
        if form_values[input_field][1] is None:
            flag = False
            break
    return flag

def upload(flag, db):
    if flag:
        # Unique reference used is student number
        if "Student Number" in form_values.keys():
            doc_ref = db.collection("Template 3").document(form_values["Student Number"])
            value_pairs = {}
            for input_field in form_values.keys():
                value_pairs[input_field] = form_values[input_field][1]
            doc_ref.set(value_pairs)


def draw_all():
    title()
    content()