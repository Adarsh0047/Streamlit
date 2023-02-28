import streamlit as st
st.title("st.form")
st.header("Example of object notation form")
st.subheader("Coffee Machine")
form = st.form("my_form1")
form.subheader("**Order your coffee**")
coffee_bean_val = form.selectbox("Coffee Bean", 
               ['Arabica', 'Robusta'])
coffee_roast_val = form.selectbox("Coffee Roast",
               ["Light", "Medium", "Dark"])
brewing_val = form.selectbox("Brewing Method",
               ["Aeropress","Drip","French Press","Moka Pot","Siphon"])
serving_type_val = form.selectbox("Serving Format",
               ["Hot", "Iced", "Frappe"])
milk_val = form.select_slider("Milk Intesity",["None","Low","Medium","High"])
owncup_val = form.checkbox("Select your own cup")
submitted = form.form_submit_button("Order")

if submitted:   
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')

st.header("Example of using `with` notation")
with st.form("form_2"):
    selected_val = st.slider("Select a value")
    submitted = st.form_submit_button("Submit")
if submitted:
    st.write(f"You have selected the value {selected_val}")