import streamlit as st

from src.docker import docker_install, intro

page_names_to_funcs = {
    "—": intro.intro,
    "install (Engine)": docker_install.docker_install,
}

api_name = st.sidebar.selectbox("DOCKER", page_names_to_funcs.keys())
page_names_to_funcs[api_name]()
