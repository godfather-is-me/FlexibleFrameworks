import streamlit as st
from google.cloud import firestore

# pages
import T1

#def auth():
#    db = firestore.Client.from_service_account_json("firestore-key.json")
    
#    doc_ref = db.collection("template1").document("1")
#    doc = doc_ref.get()

#    st.write("The id is: ", doc.id)
#    st.write("The contents are: ", doc.to_dict())
    

def draw_sidebar():
    topics = [
        "Template 1",
        "Template 2",
        "Template 3"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("", topics)

    if page == topics[0]:
        T1.draw_all()
    elif page == topics[1]:
        pass
    elif page == topics[2]:
        pass
    else:
        pass

# Side bar always drawn
def draw_main():
    draw_sidebar()

# Main page call
draw_main()