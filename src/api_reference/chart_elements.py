import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import graphviz
# import plotly.figure_factory as ff
# import plotly.express as px
import pydeck as pdk


def chart_elements():
    st.markdown("""
    Documentation: [Chart elements](https://docs.streamlit.io/develop/api-reference/charts)
    
    ## Area Chart
    `st.area_chart(data=None, *, x=None, y=None, color=None, width=None, height=None, use_container_width=True)`
    """)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )
    st.area_chart(chart_data, x="col1", y="col2", color="col3")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    st.area_chart(
        chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
    )

    # Bar Chart
    st.markdown("""
    ## Bar Chart
    `st.bar_chart(data=None, *, x=None, y=None, color=None, width=None, height=None, use_container_width=True)`
    """)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

    chart_data = pd.DataFrame(
        {
            "col1": list(range(20)) * 3,
            "col2": np.random.randn(60),
            "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
        }
    )
    st.bar_chart(chart_data, x="col1", y="col2", color="col3")

    chart_data = pd.DataFrame(
        {"col1": list(range(20)), "col2": np.random.randn(20), "col3": np.random.randn(20)}
    )
    st.bar_chart(
        chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
    )

    # line_chart
    st.markdown("""
    ## Line Chart
    `st.line_chart(data=None, *, x=None, y=None, color=None, width=None, height=None, use_container_width=True)`
    """)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )
    st.line_chart(chart_data, x="col1", y="col2", color="col3")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    st.line_chart(
        chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
    )

    # map
    st.markdown("""
    ## Map
    `st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)`
    """)
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(df)

    st.map(df, size=20, color='#0044ff')

    df = pd.DataFrame({
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    })
    st.map(df,
           latitude='col1',
           longitude='col2',
           size='col3',
           color='col4')

    # scatter_chart
    st.markdown("""
    ## Scatter Chart
    `st.scatter_chart(data=None, *, x=None, y=None, color=None, size=None, width=None, height=None, use_container_width=True)`
    """)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.scatter_chart(chart_data)

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
    st.scatter_chart(
        chart_data,
        x='col1',
        y='col2',
        color='col4',
        size='col3',
    )

    chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"])
    st.scatter_chart(
        chart_data,
        x='col1',
        y=['col2', 'col3'],
        size='col4',
        color=['#FF0000', '#0000FF'],  # Optional
    )

    # altair_chart
    st.markdown("""
    ## Altair Chart
    `st.altair_chart(altair_chart, *, use_container_width=False, theme="streamlit", key=None, on_select="ignore", 
    selection_mode=None)`
    """)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    c = (
        alt.Chart(chart_data)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )
    st.altair_chart(c, use_container_width=True)

    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame(
            np.random.randn(20, 3), columns=["a", "b", "c"]
        )
    df = st.session_state.data
    point_selector = alt.selection_point("point_selection")
    interval_selector = alt.selection_interval("interval_selection")
    chart = (
        alt.Chart(df)
        .mark_circle()
        .encode(
            x="a",
            y="b",
            size="c",
            color="c",
            tooltip=["a", "b", "c"],
            fillOpacity=alt.condition(point_selector, alt.value(1), alt.value(0.3)),
        )
        .add_params(point_selector, interval_selector)
    )
    event = st.altair_chart(chart, key="alt_chart", on_select="rerun")
    st.write(event)

    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame(
            np.random.randn(20, 3), columns=["a", "b", "c"]
        )
    spec = {
        "mark": {"type": "circle", "tooltip": True},
        "params": [
            {"name": "interval_selection", "select": "interval"},
            {"name": "point_selection", "select": "point"},
        ],
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
            "fillOpacity": {
                "condition": {"param": "point_selection", "value": 1},
                "value": 0.3,
            },
        },
    }
    event = st.vega_lite_chart(st.session_state.data, spec, key="vega_chart", on_select="rerun")
    st.write(event)

    # graphviz_chart
    st.markdown("""
    ## Graphviz Chart
    `st.graphviz_chart(figure_or_dot, use_container_width=False)`
    """)
    graph = graphviz.Digraph()
    graph.edge('run', 'intr')
    graph.edge('intr', 'runbl')
    graph.edge('runbl', 'run')
    graph.edge('run', 'kernel')
    graph.edge('kernel', 'zombie')
    graph.edge('kernel', 'sleep')
    graph.edge('kernel', 'runmem')
    graph.edge('sleep', 'swap')
    graph.edge('swap', 'runswap')
    graph.edge('runswap', 'new')
    graph.edge('runswap', 'runmem')
    graph.edge('new', 'runmem')
    graph.edge('sleep', 'runmem')
    st.graphviz_chart(graph)

    st.graphviz_chart('''
        digraph {
            run -> intr
            intr -> runbl
            runbl -> run
            run -> kernel
            kernel -> zombie
            kernel -> sleep
            kernel -> runmem
            sleep -> swap
            swap -> runswap
            runswap -> new
            runswap -> runmem
            new -> runmem
            sleep -> runmem
        }
    ''')

    # plotly_chart
    # st.markdown("""
    # ## Plotly Chart
    # `st.plotly_chart(figure_or_data, use_container_width=False, *, theme="streamlit", key=None, on_select="ignore",
    # selection_mode=('points', 'box', 'lasso'), **kwargs)`
    # """)
    # # Add histogram data
    # x1 = np.random.randn(200) - 2
    # x2 = np.random.randn(200)
    # x3 = np.random.randn(200) + 2
    # # Group data together
    # hist_data = [x1, x2, x3]
    # group_labels = ['Group 1', 'Group 2', 'Group 3']
    # # Create distplot with custom bin_size
    # fig = ff.create_distplot(
    #     hist_data, group_labels, bin_size=[.1, .25, .5])
    # # Plot!
    # st.plotly_chart(fig, use_container_width=True)
    #
    # df = px.data.iris()  # iris is a pandas DataFrame
    # fig = px.scatter(df, x="sepal_width", y="sepal_length")
    # event = st.plotly_chart(fig, key="iris", on_select="rerun")
    # st.write(event)
    #
    # df = px.data.gapminder()
    # fig = px.scatter(
    #     df.query("year==2007"),
    #     x="gdpPercap",
    #     y="lifeExp",
    #     size="pop",
    #     color="continent",
    #     hover_name="country",
    #     log_x=True,
    #     size_max=60,
    # )
    # tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    # with tab1:
    #     # Use the Streamlit theme.
    #     # This is the default. So you can also omit the theme argument.
    #     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    # with tab2:
    #     # Use the native Plotly theme.
    #     st.plotly_chart(fig, theme=None, use_container_width=True)

    # pydeck_chart
    st.markdown("""
    ## Pydeck Chart
    `st.pydeck_chart(pydeck_obj=None, use_container_width=False)`
    """)
    chart_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=chart_data,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

    # vega_lite_chart
    st.markdown("""
    ## Vega Lite Chart
    `st.vega_lite_chart(data=None, spec=None, *, use_container_width=False, theme="streamlit", key=None, 
    on_select="ignore", selection_mode=None, **kwargs)`
    """)
    chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
    st.vega_lite_chart(
        chart_data,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "a", "type": "quantitative"},
                "y": {"field": "b", "type": "quantitative"},
                "size": {"field": "c", "type": "quantitative"},
                "color": {"field": "c", "type": "quantitative"},
            },
        },
    )

    st.markdown("""
    ## Third-party components
    [Echarts](https://github.com/andfanilo/streamlit-echarts) \n
    [Streamlit Agraph](https://github.com/ChrisDelClea/streamlit-agraph) \n
    [Streamlit Extras](https://extras.streamlit.app/) \n
    [HiPlot](https://github.com/facebookresearch/hiplot) \n
    [Spacy-Streamlit](https://github.com/explosion/spacy-streamlit) \n
    [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie) \n
    [Plost](https://github.com/tvst/plost) \n
    [Stream Folium](https://github.com/randyzwitch/streamlit-folium) \n
    [Plotly Events](https://github.com/null-jones/streamlit-plotly-events) \n
    """)
