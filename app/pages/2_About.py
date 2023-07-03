import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide"
)


##Start to build our web app
st.title("Poaching")


st.header("Overview")

st.markdown("<p style='font-size: 24px;'>Poaching is the the illegal shooting, trapping, or taking of game, fish, or plants from private property or from a place where such practices are specially reserved or forbidden. Animals are seen to have commercial value as jewelry, decor, or traditional medicine. For example, the ivory tusks of African elephants are carved into trinkets or display pieces.</p>", unsafe_allow_html=True)
st.write('')

st.markdown("<p style='font-size: 24px;'>Financial gain and human–wildlife conflict are the two main causes of poaching. Human–wildlife conflict involves the tangible and/or perceived impacts of wildlife on people, including human injury and death, direct and indirect economic damage to crops, livestock, and property.</p>", unsafe_allow_html=True)
st.write('')



st.markdown("<p style='font-size: 24px;'>In 1989, the Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) banned the international commercial trade in elephant ivory. Poaching rates dropped following this action, but began to surge again around 2010, due to renewed consumer interest in purchasing elephant ivory, largely in Asia.</p>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

st.write("---")

col10, col11= st.columns(2)

with col10:
    st.header("Effects of Poaching ")
    bullet_list = """
        <ul style='font-size: 24px;'>
            <li style='font-size: 24px;'>Poaching has devastating consequences for wildlife. In some instances, it is the primary reason why an animal faces a risk of extinction. This is the case with the African elephants, more than 100,000 of which were killed between 2014 and 2017 for ivory.</li><br>
            <li style='font-size: 24px;'>In certain parks where security is controlled, poachers kill the rangers and officers, so they have access to the animals. In Africa, nearly 600 rangers charged with protecting wildlife were gunned down by poachers between 2009 and 2016 while in the line of duty.</li><br>
            <li style='font-size: 24px;'>Poaching creates an imbalance in the ecosystem. Many wildlife animals help maintain the food chain and its balance, if they are 'taken away', the ecosystem is disturbed and could lead to more deaths.</li><br>
        </ul>
        """
    st.markdown(bullet_list, unsafe_allow_html=True)

with col11:

    st.header("Effects on Tourism")
    bullet_list = """
        <ul style='font-size: 24px;'>
            <li style='font-size: 24px;'>Wildlife tourism attracts substantial numbers and ultimately brings in hundreds of thousands of tourists of local and international visitors each year. Elephants are one of the big 5 alongside leopards, lions, rhinoceros and buffalos.</li><br>
            <li style='font-size: 24px;'>The tourism sector generates thousands of jobs so a reduction in tourism will result in less employment for local communities involved in the accommodation, restaurant and guiding sectors. Poaching has impacted tourism levels with the population of elephants (and rhinoceroses).</li><br>
            <li style='font-size: 24px;'>A decline in tourists’ visits will directly affect tourism revenue which forms the bulk of the funding for conservation and protection of endangered animals.</li><br>
                       
        </ul>
        """
    st.markdown(bullet_list, unsafe_allow_html=True)
    
