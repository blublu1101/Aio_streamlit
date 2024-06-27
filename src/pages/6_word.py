import streamlit as st
import pandas

# st.balloons()
# st.snow()
st.toast('Mr Stay-Puft')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')

# st.help(pandas.DataFrame)

with st.echo():
    st.write('Code will be executed and printed')
