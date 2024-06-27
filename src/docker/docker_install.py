import streamlit as st

from common.md_to_body import *


def docker_install():
    res = import_md_file("docker install.md")
    st.markdown(res)
