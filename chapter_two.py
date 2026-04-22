# widgets and inputs

# Mini Practice Task (do this)
'''
Build a small app:

Ask name
Ask age
Select favorite language
Show all outputs '''

import streamlit as st

name= st.text_input("What's your name?")

age= st.number_input("Whats's your age",min_value=15,max_value=25)

language= st.selectbox('Select your favourite language: ',["Python","C++","C#","Java","JavaScript"])

if name:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Favourite Language: {language}")
