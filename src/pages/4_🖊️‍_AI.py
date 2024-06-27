import streamlit as st

from src.ai import home, coze, kimi

page_names_to_funcs = {
    "Home": home.home,
    "Coze": coze.coze,
    "Kimi": kimi.kimi
}

api_name = st.sidebar.selectbox("AI", page_names_to_funcs.keys())
page_names_to_funcs[api_name]()
