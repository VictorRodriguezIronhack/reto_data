import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Different sections I will be using
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()


#The database I will be using
unpickled_df = pd.read_pickle("./dummy.pkl")

#Lets structure it into different sections
with header:
    st.title('Gas consumption per type')
    
with dataset:
    st.header('Dataset: Car fuel consumption')
    st.text('This dataset was provided to us, and it can be found in kaggle ;https://www.kaggle.com/anderas/car-consume?select=measurements.csv')

    #Insert the dataframe
    st.dataframe(unpickled_df.head())

    #Lets represent the speed,consumption and distance
    st.subheader('This histogram represents the distance driven each trip;')
    hist_values = np.histogram(unpickled_df['distance'], bins=8, range=(0,200))[0]
    st.bar_chart(hist_values)

    st.subheader('This histogram represents the car consumption distribution;')
    con_dist = pd.DataFrame(unpickled_df['consume'].value_counts())
    st.bar_chart(con_dist)

    st.subheader('This histogram represents the car speed;')
    hist_values = np.histogram(unpickled_df['speed'], bins=11, range=(0,100))[0]
    st.bar_chart(hist_values)

  
with features:
    st.header('New features I came up with')
    st.text('Some interesting bullet points could be written here...')

with model_training:
    st.header('Model training')
    st.text('In this section you can see wich algorithm used was more precise!')

######
cols = ["distance", "consume", "speed", "temp_inside", "temp_outside","gas_type","AC","rain","sun"]
st_ms = st.multiselect("Columns", unpickled_df.columns.tolist(), default=cols)