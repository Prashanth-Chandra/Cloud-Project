import streamlit as st
from PIL import Image

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')


st.set_page_config(page_title = "About us", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'> Made with ❤️ from Prashanth </h1>", unsafe_allow_html=True)




st.title("About us📍")
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("This project developed by The A Team comprising of :blue[**_Prashanth Chandra Reddy, Sanjay J K S, Hrishab T H and Anupam Kumar_**] for Department of Weather Forecast focus on predicting the weather in 5 cities in Australia using :blue[**_using Machine Learning_**].")
st.markdown(" <br> ", unsafe_allow_html=True)
