import streamlit as st
import time
st.header("st.progress")
with st.expander("About this app"):
    st.write("This app is used for demonstrating progress bar")
mybar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.05)
    mybar.progress(percent_complete + 1)
st.balloons()