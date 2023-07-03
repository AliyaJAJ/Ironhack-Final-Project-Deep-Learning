import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide"
)

st.title("Feature Improvements")


bullet_list = """
    <ul style='font-size: 24px;'>
    <br>
        <li style='font-size: 26px;'>Train the model to differentiate between rangers and poachers.</li><br>
        <li style='font-size: 26px;'>Connect to drones that can provide live surveillance of the conservancy.</li><br>
        <li style='font-size: 26px;'> Include a tracking feature on poachers to identify routes they may use frequently.</li><br>
        
        
    </ul>
    """
st.markdown(bullet_list, unsafe_allow_html=True)

st.write('')
st.write('')

image10 = Image.open('/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/media/12062017_stoppoaching.jpeg')
st.image(image10, width=1500)