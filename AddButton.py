import streamlit as st
import T3

def title():
    st.markdown("## Add Button for Template 3 \n ---")

def content():
    option = st.radio(
        "Enter field you would like to enter",
        ("Text", "Number")
    )

    in_the_key = "Input field key"
    with st.form("Add button input"):
        input_field = None
        if option == "Text":
            input_field = st.text_input(in_the_key)
        elif option == "Number":
            input_field = st.number_input(in_the_key)
        else:
            pass

        submit = st.form_submit_button("Submit column")

        # Check if input field is filled
        if submit and input_field:
            submit_value(input_field, option)

def submit_value(input_field, type):
    value = None
    if type == "Text":
        value = st.text_input
    else:
        value = st.number_input
    T3.form_values[input_field] = [value, None]

def draw_all():
    title()
    content()