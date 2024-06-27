import streamlit as st

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
        st.Page("src/pages/4_👩‍_AI.py", title="AI"),
    ],
    "Demo": [
        st.Page("src/pages/api_reference.py", title="api_reference"),
        st.Page("src/pages/1_📈_Plotting_Demo.py", title="Plotting_Demo"),
        st.Page("src/pages/2_🌍_Mapping_Demo.py", title="Mapping_Demo"),
        st.Page("src/pages/3_📊_DataFrame_Demo.py", title="DataFrame_Demo"),
        st.Page("src/pages/5_db_test.py", title="db_test"),
        st.Page("src/pages/6_word.py", title="word"),
    ],
}

pg = st.navigation(pages)
pg.run()
