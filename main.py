import streamlit as st
from google.cloud import firestore

# pages
import T1
import T2
import T3
import Outcome
import AddButton

def auth():
    # Simple check to see if connection is made with database
    try:
        db = firestore.Client.from_service_account_json("../firestore-key.json")
    except:
        print("Authentication error")

def draw_sidebar():
    topics = [
        "Template 1",
        "Template 2",
        "Template 3",
        "Add button",
        "Outcome"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("", topics)

    if page == topics[0]:
        T1.draw_all()
    elif page == topics[1]:
        T2.draw_all()
    elif page == topics[2]:
        T3.draw_all()
    elif page == topics[3]:
        AddButton.draw_all()
    elif page == topics[4]:
        Outcome.draw_all()
    else:
        pass

# Side bar always drawn
def draw_main():
    draw_sidebar()
    auth()

# Main page call
draw_main()