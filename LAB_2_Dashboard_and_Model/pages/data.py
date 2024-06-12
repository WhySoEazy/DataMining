import streamlit as st
import pandas as pd

st.header("Data Overview")
path = "C:/Users/triet/OneDrive/Desktop/DataMining/LAB_2_Dashboard_and_Model/AirlineQualityRating.csv"
df = pd.read_csv(path ,  index_col=0)
df

st.header("Data Describe")
df_info = df.describe()
df_info