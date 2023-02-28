import streamlit as st
st.markdown(f'<p style="color:yellow;font-size:24px;">{"st.selectbox"}</p>', unsafe_allow_html=True)
color = st.selectbox("Select your favorite color",
             options=("Red", "Blue", "Green", "Orange"))
st.write(f"My favorite color is: {color}")