import random
from datetime import datetime, date, time

import streamlit as st
import pandas as pd
import numpy as np


def data_elements():
    st.markdown("""
    Documents: [Data elements](https://docs.streamlit.io/develop/api-reference/data)
    # Data elements
    
    When you're working with data, it is extremely valuable to visualize that data quickly, interactively, and from 
    multiple different angles. That's what Streamlit is actually built and optimized for.
    """)

    # Dataframes
    st.markdown("""
    ## Dataframes
    `st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, column_order=None, 
    column_config=None, key=None, on_select="ignore", selection_mode="multi-row")`
    
    **data** \n
    _(pandas.DataFrame, pandas.Series, pandas.Styler, pandas.Index, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, 
    snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table, Iterable, dict, or None)_
    """)
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df)

    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(
            np.random.randn(12, 5), columns=["a", "b", "c", "d", "e"]
        )

    event = st.dataframe(
        st.session_state.df,
        key="data",
        on_select="rerun",
        selection_mode=["multi-row", "multi-column"],
    )
    st.write(event.selection)

    st.markdown("""
    `element.add_rows(data=None, **kwargs)`
    """)
    df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    my_table = st.table(df1)
    df2 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    my_table.add_rows(df2)

    my_chart = st.line_chart(df1)
    my_chart.add_rows(df2)

    # Data editor
    st.markdown("""
    ## Data editor
    `st.data_editor(data, *, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, 
    column_config=None, num_rows="fixed", disabled=False, key=None, on_change=None, args=None, kwargs=None)`
    
    **data** \n
    _(pandas.DataFrame, pandas.Series, pandas.Styler, pandas.Index, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame,
    snowflake.snowpark.DataFrame, list, set, tuple, dict, or None)_
    """)
    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(df)
    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(df, num_rows="dynamic")
    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(
        df,
        column_config={
            "command": "Streamlit Command",
            "rating": st.column_config.NumberColumn(
                "Your rating",
                help="How much do you like this command (1-5)?",
                min_value=1,
                max_value=5,
                step=1,
                format="%d ⭐",
            ),
            "is_widget": "Widget ?",
        },
        disabled=["command", "is_widget"],
        hide_index=True,
    )
    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    # Column configuration
    st.markdown("""
    ## Column configuration
    ### Column
    `st.column_config.Column(label=None, *, width=None, help=None, disabled=None, required=None)`
    """)
    data_df = pd.DataFrame(
        {
            "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.Column(
                "Streamlit Widgets",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                required=True,
            )
        },
        hide_index=True,
        num_rows="dynamic",
    )

    st.markdown("""
    ### TextColumn
    `st.column_config.TextColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    max_chars=None, validate=None)`
    """)
    data_df = pd.DataFrame(
        {
            "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.TextColumn(
                "Widgets",
                help="Streamlit **widget** commands 🎈",
                default="st.",
                max_chars=50,
                validate="^st\.[a-z_]+$",
            )
        },
        hide_index=True,
    )

    st.markdown("""
    ### NumberColumn
    `st.column_config.NumberColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    format=None, min_value=None, max_value=None, step=None)`
    """)
    data_df = pd.DataFrame(
        {
            "price": [20, 950, 250, 500],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "price": st.column_config.NumberColumn(
                "Price (in USD)",
                help="The price of the product in USD",
                min_value=0,
                max_value=1000,
                step=1,
                format="$%d",
            )
        },
        hide_index=True,
    )

    st.markdown("""
    ### CheckboxColumn
    `st.column_config.CheckboxColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None)`
    """)
    data_df = pd.DataFrame(
        {
            "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
            "favorite": [True, False, False, True],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "favorite": st.column_config.CheckboxColumn(
                "Your favorite?",
                help="Select your **favorite** widgets",
                default=False,
            )
        },
        disabled=["widgets"],
        hide_index=True,
    )

    st.markdown("""
    ### SelectboxColumn
    `st.column_config.SelectboxColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    options=None)`
    """)
    data_df = pd.DataFrame(
        {
            "category": [
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
                "📊 Data Exploration",
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "category": st.column_config.SelectboxColumn(
                "App Category",
                help="The category of the app",
                width="medium",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                ],
                required=True,
            )
        },
        hide_index=True,
    )

    st.markdown("""
    ### DatetimeColumn
    `st.column_config.DatetimeColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    format=None, min_value=None, max_value=None, step=None, timezone=None)`
    """)
    data_df = pd.DataFrame(
        {
            "appointment": [
                datetime(2024, 2, 5, 12, 30),
                datetime(2023, 11, 10, 18, 0),
                datetime(2024, 3, 11, 20, 10),
                datetime(2023, 9, 12, 3, 0),
            ]
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.DatetimeColumn(
                "Appointment",
                min_value=datetime(2023, 6, 1),
                max_value=datetime(2025, 1, 1),
                format="D MMM YYYY, h:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### DateColumn
    `st.column_config.DateColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    format=None, min_value=None, max_value=None, step=None)`
    """)
    data_df = pd.DataFrame(
        {
            "birthday": [
                date(1980, 1, 1),
                date(1990, 5, 3),
                date(1974, 5, 19),
                date(2001, 8, 17),
            ]
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "birthday": st.column_config.DateColumn(
                "Birthday",
                min_value=date(1900, 1, 1),
                max_value=date(2005, 1, 1),
                format="DD.MM.YYYY",
                step=1,
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### TimeColumn
    `st.column_config.TimeColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    format=None, min_value=None, max_value=None, step=None)`
    """)
    data_df = pd.DataFrame(
        {
            "appointment": [
                time(12, 30),
                time(18, 0),
                time(9, 10),
                time(16, 25),
            ]
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.TimeColumn(
                "Appointment",
                min_value=time(8, 0, 0),
                max_value=time(19, 0, 0),
                format="hh:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### ListColumn
    `st.column_config.ListColumn(label=None, *, width=None, help=None)`
    """)
    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ListColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                width="medium",
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### LinkColumn
    `st.column_config.LinkColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, 
    max_chars=None, validate=None, display_text=None)`
    """)
    data_df = pd.DataFrame(
        {
            "apps": [
                "https://roadmap.streamlit.app",
                "https://extras.streamlit.app",
                "https://issues.streamlit.app",
                "https://30days.streamlit.app",
            ],
            "creator": [
                "https://github.com/streamlit",
                "https://github.com/arnaudmiribel",
                "https://github.com/streamlit",
                "https://github.com/streamlit",
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.LinkColumn(
                "Trending apps",
                help="The top trending Streamlit apps",
                validate="^https://[a-z]+\.streamlit\.app$",
                max_chars=100,
                display_text="https://(.*?)\.streamlit\.app"
            ),
            "creator": st.column_config.LinkColumn(
                "App Creator", display_text="Open profile"
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### ImageColumn
    `st.column_config.ImageColumn(label=None, *, width=None, help=None)`
    """)
    data_df = pd.DataFrame(
        {
            "apps": [
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
    )

    st.markdown("""
    ### AreaChartColumn
    `st.column_config.AreaChartColumn(label=None, *, width=None, help=None, y_min=None, y_max=None)`
    """)
    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.AreaChartColumn(
                "Sales (last 6 months)",
                width="medium",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### LineChartColumn
    ` st.column_config.LineChartColumn(label=None, *, width=None, help=None, y_min=None, y_max=None)`
    """)
    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.LineChartColumn(
                "Sales (last 6 months)",
                width="medium",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### BarChartColumn
    `st.column_config.BarChartColumn(label=None, *, width=None, help=None, y_min=None, y_max=None)`
    """)
    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.BarChartColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )

    st.markdown("""
    ### ProgressColumn
    `st.column_config.ProgressColumn(label=None, *, width=None, help=None, format=None, min_value=None, max_value=None)`
    """)
    data_df = pd.DataFrame(
        {
            "sales": [200, 550, 1000, 80],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ProgressColumn(
                "Sales volume",
                help="The sales volume in USD",
                format="$%f",
                min_value=0,
                max_value=1000,
            ),
        },
        hide_index=True,
    )

    # Static tables
    st.markdown("""
    ## Static tables
    `st.table(data=None)`
    """)
    df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    st.table(df)

    # Metrics
    st.markdown("""
    ## Metrics
    `st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")`
    """)
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    st.metric(label="Gas price", value=4, delta=-0.5,
              delta_color="inverse")
    st.metric(label="Active developers", value=123, delta=123,
              delta_color="off")

    # Dicts and Json
    st.markdown("""
    ## Dicts and Json
    `st.json(body, *, expanded=True)`
    """)
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })

    # Third-party components
    st.markdown("""
    ## Third-party components
    [Streamlit Extras](https://extras.streamlit.app) \n
    [Streamlit Aggrid](https://github.com/PablocFonseca/streamlit-aggrid) \n
    [Image Coordinates](https://github.com/blackary/streamlit-image-coordinates) \n
    [Plotly Events](https://github.com/null-jones/streamlit-plotly-events) \n
    [Streamlit Folium](https://github.com/randyzwitch/streamlit-folium) \n
    [Pandas Profiling](https://github.com/okld/streamlit-pandas-profiling) \n
    """)
