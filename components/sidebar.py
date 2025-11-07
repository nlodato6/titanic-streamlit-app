import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.image("media/logo.png", width=True)
        st.header("Navigation")
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/Data.py", label="Data Exploration", icon="📊")
        st.page_link("pages/Plots.py", label="Plots & Predictions", icon="📈")