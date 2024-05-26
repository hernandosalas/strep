import streamlit as st
import base64
import requests

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

prompt = '''
To accurately determine if the image depicts strep throat, please provide a detailed analysis based on the following criteria:

	1.	Redness: Is there significant redness in the throat or on the tonsils?
	2.	Swelling: Are the tonsils swollen or enlarged?
	3.	White Patches or Streaks: Are there any white patches, streaks, or pus on the tonsils or throat?
	4.	Appearance of Uvula: Is the uvula (the small fleshy extension at the back of the throat) red and swollen?
	5.	Lymph Nodes: Are there visible or palpable swollen lymph nodes in the neck area?
	6.	Other Symptoms: Note any other visible symptoms such as a rash on the skin (scarlet fever) or red spots on the roof of the mouth.

Please thoroughly explain your reasoning for each criterion, stating whether the image displays these signs and why they are indicative (or not) of strep throat.
'''

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
            "text": prompt
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
    "max_tokens": 1000
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