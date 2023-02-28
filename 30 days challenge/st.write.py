import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

st.header("st.write")
st.write("Hello *World!* :sunglasses:")
st.write(1234)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
df2 = px.data.iris()
# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
fig = px.scatter(df2, x=df2.sepal_length, y=df2.sepal_width, color=df2.species, size=df2.petal_length)
st.plotly_chart(fig)
