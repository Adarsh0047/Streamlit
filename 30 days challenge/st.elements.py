import streamlit as st
import json
from pathlib import Path
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo
st.set_page_config("wide")
with st.sidebar:
    st.title("📅 Day 27")
    st.write("Build draggable elements")
    st.write("---")
    media_url = st.text_input("Enter URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()
layout = [
    dashboard.Item("editor", 0,0,6,3),
    dashboard.Item("chart", 6,0,6,3),
    dashboard.Item("media", 0,2,12,4)
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        afasf=22