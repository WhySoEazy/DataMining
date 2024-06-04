import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.title("Airline Quality Rating")

st.header("Data Overview")
path = "AirlineQualityRating.csv"
df = pd.read_csv(path ,  index_col=0)
df

#1
st.header("Age Distribution")
age_count = df['Age'].value_counts()
st.bar_chart(age_count)

#2
st.header("Rate")
label_1 = 'Select your option: '
category = ["Gender", "Customer Type", "Type of Travel" , "Class" , "Satisfaction"]
selected = st.selectbox(label=label_1 , options=category)
count = df[selected].value_counts()
fig = plt.pie(count , labels=df[selected].unique() , autopct="%1.1f%%" , radius=0.75)
plt.title(selected)
st.pyplot(plt.gcf())


#3
st.header("Rating")
label_2 = 'Select service: '
service = ["Departure and Arrival Time Convenience",
            "Ease of Online Booking", 
            "Check-in Service" ,  
            "Online Boarding" ,
            "Gate Location" ,
            "On-board Service" ,
            "Seat Comfort" ,
            "Leg Room Service" ,
            "Cleanliness" ,
            "Food and Drink" ,
            "In-flight Service" ,
            "In-flight Wifi Service" ,
            "In-flight Entertainment" ,
            "Baggage Handling"]
selected_1 = st.selectbox(label=label_2 , options=service)
service_rank = df[selected_1].value_counts()
st.bar_chart(service_rank)

#Optional
st.header("Information")
label1 = 'Select Age: '
label2 = 'Select Customer Type:	'
label3 = 'Select Type of Travel: '
label4 = 'Select Class: '
Age = ['Children (1-15)' , 'Teenager (16-30)' , 'Middle-Age (31-65)' , 'Old (66-85)']
customer_type = ['First-time' , 'Returning']
type_of_travel = ['Business' , 'Personal']
classes = ['Business' , 'Economy' , 'Economy Plus']
selected1 = st.selectbox(label=label1 , options=Age)
selected2 = st.selectbox(label=label2 , options=customer_type)
selected3 = st.selectbox(label=label3 , options=type_of_travel)
selected4 = st.selectbox(label=label4 , options=classes)
if selected1 == 'Teenager (16-30)':
    age = df[['Age', 'Customer Type' , 'Type of Travel' , 'Class']][df['Age'] <= 30][df['Age'] >= 16][df['Customer Type'] == selected2][df['Type of Travel'] == selected3][df['Class'] == selected4]
    age_counts = age['Age'].value_counts().sort_index()
    st.bar_chart(age_counts)
elif selected1 == 'Middle-Age (31-65)':
    age = df[['Age', 'Customer Type' , 'Type of Travel' , 'Class']][df['Age'] <= 65][df['Age'] >= 31][df['Customer Type'] == selected2][df['Type of Travel'] == selected3][df['Class'] == selected4]
    age_counts = age['Age'].value_counts().sort_index()
    st.bar_chart(age_counts)
elif selected1 == 'Old (66-85)':
    age = df[['Age', 'Customer Type' , 'Type of Travel' , 'Class']][df['Age'] <= 85][df['Age'] >= 66][df['Customer Type'] == selected2][df['Type of Travel'] == selected3][df['Class'] == selected4]
    age_counts = age['Age'].value_counts().sort_index()
    st.bar_chart(age_counts)
elif selected1 == 'Children (1-15)':
    age = df[['Age', 'Customer Type' , 'Type of Travel' , 'Class']][df['Age'] <= 15][df['Age'] >= 1][df['Customer Type'] == selected2][df['Type of Travel'] == selected3][df['Class'] == selected4]
    age_counts = age['Age'].value_counts().sort_index()
    st.bar_chart(age_counts)

#Satisfaction by Gender, Class, Type of travel, Customer type
st.write("### Satisfaction by Categorical Values")
selected_value = st.radio("Select options",['Gender','Class','Type of Travel','Customer Type'])
selected_value_type = df[selected_value].unique()

satisfaction_categorical_chart = alt.Chart(df).mark_bar().encode(
    x=selected_value,
    y='count()',
    color='Satisfaction'
).properties(
    width=600,
    height=400
)
st.altair_chart(satisfaction_categorical_chart, use_container_width=True)

# Flight Distance Distribution
st.write("### Flight Distance Distribution")
selected_value_flight = st.radio("Select options for flight distance",['Gender','Class','Type of Travel','Customer Type'])
distance_chart = alt.Chart(df).mark_bar().encode(
    alt.X("Flight Distance", bin=True),
    y='count()',
    color =selected_value_flight
).properties(
    width=600,
    height=400
)
st.altair_chart(distance_chart, use_container_width=True)

# Departure Delay vs. Arrival Delay
st.write("### Departure Delay vs. Arrival Delay")
delay_chart = alt.Chart(df).mark_point().encode(
    x='Departure Delay',
    y='Arrival Delay',
    color='Satisfaction',
    tooltip=['Departure Delay', 'Arrival Delay', 'Satisfaction']
).properties(
    width=600,
    height=400
)
st.altair_chart(delay_chart, use_container_width=True)

#5 Headmap

st.write("### Correlation Heatmap")

numeric_data = df.select_dtypes(include=['float64', 'int64'])
fig, ax = plt.subplots(figsize=(10, 8))  
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)  
st.pyplot(fig) 