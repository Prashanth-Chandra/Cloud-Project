import streamlit as st
import joblib
import numpy as np
import pandas as pd
import random
from PIL import Image


# Load the model
model = joblib.load('model.pkl')

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

st.set_page_config(page_title="Datasets", page_icon=image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.image(image, use_column_width=True, output_format='auto')

st.sidebar.markdown("---")

st.sidebar.markdown(
    "<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'> Made with ❤️ from Prashanth </h1>",
    unsafe_allow_html=True)


# Function to get user input using expanders
def get_user_input():
    st.header('Enter Weather Details')

    with st.expander('Temperature and Rain'):
        MinTemp = st.number_input('MinTemp', format="%.1f")
        MaxTemp = st.number_input('MaxTemp', format="%.1f")
        Rainfall = st.number_input('Rainfall', format="%.1f")
        Evaporation = st.number_input('Evaporation', format="%.1f")
        Sunshine = st.number_input('Sunshine', format="%.1f")

    with st.expander('Wind'):
        WindGustDir = st.number_input('WindGustDir', format="%.1f")
        WindGustSpeed = st.number_input('WindGustSpeed', format="%.1f")
        WindDir9am = st.number_input('WindDir9am', format="%.1f")
        WindDir3pm = st.number_input('WindDir3pm', format="%.1f")
        WindSpeed9am = st.number_input('WindSpeed9am', format="%.1f")
        WindSpeed3pm = st.number_input('WindSpeed3pm', format="%.1f")

    with st.expander('Humidity and Pressure'):
        Humidity9am = st.number_input('Humidity9am', format="%.1f")
        Humidity3pm = st.number_input('Humidity3pm', format="%.1f")
        Pressure9am = st.number_input('Pressure9am', format="%.1f")
        Pressure3pm = st.number_input('Pressure3pm', format="%.1f")

    with st.expander('Cloud and Temperature'):
        Cloud9am = st.number_input('Cloud9am', format="%.1f")
        Cloud3pm = st.number_input('Cloud3pm', format="%.1f")
        Temp9am = st.number_input('Temp9am', format="%.1f")
        Temp3pm = st.number_input('Temp3pm', format="%.1f")
        RainToday = st.selectbox('RainToday', options=['Yes', 'No'])

    with st.expander('Date and Time'):
        Year = st.number_input('Year', min_value=1900, max_value=2100, format='%d')
        Month = st.number_input('Month', min_value=1, max_value=12, format='%d')
        Day = st.number_input('Day', min_value=1, max_value=31, format='%d')
        DayOfWeek = st.number_input('DayOfWeek', min_value=0, max_value=6, format='%d')
        Hour = st.number_input('Hour', min_value=0, max_value=23, format='%d')

    Month_sin = np.sin(2 * np.pi * Month / 12)
    Month_cos = np.cos(2 * np.pi * Month / 12)
    DayOfWeek_sin = np.sin(2 * np.pi * DayOfWeek / 7)
    DayOfWeek_cos = np.cos(2 * np.pi * DayOfWeek / 7)

    # Create a dictionary with the user input
    user_input = {
        'MinTemp': MinTemp,
        'MaxTemp': MaxTemp,
        'Rainfall': Rainfall,
        'Evaporation': Evaporation,
        'Sunshine': Sunshine,
        'WindGustDir': WindGustDir,
        'WindGustSpeed': WindGustSpeed,
        'WindDir9am': WindDir9am,
        'WindDir3pm': WindDir3pm,
        'WindSpeed9am': WindSpeed9am,
        'WindSpeed3pm': WindSpeed3pm,
        'Humidity9am': Humidity9am,
        'Humidity3pm': Humidity3pm,
        'Pressure9am': Pressure9am,
        'Pressure3pm': Pressure3pm,
        'Cloud9am': Cloud9am,
        'Cloud3pm': Cloud3pm,
        'Temp9am': Temp9am,
        'Temp3pm': Temp3pm,
        'RainToday': 1 if RainToday == 'Yes' else 0,
        'Year': Year,
        'Month': Month,
        'Day': Day,
        'DayOfWeek': DayOfWeek,
        'Hour': Hour,
        'Month_sin': Month_sin,
        'Month_cos': Month_cos,
        'DayOfWeek_sin': DayOfWeek_sin,
        'DayOfWeek_cos': DayOfWeek_cos
    }

    return user_input


# Streamlit app layout
st.title('Rain Tomorrow Prediction')

user_input = get_user_input()

if st.button('Predict'):
    # Convert user input to a dataframe
    user_input_df = pd.DataFrame(user_input, index=[0])

    print(user_input['Rainfall'])

    if(user_input['Rainfall'] >= 4.0 or user_input['Cloud3pm'] > 2.0):
        result = 'Yes'
    else:
        prediction = model.predict(user_input_df)
        result = 'Yes' if prediction[0] == 1 else 'No'

    print(result)

    options = ['Yes', 'No']
    result = random.choice(options)

    if(user_input_df.iloc(0) == 0 and user_input_df.iloc(1) == 0 and user_input_df.iloc(2) == 0 and user_input_df.iloc(3) == 0 ):
        result = 'No'


    if result == 'Yes':
        st.subheader('Tomorrow')
        st.image('rainy.png', caption='Rainy Tomorrow')
    else:
        st.image('sunny.jpg', caption='Sunny Tomorrow')
