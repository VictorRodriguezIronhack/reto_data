import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly as ply
import seaborn as sns
import re

"""# First look at `measurements.csv`"""
df = pd.read_csv("/Users/claytonlouden/reto-data/data/measurements.csv")
st.dataframe(df.head())

"### Shape of data"
df.shape

"### Null values"
st.write(df.isnull().sum())

"We want to separate the columns that have values for weather conditions `specials` so that we have the option to work with it later."

"# `Specials` Column Only"
df_specials = df[df['specials'].notnull()]
st.dataframe(df_specials.head())

"# Dropped `Specials` Column"
df_no_special = df[df['specials'].isnull()]
st.dataframe(df_no_special.head())
st.dataframe(df_no_special.isnull().sum())

df_no_special.shape

"""But we need to consider that this is a chronology maybe we should not separate these so quickly.
 Maybe this should be treated similat to a time series. But we will drop `specials` and `refill gas`.
 `specials` because we have those values reflected in the columns `rain`, and `sun`, those of which we are dropping anyway because they don't contain enough information. 
 We will keep `AC`. We will conserve them in another set. `refill liters` might help us see the difference between a full tank and almost empty tank of gas but for the moment they will be dropped.
But `refill_gas` is already by `gas type` """

df_drop = df.drop(columns=["specials","rain","sun","refill liters","refill gas"])


"# Dropped most of the 'unneccessary' Columns"
st.dataframe(df_drop.head())


"Uff...My instincts aren't formed yet. `21,5` is not in float form. I am going to have to get the Spanish decimal system to change to `.` "
df_drop[["distance", "consume", "temp_inside"]] = df_drop[["distance", "consume", "temp_inside"]].apply(lambda x: x.str.replace(',','.'))
df_drop[["distance", "consume", "temp_inside"]] = df_drop[["distance", "consume", "temp_inside"]].astype('float')
st.write(df_drop.dtypes)

"# Dummy values for `gas_type`"
dummy = pd.get_dummies(df_drop["gas_type"])
st.write(dummy.head())

"# Dropped `gas_type`"
df_drop_gas = df_drop.drop(columns = ["gas_type"])
st.write(df_drop_gas.head())

df_clean = pd.concat([df_drop_gas, dummy], axis=1)

df_clean.dtypes

df_clean.to_csv('/Users/claytonlouden/reto-data/data/clean.csv') 

st.write(sns.heatmap(df_clean))





