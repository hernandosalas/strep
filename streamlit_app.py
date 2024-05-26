import streamlit as st
import base64
import requests

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image(base64_image,key):
  st.write("Analyzing the image...")
  headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
  payload = {
    "model": "gpt-4o",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Does this image is stepthroat?Yes or No?Explain why."
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }
  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  content = response.json()["choices"][0]["message"]["content"]
  return content

st.write("""
# Strep AI
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write('You selected `%s`' % uploaded_file.name)
    base64_string = encode_image(uploaded_file)
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

## Get user input and hide the input
password = st.text_input("key", type="password")

if st.button("Analyze"):
    response = analyze_image(base64_string,password)
    st.write(response)