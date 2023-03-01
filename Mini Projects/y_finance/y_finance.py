import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Web app to display stpck prices
Shown are the opening and closing prices of google
""")

ticker_symbol = "^NSEI"
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start="2010-5-31", end="2023-2-24")
st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume
""")
st.line_chart(ticker_df.Volume)