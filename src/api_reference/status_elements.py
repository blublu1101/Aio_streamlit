import streamlit as st
import time as tm


def status_elements():
    st.markdown("""
    Documentation: [Display progress and status](https://docs.streamlit.io/develop/api-reference/status)
    # Display progress and status
    ## Progress
    
    `st.progress(value, text=None)`
    """)
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        tm.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    tm.sleep(1)
    my_bar.empty()
    st.button("Rerun")

    # spinner
    st.markdown("""
    ## Spinner
    `st.spinner(text="In progress...")`
    """)
    with st.spinner('Wait for it...'):
        tm.sleep(5)
    st.success('Done!')

    # success
    st.markdown("""
    ## Success
    `st.success(body, *, icon=None)`
    """)
    st.success('This is a success message!', icon="✅")

    # info
    st.markdown("""
       ## Info
       `st.info(body, *, icon=None)`
       """)
    st.info('This is a purely informational message', icon="ℹ️")

    # warning
    st.markdown("""
       ## Warning
       `st.warning(body, *, icon=None)`
       """)
    st.warning('This is a warning', icon="⚠️")

    # error
    st.markdown("""
       ## Error
       `st.error(body, *, icon=None)`
       """)
    st.error('This is an error', icon="🚨")

    # exception
    st.markdown("""
   ## Exception
   `st.exception(exception)`
   """)
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)

    # status
    st.markdown("""
        ## Status
        `st.status(label, *, expanded=False, state="running")`
        """)
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        tm.sleep(2)
        st.write("Found URL.")
        tm.sleep(1)
        st.write("Downloading data...")
        tm.sleep(1)
        status.update(label="Download complete!", state="complete", expanded=False)
    st.button("Rerun")

    # toast
    st.markdown("""
        ## Toast
        `st.toast(body, *, icon=None)`
        """)
    st.toast('Your edited image was saved!', icon='😍')

    if st.button('Three cheers'):
        st.toast('Hip!')
        tm.sleep(.5)
        st.toast('Hip!')
        tm.sleep(.5)
        st.toast('Hooray!', icon='🎉')

    def cook_breakfast():
        msg = st.toast('Gathering ingredients...')
        tm.sleep(1)
        msg.toast('Cooking...')
        tm.sleep(1)
        msg.toast('Ready!', icon="🥞")

    if st.button('Cook breakfast'):
        cook_breakfast()

    # balloons/snow
    st.markdown("""
        ## Balloons and Snow
        `st.balloons()`
        `st.snow()`
        """)
    st.balloons()
    st.snow()
