from config.configuration import engine
import pandas as pd
# import streamlit as st
# import seaborn as sns

def stats_df(df):
    """
    Function to create an histogram to compare E10 and SP98 fuel.
    Args: 
        None
    Returns:
        A seaborn basic histogram
    """
    stats = df.groupby("gas_type").consume.agg(["std", "mean", "median", "min", "max"])

    return stats
