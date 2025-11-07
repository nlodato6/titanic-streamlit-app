import streamlit as st
from components.sidebar import render_sidebar

st.title("📈 Plots & Predictions")
st.write("Show charts and a simple model here.")

render_sidebar()