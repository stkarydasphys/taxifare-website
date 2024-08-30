import streamlit as st
import datetime

import requests
import json

import pandas as pd


'''
# TaxiFareModel front
'''

"""
Details of the ride
"""
number_of_passengers = st.number_input('How many passengers?', step = 1)


date_ = st.date_input("When's the pickup date?", datetime.date(2019, 7, 6))

time_ = st.time_input('When is the pickup time?', datetime.time(8, 45))

pickup_lon = st.slider('Select the pickup longitude', min_value=-180.0, max_value=180.0, value=0.000, step = 0.00001)

pickup_lat = st.slider('Select the pickup latitude', min_value=-90.0, max_value=90.0, value=0.0, step = 0.00001)

dropoff_lon = st.slider('Select the dropoff longitude', min_value=-180.0, max_value=180.0, value=0.0, step = 0.00001)

dropoff_lat = st.slider('Select the dropoff latitude', min_value=-90.0, max_value=90.0, value=0.0, step = 0.00001)



url = 'https://taxifare.lewagon.ai/predict'


user_dict = {'pickup_datetime': str(date_)+" "+str(time_), 'pickup_longitude': pickup_lon, 'pickup_latitude': pickup_lat,
             'dropoff_longitude': dropoff_lon, 'dropoff_latitude': dropoff_lat, 'passenger_count': number_of_passengers}


response = requests.get(url, params = user_dict)
data = response.json()
readable_data = json.dumps(data, indent = 4)

st.text(f"your fare will be {readable_data}")
