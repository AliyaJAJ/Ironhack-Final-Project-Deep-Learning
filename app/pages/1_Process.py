import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide",
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title('Process:')

st.write('')
st.write('')
st.write('')




col7,col8 = st.columns(2)

with col7:
    image2 = Image.open('/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/media/Data-Collection.jpeg')
    st.image(image2, width = 800)

with col8:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<p style='font-size: 24px;'>Data Collection</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>Images of elephants</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>Images of poachers</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>African elephants population dataset, enriched with current statistics for some countires</p>", unsafe_allow_html=True)
   

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)
    

    
col9, col10 = st.columns(2)
with col9:
    image3 = Image.open('/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/media/5f6bc60e665f546a6b1e5400_logo_yo.jpeg')
    st.image(image3, width=800)
    
with col10:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<p style='font-size: 24px;'>Model</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>Yolov5 (Object detection model)</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>Retrained with custom data</p>", unsafe_allow_html=True)


    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)
    

col11, col12 = st.columns(2)
with col11:
    image4 = Image.open('/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/media/featured-image.jpeg')
    st.image(image4, width=800)
    
with col12:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<p style='font-size: 24px;'>Additional Features</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>Email Notification when the target class is detected</p>", unsafe_allow_html=True)
    st.markdown("- <p style='font-size: 20px;'>Tableau for Data Visualization</p>", unsafe_allow_html=True)

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)
    