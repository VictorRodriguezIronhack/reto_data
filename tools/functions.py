from config.configuration import engine
import pandas as pd
# import streamlit as st
# import seaborn as sns

def stats_df(df):
    """
    Function to create a a grouped dataframe and show it's statistics 
    (Standard deviation, mean, median, minimum and maximum).
    Args: 
        df: dataframe
    Returns:
        df: grouped dataframe and aggregated statistics for consume
    """
    stats = df.groupby("gas_type").consume.agg(["std", "mean", "median", "min", "max"])

    return stats