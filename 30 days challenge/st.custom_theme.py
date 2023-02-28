import streamlit as st
st.header("Customizing themes")
st.write("Code for the comfig.toml file:")
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
number = st.sidebar.slider("Select a number:",0,15,5)
st.write(f"The number that you have selected is {number}")