import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Airline Quality Rating")

st.header("Data Overview")
path = "C:/Users/triet/OneDrive/Documents/DBM302m/Project/archive/AirlineQualityRating.csv"
df = pd.read_csv(path ,  index_col=0)
head = df.head(10)
head

#1
st.header("Bar Chart")
age_count = df['Age'].value_counts()
st.bar_chart(age_count)

#2
st.header("Pie Chart")
label_1 = 'Select your option: '
category = ["Gender", "Customer Type", "Type of Travel" , "Class" , "Satisfaction"]
selected = st.selectbox(label=label_1 , options=category)
count = df[selected].value_counts()
fig = plt.pie(count , labels=df[selected].unique() , autopct="%1.1f%%" , radius=0.75)
plt.title(selected)
st.pyplot(plt.gcf())


#3
st.header("Bar Chart")
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

#4 Optional
st.header("Age")
label1 = 'Select Age: '
label2 = 'Select Customer Type:	'
label3 = 'Select Type of Travel: '
label4 = 'Select Class: '
Age = ['Children (1-15)' , 'Teenager (16-30)' , 'Middle-Age (31-65)' , 'Old (66-80)']
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
elif selected1 == 'Old (66-80)':
    age = df[['Age', 'Customer Type' , 'Type of Travel' , 'Class']][df['Age'] <= 80][df['Age'] >= 66][df['Customer Type'] == selected2][df['Type of Travel'] == selected3][df['Class'] == selected4]
    age_counts = age['Age'].value_counts().sort_index()
    st.bar_chart(age_counts)
elif selected1 == 'Children (1-15)':
    age = df[['Age', 'Customer Type' , 'Type of Travel' , 'Class']][df['Age'] <= 15][df['Age'] >= 1][df['Customer Type'] == selected2][df['Type of Travel'] == selected3][df['Class'] == selected4]
    age_counts = age['Age'].value_counts().sort_index()
    st.bar_chart(age_counts)

#5 Headmap
catcol = []
numcol = []

for col in df.columns :
    if df[col].dtype == 'object':
        catcol.append(col)
    else :
        numcol.append(col)

from sklearn.preprocessing import LabelEncoder

df_ = df.copy()

label_encoding = {}
for cat in catcol:
    encoder = LabelEncoder()
    df_[cat] = encoder.fit_transform(df_[cat])
    label_encoding[cat] = encoder

df_

plt.figure(figsize=(50 , 30))
fig = sns.heatmap(df_.corr() , annot=True , cmap="YlGnBu")
st.pyplot(plt)