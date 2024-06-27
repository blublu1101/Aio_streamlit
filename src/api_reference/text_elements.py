import streamlit as st


def text_elements():
    st.markdown("""
    Document: [Text elements](https://docs.streamlit.io/develop/api-reference/text)
    
    Streamlit apps usually start with a call to `st.title` to set the app's title. After that, there are 2 heading levels 
    you can use: `st.header` and `·`st.subheader`.
    
    Pure text is entered with `st.text`, and Markdown with `st.markdown`.
    
    We also offer a "swiss-army knife" command called `st.write`, which accepts multiple arguments, and multiple data types.
    And as described above, you can also use magic commands in place of `st.write`.
    """)

    # markdown
    st.markdown("""
    ## Headings and body text
    ### Markdown
    `st.markdown(body, unsafe_allow_html=False, *, help=None)`
    """)
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

    md = st.text_area('Type in your markdown string (without outer quotes)',
                      "Happy Streamlit-ing! :balloon:")
    st.code(f"""
    import streamlit as st
    st.markdown('''{md}''')
    """)
    st.markdown(md)

    # title
    st.markdown("""
    ### Title
    `st.title(body, anchor=None, *, help=None)`
    """)
    st.title('This is a title')
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')

    # header
    st.markdown("""
    ### Header
    `st.header(body, anchor=None, *, help=None, divider=False)`
    """)
    st.header('This is a header with a divider', divider='rainbow')
    st.header('_Streamlit_ is :blue[cool] :sunglasses:')

    # subheader
    st.markdown("""
    ### Subheader
    `st.subheader(body, anchor=None, *, help=None, divider=False)`
    """)
    st.subheader('This is a subheader with a divider', divider='rainbow')
    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

    # caption
    st.markdown("""
    ## Formatted text
    ### Caption
    `st.caption(body, unsafe_allow_html=False, *, help=None)`
    """)
    st.caption('This is a string that explains something above.')
    st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

    # Code block
    st.markdown("""
    ### Code block
    `st.code(body, language="python", line_numbers=False)`
    """)
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')

    # Echo
    st.markdown("""
    ### Echo
    `st.echo(code_location="above")`
    """)

    def get_user_name():
        return 'John'

    with st.echo():
        # Everything inside this block will be both printed to the screen
        # and executed.
        def get_punctuation():
            return '!!!'

        greeting = "Hi there, "
        value = get_user_name()
        punctuation = get_punctuation()

        st.write(greeting, value, punctuation)
    # And now we're back to _not_ printing to the screen
    st.write('Done!')

    # Performatted text
    st.markdown("""
    ### Performatted text
    `st.text(body, *, help=None)`
    """)
    st.text('This is some text.')

    # LaTeX
    st.markdown("""
    ### LaTeX
    `st.latex(body, *, help=None)`
    """)
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    # Divider
    st.markdown("""
    ### Divider
    `st.divider()`
    """)
    st.write("This is some text.")
    st.slider("This is a slider", 0, 100, (25, 75))
    st.divider()  # 👈 Draws a horizontal rule
    st.write("This text is between the horizontal rules.")
    st.divider()  # 👈 Another horizontal rule

    # Third-party components
    st.markdown("""
    ## Third-party components
    [Tags](https://github.com/gagan3012/streamlit-tags) \n
    [Drawable Canvas](https://github.com/andfanilo/streamlit-drawable-canvas) \n
    [NLU](https://github.com/JohnSnowLabs/nlu) \n
    [Streamlit Extras](https://extras.streamlit.app/) \n
    [Annotated text](https://github.com/andfanilo/streamlit-drawable-canvas) \n
    """)
