import streamlit as st
st.header("st.checkbox")
icecream = st.checkbox("Icecream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")
if icecream:
    st.write("Here is some ice cream 🍦")
if coffee:
    st.write("Here is some coffee ☕")
if cola:
    st.write("Here is some cola 🥤")