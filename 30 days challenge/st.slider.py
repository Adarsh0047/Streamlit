import streamlit as st
from datetime import datetime, time
st.header("st.slider")
st.subheader("Slider")
age = st.slider("How old are you?",0,100,25)
st.write("I'm", age, "years old.")
st.subheader("Range Slider")
values = st.slider("Select a range of values",0.0,100.0,(25.0,75.0))
st.write("Difference",values[1]-values[0])
st.subheader("Time range slider")
appointment = st.slider("Schedule your appointment",
                        value=(time(11,45), time(1,00)))
# st.write(f"Your appointment is at{appointment[0].strftime(appointment[0])} to {appointment[1].strftime(appointment[1])}")
st.write(f"Your appointment is at {appointment}")

st.subheader("Datetime slider")
start_time = st.slider("When do you want to start?",
                       value=datetime(2020,1,1,9,30),
                       format="MM/DD/YY - hh:mm")
st.write("Start time:",start_time)
