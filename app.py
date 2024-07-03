import streamlit as st

HORIZONTAL_RED = "static/images/aio_logo.png"

options = [HORIZONTAL_RED, HORIZONTAL_RED, HORIZONTAL_RED, HORIZONTAL_RED]
# sidebar_logo = st.selectbox("Sidebar logo", options, 0)
# main_body_logo = st.selectbox("Main body logo", options, 1)

pages = {
    "Your account": [
        st.Page("src/pages/home_page.py", title="HomePage"),
    ],
    "Notes": [
        st.Page("src/pages/docker.py", title="Docker"),
    ],
    "Data Analysis": [
        st.Page("src/pages/7_🏠_house.py", title="House"),
    ],
    "AI": [
        st.Page("src/pages/4_🖊️‍_AI.py", title="AI Tools"),
    ],
    "Demo": [
        st.Page("src/pages/api_reference.py", title="api_reference"),
        st.Page("src/pages/1_📈_Plotting_Demo.py", title="Plotting_Demo"),
        st.Page("src/pages/2_🌍_Mapping_Demo.py", title="Mapping_Demo"),
        st.Page("src/pages/3_📊_DataFrame_Demo.py", title="DataFrame_Demo"),
        st.Page("src/pages/5_db_test.py", title="db_test"),
        st.Page("src/pages/6_word.py", title="word"),
    ],
    "Playground": [
        st.Page("src/pages/playground.py", title="playground"),
    ]
}

# st.logo(sidebar_logo, icon_image=main_body_logo)
pg = st.navigation(pages)
pg.run()
