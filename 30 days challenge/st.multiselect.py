import streamlit as st
st.header("st.multiselect")
colors = st.multiselect("Select the colors that you like",
               ["Red", "Blue", "Green", "Orange"],
               ["Red", "Green", "Blue"])
st.write(f"You selected {colors}")