import streamlit as st
from components.sidebar import render_sidebar

st.set_page_config(page_title="Titanic App", page_icon="🛳️", layout="wide")
st.title("Titanic App Streamlit demo")
st.image("media/titanic.png")
st.write("Use the left sidebar to switch pages.")

render_sidebar()


