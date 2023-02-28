import streamlit as st
st.set_page_config(layout="wide")
st.title("How to layout your app")
with st.expander("About this app"):
    st.write("This app shows the various ways on how you can layout your Streamlit app.")
    st.image("https://static.wixstatic.com/media/74de77_806e1e3a7b9f49869c14b5bad8bd279b~mv2_d_4896_3264_s_4_2.jpg/v1/fill/w_1220,h_813,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/74de77_806e1e3a7b9f49869c14b5bad8bd279b~mv2_d_4896_3264_s_4_2.jpg", width=200)
st.sidebar.header("Input")
name = st.sidebar.text_input("Enter your name")
emoji = st.sidebar.selectbox("Enter your favourite emoji",
                     ['','😄', '😆', '😊', '😍', '😴', '😕', '😱'])
food = st.sidebar.selectbox("What is your favourite food?",
                     ['','Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
col1, col2, col3 = st.columns(3)
with col1:
    if name:
        st.write(f"👋 Hello {name}")
    else:
        st.write("👈 Enter your name")
with col2:
    if emoji:
        st.write(f"Your favourite emoji is {emoji}")
    else:
        st.write("👈 Enter your favourite emoji")
with col3:
    if food:
        st.write(f"🍴 Your favourite food is {food}")
    else:
        st.write("👈 Enter your favourite food")