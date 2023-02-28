import streamlit as st
st.header("st.secrets")
st.write(st.secrets["message"])
st.write("Password:",st.secrets["mypassword"])