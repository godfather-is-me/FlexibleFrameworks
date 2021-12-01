import json
import streamlit as st

from google.cloud import firestore
from google.oauth2 import service_account

# Private key to NoSQL database loaded as a secret key
def auth_DB():
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)
    
    # Returns the db with required credentials
    return db