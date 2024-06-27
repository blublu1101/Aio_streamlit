import streamlit as st
import numpy as np
import time


def layouts_and_containers():
    st.markdown("""
    Documentation: [Layouts and Containers](https://docs.streamlit.io/develop/api-reference/layout)
    
    # Layouts and Containers
    ## columns
    `st.columns(spec, *, gap="small")`
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    col1, col2 = st.columns([3, 1])
    data = np.random.randn(10, 1)
    col1.subheader("A wide column with a chart")
    col1.line_chart(data)
    col2.subheader("A narrow column with the data")
    col2.write(data)

    # container
    st.markdown("""
    ## container
    `st.container(*, height=None, border=None)`
    """)
    with st.container():
        st.write("This is inside the container")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))
    st.write("This is outside the container")

    container = st.container(border=True)
    container.write("This is inside the container")
    st.write("This is outside the container")
    # Now insert some more in the container
    container.write("This is inside too")

    row1 = st.columns(3)
    row2 = st.columns(3)
    for col in row1 + row2:
        tile = col.container(height=120)
        tile.title(":balloon:")

    long_text = "Lorem ipsum. " * 1000
    with st.container(height=300):
        st.markdown(long_text)

    # experimental_dialog
    st.markdown("""
    ## Dialog
    `st.experimental_dialog(title, *, width="small")`
    """)

    @st.experimental_dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

    # form
    st.markdown("""
    ## Form
    `st.form(key, clear_on_submit=False, *, border=True)`
    """)
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
    st.write("Outside the form")

    # empty
    st.markdown("""
    ## Empty
    `st.empty()`
    """)
    with st.empty():
        for seconds in range(3):
            st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
        st.write("✔️ 1 minute over!")

    # expander
    st.markdown("""
    ## Expander
    `st.expander(label, expanded=False)`
    """)

    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    with st.expander("See explanation"):
        st.write('''
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        ''')
        st.image("https://static.streamlit.io/examples/dice.jpg")

    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    expander = st.expander("See explanation")
    expander.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    expander.image("https://static.streamlit.io/examples/dice.jpg")

    # popover
    st.markdown("""
    ## Popover
    `st.popover(label, *, help=None, disabled=False, use_container_width=False)`
    """)
    with st.popover("Open popover"):
        st.markdown("Hello World 👋")
        name = st.text_input("What's your name?")
    st.write("Your name:", name)

    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)
    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")

    # sidebar
    st.markdown("""
    ## Sidebar
    `st.popover(label, *, help=None, disabled=False, use_container_width=False)`
    
    [st.sidebar](https://docs.streamlit.io/develop/api-reference/layout/st.sidebar)
    """)

    # tabs
    st.markdown("""
   ## Tabs
   `st.tabs(tabs)`
   """)
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = np.random.randn(10, 1)
    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)
    tab2.subheader("A tab with the data")
    tab2.write(data)

    # Third-party components
    st.markdown("""
   ## Third-party components
   [Streamlit Elements](https://github.com/okld/streamlit-elements) \n
   [Pydantic](https://github.com/lukasmasuch/streamlit-pydantic) \n
   [Streamlit Pages](https://github.com/blackary/st_pages) \n
   """)