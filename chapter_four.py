# Working with data

import streamlit as st
import pandas as pd

st.title("Customer Churn Data Analysis")

file=st.file_uploader("Upload CSV",type=['csv'])

if file:
    df=pd.read_csv(file)
    st.subheader('Data Preview')
    st.dataframe(df)

    # basic infos
    st.header('Basic info')
    st.write('Rows: ',df.shape[0])
    st.write('Columns:', df.shape[1])

    # select column
    colum= st.selectbox("Select columns:",df.columns)

    # show the value counts of column
    st.subheader('Value counts')
    st.write(df[colum].value_counts())

    #display stats summary
    if file:
        st.header("Statistical Summary")
        st.write(df.describe())

    #simple chart
    st.subheader("Bar chart")
    st.bar_chart(df[colum].value_counts())

