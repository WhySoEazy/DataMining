import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
import sklearn

st.page_link("pages/main.py", label="Home", icon="🏠")
st.page_link("pages/data.py", label="Data", icon="📚")
st.page_link("pages/dashboard.py", label="Dashboard", icon="1️⃣")
st.page_link("pages/model.py", label="Model", icon="2️⃣")
st.page_link("http://www.google.com", label="Google", icon="🌎")