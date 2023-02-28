import streamlit as st
import pandas as pd
st.header("st.file_uploader")
st.subheader("Input Csv")
uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataframe")
    st.write(df.head())
    st.subheader("Describe")
    st.write(df.describe())
else:
    st.write("👆 Upload a File")