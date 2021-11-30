import streamlit as st
from google.cloud import firestore

# pages
import T1
import Outcome

def auth():
    db = firestore.Client.from_service_account_json("../firestore-key.json")
    
    smth = """ doc_ref = db.collection("posts").document("Google")

    # Set a new document
    doc_ref = db.collection("posts").document("Apple")
    if not (doc_ref.get() is None):
        doc_ref.set({
            "title" : "Apple",
            "url" : "apple.com"
        })

    # Read all values
    posts_ref = db.collection("posts")
    for doc in posts_ref.stream():
        st.write("The id is: ", doc.id)
        st.write("The contents are: ", doc.to_dict()) """
    

def draw_sidebar():
    topics = [
        "Template 1",
        "Template 2",
        "Template 3",
        "Outcome"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("", topics)

    if page == topics[0]:
        T1.draw_all()
    elif page == topics[1]:
        pass
    elif page == topics[2]:
        pass
    elif page == topics[3]:
        Outcome.draw_all()
    else:
        pass

# Side bar always drawn
def draw_main():
    draw_sidebar()
    auth()

# Main page call
draw_main()