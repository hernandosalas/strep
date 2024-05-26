import streamlit as st
import base64

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

st.write("""
# My first app
Hello *world!*
Strep AI
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Do something with the file
    st.write('You selected `%s`' % uploaded_file.name)
    base64_string = encode_image(uploaded_file.name)
    st.write(base64_string)

