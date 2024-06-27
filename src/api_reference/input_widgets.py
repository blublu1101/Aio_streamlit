from datetime import time, datetime, date
from io import StringIO

import streamlit as st
import pandas as pd
import numpy as np


def input_widgets():
    st.markdown("""
    Documentation: [Input widgets](https://docs.streamlit.io/develop/api-reference/widgets) 
    
    # Input widgets
    With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs,
    and more.
    
    ## Button 
    `st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, 
    use_container_width=False)`
    """)
    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

    st.markdown("""
    [Featured videos](https://youtu.be/JSeQSnGovSE?list=TLGGcen3xq_FouUxMzA2MjAyNA) \n
    [Featured videos](https://youtu.be/EnXJBsCIl_A?list=TLGGEz3dvFMP4skxMzA2MjAyNA) \n
    """)

    # download_button
    st.markdown("""
    ## Download Button
    `st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, 
    kwargs=None, *, type="secondary", disabled=False, use_container_width=False)`
    """)

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    my_large_df = pd.DataFrame({"x": range(1000), "y": range(1000)})
    csv = convert_df(my_large_df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="large_df.csv",
        mime="text/csv",
    )

    text_contents = '''This is some text'''
    st.download_button("Download some text", text_contents)

    binary_contents = b"example content"
    # Defaults to "application/octet-stream"
    st.download_button("Download binary file", binary_contents)

    with open("static/images/bsh_logo.jpg", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )

    # form_submit_button
    st.markdown("""
    ## Form Submit Button
    `st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, 
    kwargs=None, *, type="secondary", disabled=False, use_container_width=False)`
    
    Display a form submit button. \n
    When this button is clicked, all widget values inside the form will be sent to Streamlit in a batch. \n
    Every form must have a form_submit_button. A form_submit_button cannot exist outside a form. \n
    
    [For more information about forms, check out](https://blog.streamlit.io/introducing-submit-button-and-forms/)
    """)
    with st.form(key='my_form'):
        text_input = st.text_input(label='Enter some text')
        submit_button = st.form_submit_button(label='Submit')
    st.write(text_input)
    st.write(submit_button)

    form = st.form(key='my-form')
    name = form.text_input('Enter your name')
    submit = form.form_submit_button('Submit')
    st.write('Press submit to have your name printed below')
    if submit:
        st.write(f'hello {name}')

    # experimental_fragment
    st.markdown("""
    ### experimental_fragment
    
    `st.experimental_fragment(func=None, *, run_every=None)`
    """)
    if "script_runs" not in st.session_state:
        st.session_state.script_runs = 0
        st.session_state.fragment_runs = 0

    @st.experimental_fragment
    def fragment():
        st.session_state.fragment_runs += 1
        st.button("Rerun fragment")
        st.write(f"Fragment says it ran {st.session_state.fragment_runs} times.")

    st.session_state.script_runs += 1
    fragment()
    st.button("Rerun full script")
    st.write(f"Full script says it ran {st.session_state.script_runs} times.")
    st.write(f"Full script sees that fragment ran {st.session_state.fragment_runs} times.")

    if "clicks" not in st.session_state:
        st.session_state.clicks = 0

    @st.experimental_fragment
    def count_to_five():
        if st.button("Plus one!"):
            st.session_state.clicks += 1
            if st.session_state.clicks % 5 == 0:
                st.rerun()
        return

    count_to_five()
    st.header(f"Multiples of five clicks: {st.session_state.clicks // 5}")

    if st.button("Check click count"):
        st.toast(f"## Total clicks: {st.session_state.clicks}")

    # rerun
    st.markdown("""
    ### rerun

    `st.rerun()`
    """)
    if "value" not in st.session_state:
        st.session_state.value = "Title"
    ##### Option using st.rerun #####
    st.header(st.session_state.value)
    if st.button("Foo"):
        st.session_state.value = "Foo"
        st.rerun()

    st.header(st.session_state.value)

    def update_value():
        st.session_state.value = "Bar"

    st.button("Bar", on_click=update_value)

    container = st.container()

    if st.button("Baz"):
        st.session_state.value = "Baz"

    container.header(st.session_state.value)

    # stop
    st.markdown("""
    ### stop

    `st.stop()`
    """)
    name = st.text_input('Name')
    if not name:
        st.warning('Please input a name. 输入后先手后面内容')
        st.stop()
    st.success('Thank you for inputting a name.')

    # link_button
    st.markdown("""
    ## Link Button
    `st.link_button(label, url, *, help=None, type="secondary", disabled=False, use_container_width=False)`
    """)
    st.link_button("Go to gallery", "https://streamlit.io/gallery")

    # page_link
    st.markdown("""
    ## Page Link
    `st.page_link(page, *, label=None, icon=None, help=None, disabled=False, use_container_width=None)`
    """)
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages1/5_db_test.py", label="Page 1", icon="1️⃣")
    st.page_link("pages1/6_word.py", label="Page 2", icon="2️⃣", disabled=True)
    st.page_link("http://www.google.com", label="Google", icon="🌎")

    # checkbox
    st.markdown("""
    ## Checkbox
    `st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, 
    label_visibility="visible")`
    """)
    agree = st.checkbox("I agree")
    if agree:
        st.write("Great!")

    # color_picker
    st.markdown("""
    ## Color Picker
    `st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, 
    label_visibility="visible")`
    """)
    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)

    # multiselect
    st.markdown("""
    ## Multiselect
    `st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, 
    on_change=None, args=None, kwargs=None, *, max_selections=None, placeholder="Choose an option", disabled=False, 
    label_visibility="visible")`
    """)
    options = st.multiselect(
        "What are your favorite colors",
        ["Green", "Yellow", "Red", "Blue"],
        ["Yellow", "Red"])
    st.write("You selected:", options)

    # radio
    st.markdown("""
    ## Radio
    `st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, 
    args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")`
    """)
    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions=["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
    if genre == ":rainbow[Comedy]":
        st.write("You selected comedy.")
    else:
        st.write("You didn't select comedy.")

    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        index=None,
    )
    st.write("You selected:", genre)

    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
        st.session_state.horizontal = False
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Disable radio widget", key="disabled")
        st.checkbox("Orient radio options horizontally", key="horizontal")
    with col2:
        st.radio(
            "Set label visibility 👇",
            ["visible", "hidden", "collapsed"],
            key="visibility",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            horizontal=st.session_state.horizontal,
        )

    # selectbox
    st.markdown("""
    ## Selectbox
    `st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, 
    args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")`
    """)
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"))
    st.write("You selected:", option)

    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        index=None,
        placeholder="Select contact method...",
    )
    st.write("You selected:", option)

    # select_slider
    st.markdown("""
    ## Select Slider
    `st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, 
    on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")`
    """)
    color = st.select_slider(
        "Select a color of the rainbow",
        options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
    st.write("My favorite color is", color)

    start_color, end_color = st.select_slider(
        "Select a range of color wavelength",
        options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
        value=("red", "blue"))
    st.write("You selected wavelengths between", start_color, "and", end_color)

    # toggle
    st.markdown("""
    ## Toggle
    `st.toggle(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, 
    label_visibility="visible")`
    """)
    on = st.toggle("Activate feature")
    if on:
        st.write("Feature activated!")

    # number_input
    st.markdown("""
    ## Number Input
    `st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, 
    on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")`
    """)
    number = st.number_input("Insert a number")
    st.write("The current number is ", number)

    number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
    st.write("The current number is ", number)

    # slider
    st.markdown("""
    ## Slider
    `st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, 
    on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")`
    """)
    age = st.slider("How old are you?", 0, 130, 25)
    st.write("I'm ", age, "years old")

    values = st.slider(
        "Select a range of values",
        0.0, 100.0, (25.0, 75.0))
    st.write("Values:", values)

    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)

    # date_input
    st.markdown("""
    ## Date Input
    `st.date_input(label, value="default_value_today", min_value=None, max_value=None, key=None, help=None, 
    on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible")`
    """)
    d = st.date_input("When's your birthday", datetime(2024, 6, 14))
    st.write("Your birthday is:", d)

    today = datetime.now()
    next_year = today.year + 1
    jan_1 = date(next_year, 1, 1)
    dec_31 = date(next_year, 12, 31)
    d = st.date_input(
        "Select your vacation for next year",
        (jan_1, date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
    st.write(d)

    d = st.date_input("When's your birthday", value=None)
    st.write("Your birthday is:", d)

    # chat_input
    st.markdown("""
    ## Chat Input
    `st.chat_input(placeholder="Your message", *, key=None, max_chars=None, disabled=False, on_submit=None, args=None, 
    kwargs=None)`
    """)
    # prompt1 = st.chat_input("Say something")
    # if prompt1:
    #     st.write(f"User has sent the following prompt: {prompt1}")

    # with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")

    # chat_message
    st.markdown("""
    ## Chat Message
    `st.chat_message(name, *, avatar=None)`
    """)
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.line_chart(np.random.randn(30, 3))

    # text_area
    st.markdown("""
    ## Text Area
    `st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, 
    kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")`
    """)
    txt = st.text_area(
        "Text to analyze",
        "It was the best of times, it was the worst of times, it was the age of "
        "wisdom, it was the age of foolishness, it was the epoch of belief, it "
        "was the epoch of incredulity, it was the season of Light, it was the "
        "season of Darkness, it was the spring of hope, it was the winter of "
        "despair, (...)",
    )
    st.write(f"You wrote {len(txt)} characters.")

    # text_input
    st.markdown("""
    ## Text Input
    `st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
    on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")`
    """)
    title = st.text_input("Movie title", "Life of Brian")
    st.write("The current movie title is", title)

    # camera_input
    st.markdown("""
    ## Camera Input
    `st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, 
    label_visibility="visible")`
    """)
    # picture = st.camera_input("Take a picture")
    # if picture:
    #     st.image(picture)

    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        # To read image file buffer as bytes:
        bytes_data = img_file_buffer.getvalue()
        # Check the type of bytes_data:
        # Should output: <class 'bytes'>
        st.write(type(bytes_data))

    # file_uploader
    st.markdown("""
    ## File Uploader
    `st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, 
    kwargs=None, *, disabled=False, label_visibility="visible")`
    """)
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)
        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

    # Third-party components
    st.markdown("""
    ## Third-party components
    (Tags)[https://github.com/gagan3012/streamlit-tags] \n
    (Streamlit Elements)[https://github.com/okld/streamlit-elements] \n
    (Streamlit Extras)[https://extras.streamlit.app] \n
    (Stqdm)[https://github.com/Wirg/stqdm] \n
    (Timeline)[https://github.com/innerdoc/streamlit-timeline] \n
    (Camera input live)[https://github.com/blackary/streamlit-camera-input-live] \n
    (Streamlit Ace)[https://github.com/okld/streamlit-ace] \n
    (Streamlit Chat)[https://github.com/AI-Yash/st-chat] \n
    (Streamlit Option Menu)[https://github.com/victoryhb/streamlit-option-menu] \n
    """)
