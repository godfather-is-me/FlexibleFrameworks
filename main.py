import streamlit as st

import pandas as pd
import numpy as np

def draw_sidebar():
    topics = [
        "Template 1",
        "Template 2",
        "Template 3"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("", topics)

    if page == topics[0]:
        pass
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