import streamlit as st
from google.cloud import firestore

def title():
    st.markdown("## Outcome \n ---")

def content():
    db = firestore.Client.from_service_account_json("../firestore-key.json")

    # Loop through templates and their data
    for collect in db.collections():
        st.write("The collection identifier is: ", collect.id)
        for doc in collect.stream():
            st.write("The contents are: ", doc.to_dict())

def draw_all():
    title()
    content()