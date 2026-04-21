import streamlit as st

# basic 
st.title("my first app")
st.subheader("streamlit app")
st.text("hello world")

# selectbox
language= st.selectbox("Your Favourite Programming Language:",['Python','Java','JavaScript','C'])
