#app.py

import streamlit as st

st.set_page_config(page_title="Titanic App", page_icon="🛳️", layout="wide")

st.sidebar.image(image="media/logo.png")

def Home():
    st.title("Titanic App Streamlit demo")
    st.image("media/titanic.png")
    st.write("Use the left sidebar to switch pages.")

pg = st.navigation([Home,"pagehandler/Data.py", "pagehandler/Plots.py"], position="sidebar", expanded=False)
pg.run()


