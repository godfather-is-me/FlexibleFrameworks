import streamlit as st
import Authentication as A

def title():
    st.markdown("## Outcome \n ---")

def content():
    db = A.auth_DB()

    # Loop through templates and their data
    for collect in db.collections():
        st.write("The collection identifier is: ", collect.id)
        for doc in collect.stream():
            st.write("The contents are: ", doc.to_dict())
        st.markdown(" \n --- \n ")

def draw_all():
    title()
    content()