import streamlit as st
import pandas as pd
import numpy as np
st.header("Line Chart")
data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(data)