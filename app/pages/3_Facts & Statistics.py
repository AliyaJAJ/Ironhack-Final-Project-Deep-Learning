import streamlit as st

st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide"
)

st.title("African Elephants")

st.write("")
st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 24px;'>African elephants are the largest land animals on Earth, scientists have determined that there are actually two species of African elephants.</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 24px;'>Savanna elephants are larger animals that roam the plains of sub-Saharan Africa, while forest elephants are smaller animals that live in the forests of Central and West Africa. The International Union for the Conservation of Nature lists both as critically endangered.</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 24px;'>In recent years, at least 20,000 elephants have been killed in Africa each year for their tusks. African forest elephants have been the worst hit.</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 24px;'>The African Elephant population has dropped by 62% in the last decade and is expected to drop another 30% by 2025 making them an endangered species.</p>", unsafe_allow_html=True)
    
    
with col2:
    tableau_url = "https://public.tableau.com/views/IronhackFinalProject_16860571089940/TotalPopulation1995-2015?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link"
    tableau_embed_code = f'<iframe src="{tableau_url}:showVizHome=no" width="100" height="600" frameborder="0"></iframe>'
    st.markdown(tableau_embed_code, unsafe_allow_html=True)
    st.markdown("""
        <style>
            iframe {
                width: 100%;
                height:1000px;
            }
        </style>
    """, unsafe_allow_html=True)


    

    
col3, col4 = st.columns(2)
with col3:

    bullet_list = """
    <ul style='font-size: 24px;'>
    <br>
    <br>
    <br>
        <li style='font-size: 24px;'>African elephants are found in 37 countries in sub-Sahara Africa, with an estimated 70% in Southern Africa, 20% in Eastern Africa, 6% in Central Africa and 3% in West Africa.</li><br>
        <li style='font-size: 24px;'>Elephant tusks serve many purposes. These extended teeth can be used to protect the elephant's trunk, lift and move objects, gather food, and strip bark from trees. They can also be used for defense. During times of drought, elephants even use their tusks to dig holes to find water underground.</li><br>
        <li style='font-size: 24px;'>Male's tusks are longer and heavier, weighing between 110 and 175 pounds each. Females' tusks weigh approximately 40 pounds each.</li><br>
        <li style='font-size: 24px;'>Given that ivory sells for approximately $3,300 per pound, poachers have plenty of motivation to continue killing elephants for their tusks.</li><br>
        <li style='font-size: 24px;'>Today, the greatest threat to African elephants is wildlife crime, primarily poaching for the illegal ivory trade!</li><br>
        
        
    </ul>
    """
    st.markdown(bullet_list, unsafe_allow_html=True)

with col4:
    tableau_url = "https://public.tableau.com/views/IronhackFinalProject_/PopulationofAfricanElephantsByCountry_1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link"
    tableau_embed_code = f'<iframe src="{tableau_url}:showVizHome=no" width="100" height="600" frameborder="0" ></iframe>'
    st.markdown(tableau_embed_code, unsafe_allow_html=True)
    st.markdown("""
        <style>
            iframe {
                width: 100%;
                height:1000px;
            }
        </style>
    """, unsafe_allow_html=True)