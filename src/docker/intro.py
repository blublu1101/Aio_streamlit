import streamlit as st
from common.md_to_body import *


def intro():
    st.write("# Catalog 👋 👈")
    st.page_link("https://www.baidu.com", label="Docker install", icon="🏠")
    docker_install_page = st.Page("src/docker/docker_install.py", title="Docker")
    st.page_link(docker_install_page, label="Docker install", icon="🏠")
