import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide",
    initial_sidebar_state="auto", 
    menu_items=None
)



st.title('Poacher Detector: A model to reduce poaching')
st.header('Aliya Janmohamed')

st.write('')
st.write('')
st.write('')
image1 = Image.open('/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/media/elephantbackground.jpeg')
st.image(image1, width=1500)


