import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
import streamlit as st

load_dotenv()

gemini_api_key=os.getenv('api')
genai.configure(api_key=gemini_api_key)

st.header('Image analytics')
uploaded_file=st.file_uploader("Upload the image",type=["jpg","png","jpeg"])


if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

prompt=st.text_input('enter the text')
if st.button('GET RESPOSE'):
    img=Image.open(uploaded_file)
    model = genai.GenerativeModel(model_name='models/gemini-2.5-flash')
    response=model.generate_content([prompt,img])
    st.markdown(response.text)
     

# mof]d\\\\\