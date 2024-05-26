import streamlit as st

st.write("""
# My first app
Hello *world!*
Strep AI
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Do something with the file
    st.write('You selected `%s`' % uploaded_file.name)