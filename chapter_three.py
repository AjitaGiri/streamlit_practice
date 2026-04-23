#Layouts and styling

import streamlit as st

st.set_page_config(page_title='My App',layout='wide')

#Sidebar
st.sidebar.title('Input Section')
name=st.sidebar.text_input("Name")
age=st.sidebar.number_input("Age",15,25)
language=st.sidebar.selectbox('Language',['Python','C','C++','C#','Java','JavaScript'])

#main UI
st.title('User Dashboard')
st.divider()

if name:
    col1,col2,col3=st.columns(3)
    with col1:
        st.metric("Name: ", name)
    
    with col2:
        st.metric("Age: ",age)
    
    with col3:
        st.metric("Language: ",language)
