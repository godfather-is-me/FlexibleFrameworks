import streamlit as st


def title():
    st.markdown("## Template 1 \n\n ---")

def content():
    if st.button('Balloons?'):
        st.balloons()


def draw_all():
    title()
    content()