import streamlit as st

from src.docker import intro
from src.api_reference import write_and_magic
from src.api_reference import text_elements
from src.api_reference import data_elements
from src.api_reference import chart_elements
from src.api_reference import input_widgets
from src.api_reference import media_elements
from src.api_reference import layouts_and_containers
from src.api_reference import status_elements

page_names_to_funcs = {
    "—": intro.intro,
    "Write and magic": write_and_magic.write_and_magic,
    "Text elements": text_elements.text_elements,
    "Data elements": data_elements.data_elements,
    "Chart elements": chart_elements.chart_elements,
    "Input widgets": input_widgets.input_widgets,
    "Media elements": media_elements.media_elements,
    "Layouts and containers": layouts_and_containers.layouts_and_containers,
    "Status elements": status_elements.status_elements,
}

api_name = st.sidebar.selectbox("PAGE ELEMENTS", page_names_to_funcs.keys())
page_names_to_funcs[api_name]()
