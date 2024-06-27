import streamlit as st
from common.md_to_body import *


def intro():
    st.write("# Catalog 👋 👈")
    st.page_link("your_app.py", label="Home", icon="🏠")
