import streamlit as st
st.header("st.button")
if st.button("Say Hello!"):
    st.write('Why! Hello There..')
else:
    st.write("GoodBye..")