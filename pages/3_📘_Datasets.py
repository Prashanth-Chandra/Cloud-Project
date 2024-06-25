import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import io


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


st.set_page_config(page_title = "Datasets", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'> Made with ❤️ from Prashanth </h1>", unsafe_allow_html=True)


st.title("City📘")
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)
all_Datasets = ["Select a City","Albury", "Canberra","Melbourne","Portland","WaggaWagga"]
data_choice = st.selectbox("Dataset", all_Datasets)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
if data_choice == "Albury":
    df_weather = pd.read_csv("./Dataset/Albury.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_weather.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_weather.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_weather.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_weather.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_weather
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_weather.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_weather.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_weather.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_weather[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_weather.describe().T
        st.write(df_descr) 



elif  data_choice == "Canberra":
    df_weather = pd.read_csv("./Dataset/Canberra.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_weather.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_weather.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_weather.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_weather.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_weather
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_weather.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_weather.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_weather.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_weather[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_weather.describe().T
        st.write(df_descr) 



elif  data_choice == "Melbourne":
    df_weather = pd.read_csv("./Dataset/Melbourne.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_weather.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_weather.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_weather.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_weather.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_weather
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_weather.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_weather.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_weather.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_weather[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_weather.describe().T
        st.write(df_descr) 



elif   data_choice == "Portland": 
    df_weather = pd.read_csv("./Dataset/Portland.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_weather.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_weather.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_weather.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_weather.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_weather
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_weather.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_weather.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_weather.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_weather[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_weather.describe().T
        st.write(df_descr) 



elif   data_choice == "WaggaWagga":
    df_weather = pd.read_csv("./Dataset/WaggaWagga.csv")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Information</h1>", unsafe_allow_html=True)
    if st.checkbox("Dataset General Information"):
        
        buffer = io.StringIO()
        df_weather.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    if st.checkbox("Dataset Shape"):   
        sum = df_weather.shape
        st.markdown(":blue[" + str(sum) + "]")  

    if st.checkbox("Rows Shape"):   
        sum_rows = df_weather.shape[0]
        st.markdown(":blue[" + str(sum_rows) + "]") 

    if st.checkbox("Columns Shape"):   
        sum_col = df_weather.shape[1]
        st.markdown(":blue[" + str(sum_col) + "]") 

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'>Dataset Overview</h1>", unsafe_allow_html=True)
    # st.markdown("<br> <br> ", unsafe_allow_html=True)

    if st.checkbox("Dataset Preview"):   
        df_preview = df_weather
        st.write(df_preview)  

    if st.checkbox("Dataset Head"):   
        df_head = df_weather.head()
        st.write(df_head)  

    if st.checkbox("Dataset Tail"):   
        df_tail = df_weather.tail()
        st.write(df_tail)  

    if st.checkbox("Dataset Columns"):  
        all_columns = df_weather.columns.to_list()
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_df = df_weather[selected_columns]
        st.write(new_df)
    

    if st.checkbox("Dataset Summary"):   
        df_descr = df_weather.describe().T
        st.write(df_descr) 


