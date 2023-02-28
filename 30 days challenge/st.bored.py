import streamlit as st
import requests
st.title("Bored API ⚡")
st.sidebar.header("Input")
activity_type = st.sidebar.selectbox("Select an activity type",
                                     ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
suggested_activity_url =  f'http://www.boredapi.com/api/activity?type={activity_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
col1, col2 = st.columns(2)
with col1:
    with st.expander("About this app"):
        st.write("Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.")
with col2:
    with st.expander("JSON data"):
        st.write(suggested_activity)   

st.header("Suggested activity")
st.info(suggested_activity['activity'])
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Number of participants", value=suggested_activity['participants'], delta="")
with col2:
    st.metric(label="Type of activity", value=suggested_activity["type"].capitalize(), delta="")
with col3:
    st.metric(label="Price", value=suggested_activity['price'], delta="")