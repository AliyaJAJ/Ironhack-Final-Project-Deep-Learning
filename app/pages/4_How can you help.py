import streamlit as st

st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide"
)

st.title("Help Reduce Animal Poaching")

st.write("")


col3, col4 = st.columns(2)

with col3:
    st.header("World Wildlife Fund(WWF)")
    st.markdown("<p style='font-size: 24px;'>Wildlife crime is the most immediate threat to wild elephants, tigers and rhinos.</p>", unsafe_allow_html=True)
    
    
    
    st.markdown("<p style='font-size: 24px;'>WWF is urging governments—particularly those of demand countries such as China, Vietnam, Thailand, and the U.S., to strengthen law enforcement, invest in more boots on the ground, and commit to long-term demand reduction efforts. However, we also need your support to stop demand for illegal wildlife parts and products. </p>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 24px;'>Pledge to stop wildlife crime and commit to preserving nature's beauty for future generations.</p>", unsafe_allow_html=True)
    
    st.write("")
    st.markdown("<div style='display: flex; justify-content: center;'>"
                "<a href='https://support.worldwildlife.org/site/Advocacy?cmd=display&page=UserAction&id=664&_gl=1*5c43i8*_ga*MTAxMDM5NzU1Ny4xNjg1NzIzNjM1*_ga_FK6M9RK84Z*MTY4NTc5NDMyOC4zLjEuMTY4NTc5NDM3NS4xMy4wLjA.&_ga=2.172821923.1640862725.1685723635-1010397557.1685723635' target='_blank'>"
                "<button style='font-size: 22px; padding: 10px 20px; height: 55px; background-color: transparent; border-radius: 20px; color: red;'>Sign Pledge</button>"
                "</a>"
                "</div>", unsafe_allow_html=True)

    
st.write("") 
st.write("") 
st.write("") 
st.write("") 

with col4:
    st.image("https://files.worldwildlife.org/wwfcmsprod/images/African_Forest_Elephant_WW187349/story_full_width/4g93qymng2_African_Forest_Elephant_WW187349.jpg")


st.write("")
st.write("")
st.write("")


col5, col6 = st.columns(2)
with col5:
    
    st.header("Sheldrick Wildlife Trust (SWT)")


    st.markdown("<p style='font-size: 24px;'>SWT embraces all measures that complement the conservation, preservation and protection of wildlife and habitats. Some projects include anti-poaching, enhancing community awareness, addressing animal welfare issues, rescuing and hand rearing elephant and rhino orphans, that can ultimately enjoy a quality of life in wild terms when grown.</p>", unsafe_allow_html=True)


    st.markdown("<p style='font-size: 24px;'>They currently operate twenty three Anti-Poaching Teams. Their front line teams are fully trained and equipped to deter and prevent illegal wildlife activities, as well as launch ambushes, with any necessary arrests carried out by Kenya Wildlife Service (KWS).</p>", unsafe_allow_html=True)
    st.write("")

    st.markdown("<div style='display: flex; justify-content: center;'>"
                "<a href='https://www.sheldrickwildlifetrust.org/projects/anti-poaching' target='_blank'>"
                "<button style='font-size: 22px; padding: 10px 20px; height: 55px; background-color: transparent; border-radius: 20px; color: red;'>Donate</button>"
                "</a>"
                "</div>", unsafe_allow_html=True)



with col6:
    st.image("https://media.sciencephoto.com/c0/15/06/70/c0150670-800px-wm.jpg")