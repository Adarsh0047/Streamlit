import streamlit as st
st.header("st.query.get_query_params()")
with st.expander("About this app"):
    st.write("This app is used to demonstrate `get_query_params` function")
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Adarsh&surname=S`
after the base URL `http://localhost:8501`
such that it becomes 
`http://localhost:8501/?name=Adarsh&surname=S`
''')
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())

st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['name'][0]
surname = st.experimental_get_query_params()['surname'][0]
st.write(f"Hello {firstname} {surname}!")
