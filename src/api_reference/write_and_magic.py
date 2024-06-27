import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time


def write_and_magic():
    st.markdown("""
    # st.write
    
    Write arguments to the app.This is the Swiss Army knife of Streamlit commands: it does different things depending on 
    what you throw at it. Unlike other Streamlit commands, write() has some unique properties:

    - You can pass in multiple arguments, all of which will be written.
    - Its behavior depends on the input types as follows.
    - It returns None, so its "slot" in the App cannot be reused.

    `st.write(*args, unsafe_allow_html=False, **kwargs)`
    
    

    One or many objects to print to the App.

    Arguments are handled as follows:
    - write(string) : Prints the formatted Markdown string, with
        support for LaTeX expression, emoji shortcodes, and colored text. See docs for st.markdown for more.
    - write(data_frame) : Displays the DataFrame as a table.
    - write(error) : Prints an exception specially.
    - write(func) : Displays information about a function.
    - write(module) : Displays information about the module.
    - write(class) : Displays information about a class.
    - write(dict) : Displays dict in an interactive widget.
    - write(mpl_fig) : Displays a Matplotlib figure.
    - write(generator) : Streams the output of a generator.
    - write(openai.Stream) : Streams the output of an OpenAI stream.
    - write(altair) : Displays an Altair chart.
    - write(PIL.Image) : Displays an image.
    - write(keras) : Displays a Keras model.
    - write(graphviz) : Displays a Graphviz graph.
    - write(plotly_fig) : Displays a Plotly figure.
    - write(bokeh_fig) : Displays a Bokeh figure.
    - write(sympy_expr) : Prints SymPy expression using LaTeX.
    - write(htmlable) : Prints _repr_html_() for the object if available.
    - write(obj) : Prints str(obj) if otherwise unknown.
    
    **e.g.**
    """)
    st.write('Hello, *World!* :sunglasses:')

    st.write(1234)
    data_frame = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    })
    st.write(data_frame)

    st.write('1 + 1 = ', 2)
    st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)

    st.markdown("""[Featured video](https://www.youtube.com/watch?list=TLGGuESX_dLzy0YxMjA2MjAyNA&v=wpDuY9I2fDg)""")

    st.markdown("""
    # st.write_stream
    
    Stream a generator, iterable, or stream-like sequence to the app.

    `st.write_stream` iterates through the given sequences and writes all chunks to the app. String chunks will be 
    written using a typewriter effect. Other data types will be written using `st.write`.
    
    `st.write_stream(stream)`
    
    - stream (Callable, Generator, Iterable, OpenAI Stream, or LangChain Stream)
    - The generator or iterable to stream.
    
    **e.g.**
    """)

    _LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """

    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)

        yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )

        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)

    if st.button("Stream data"):
        st.write_stream(stream_data)

    st.markdown("""
    # Magic
    
    Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without 
    having to type an explicit command at all. Just put the thing you want to show on its own line of code, and it will 
    appear in your app. 
    
    ## How Magic works
    Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app
    using `st.write` (which you'll learn about later).
    
    Also, magic is smart enough to ignore docstrings. That is, it ignores the strings at the top of files and functions.
    
    If you prefer to call Streamlit commands more explicitly, you can always turn magic off in your `~/.streamlit/config.toml` 
    with the following setting:
    
    ```
    [runner]
    magicEnabled = false
    ```
    """)

    st.markdown("""[Featured video](https://youtu.be/wpDuY9I2fDg?list=TLGGuESX_dLzy0YxMjA2MjAyNA)""")
