import streamlit as st
import pandas as pd 
from pymongo import MongoClient

client = MongoClient()
db = client.get_database("car_fuel_api")


df=pd.read_csv("data/measurements_clean.csv")
st.title("Car Fuel App")

st.write("Datos obtenidos:")
st.write(df)

distancia=st.sidebar.selectbox("Elige una distancia", df["distance"])

"Has seleccionado:", distancia

def distancefind(distancia):
    curs=db.car_fuel.find({"distance": distancia}, {"_id":0,"consume":1})
    df1=pd.DataFrame(curs)
    return df1

if st.button("Buscar con distancia"):
    df=distancefind(distancia)
    st.write(df)

velocidad=st.sidebar.selectbox("Elige una velocidad", df["speed"])

"Has seleccionado:", velocidad

def speedfind(velocidad):
    curs=db.car_fuel.find({"speed": velocidad}, {"_id":0,"consume":1})
    df2=pd.DataFrame(curs)
    return df2

if st.button("Buscar con velocidad"):
    df=speedfind(velocidad)
    st.write(df)

temperatura=st.sidebar.selectbox("Elige una temperatura", df["temp_inside"])

"Has seleccionado:", temperatura

def tempfind(temperatura):
    curs=db.car_fuel.find({"temp_inside": temperatura}, {"_id":0,"consume":1})
    df3=pd.DataFrame(curs)
    return df3

if st.button("Buscar con temperatura"):
    df=tempfind(temperatura)
    st.write(df)

combustible=st.sidebar.selectbox("Elige un combustible", df["gas_type"])

"Has seleccionado:", combustible

def fuelfind(combustible):
    curs=db.car_fuel.find({"gas_type": combustible}, {"_id":0,"consume":1})
    df4=pd.DataFrame(curs)
    return df4

if st.button("Buscar con combustible"):
    df=fuelfind(combustible)
    st.write(df)
