import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import sklearn

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("C:/Users/triet/OneDrive/Documents/DBM302m/Project/archive/AirlineQualityRating.csv")
    return data

data = load_data()

# Title of the app
st.title("Airline Quality Ratings")

# Display the dataset
st.subheader("Dataset")
st.dataframe(data)

# Summary statistics
st.subheader("Summary Statistics")
st.write(data.describe())

# User Feedback Form
st.subheader("User Feedback Form")

# Select age 
age = st.number_input("Age", min_value=7)

# Select Gender
gender = st.selectbox("Gender", options=["Male", "Female"])

# Select Customer Type
customer_type = st.selectbox("Customer Type", options=data['Customer Type'].unique())

# Select Type of Travel
type_of_travel = st.selectbox("Type of Travel", options=data['Type of Travel'].unique())

# Select Class
travel_class = st.selectbox("Class", options=data['Class'].unique())

# Input Flight Distance
flight_distance = st.number_input("Flight Distance", min_value=0)

# Input Departure Delay
departure_delay = st.number_input("Departure Delay", min_value=0)

# Input Arrival Delay
arrival_delay = st.number_input("Arrival Delay", min_value=0)

# Ratings (1-5)
def rating(label):
    return st.number_input(label, min_value=1, max_value=5, step=1)

departure_arrival_time_convenience = rating("Departure and Arrival Time Convenience")
ease_of_online_booking = rating("Ease of Online Booking")
check_in_service = rating("Check-in Service")
online_boarding = rating("Online Boarding")
gate_location = rating("Gate Location")
on_board_service = rating("On-board Service")
seat_comfort = rating("Seat Comfort")
leg_room_service = rating("Leg Room Service")
cleanliness = rating("Cleanliness")
food_and_drink = rating("Food and Drink")
in_flight_service = rating("In-flight Service")
in_flight_wifi_service = rating("In-flight Wifi Service")
in_flight_entertainment = rating("In-flight Entertainment")
baggage_handling = rating("Baggage Handling")

##Function handle data
def load_scaler_model():
    with open(r'C:/Users/triet/OneDrive/Documents/DBM302m/Ex/scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    with open(r'C:/Users/triet/OneDrive/Documents/DBM302m/Ex/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return scaler,model

def preprocessing_data(data):
    df = pd.DataFrame([data])

    feature_order = [
    'Gender', 'Age', 'Customer Type', 'Type of Travel', 'Class', 'Flight Distance', 
    'Departure Delay', 'Arrival Delay', 'Departure and Arrival Time Convenience', 
    'Ease of Online Booking', 'Check-in Service', 'Online Boarding', 'Gate Location', 
    'On-board Service', 'Seat Comfort', 'Leg Room Service', 'Cleanliness', 'Food and Drink', 
    'In-flight Service', 'In-flight Wifi Service', 'In-flight Entertainment', 'Baggage Handling'
]
    df_ = df.copy()
    gender_mapping = {'Female': 0, 'Male': 1}
    customer_type_mapping = {'First-time': 0, 'Returning': 1}
    type_of_travel_mapping = {'Business': 0, 'Personal': 1}
    class_mapping = {'Business': 0, 'Economy': 1, 'Economy Plus': 2}

    df_['Gender'] = df_['Gender'].map(gender_mapping)
    df_['Customer Type'] = df_['Customer Type'].map(customer_type_mapping)
    df_['Type of Travel'] = df_['Type of Travel'].map(type_of_travel_mapping)
    df_['Class'] = df_['Class'].map(class_mapping)
    
    scaler, model = load_scaler_model()
    df_ = df_.reindex(columns=feature_order)   
    df_scaled = scaler.transform(df_) 

    return df_scaled, model


# Submit button
if st.button("Submit"):
    # Collect feedback
    feedback = {
        "Age": age,
        "Gender": gender,
        "Customer Type": customer_type,
        "Type of Travel": type_of_travel,
        "Class": travel_class,
        "Flight Distance": flight_distance,
        "Departure Delay": departure_delay,
        "Arrival Delay": arrival_delay,
        "Departure and Arrival Time Convenience": departure_arrival_time_convenience,
        "Ease of Online Booking": ease_of_online_booking,
        "Check-in Service": check_in_service,
        "Online Boarding": online_boarding,
        "Gate Location": gate_location,
        "On-board Service": on_board_service,
        "Seat Comfort": seat_comfort,
        "Leg Room Service": leg_room_service,
        "Cleanliness": cleanliness,
        "Food and Drink": food_and_drink,
        "In-flight Service": in_flight_service,
        "In-flight Wifi Service": in_flight_wifi_service,
        "In-flight Entertainment": in_flight_entertainment,
        "Baggage Handling": baggage_handling
    }
    st.write(feedback)
    df_, model= preprocessing_data(feedback)
    result = model.predict(df_)
    st.subheader('Result:')
    if result[0] == 0 :
        st.write('Disatisfaction')
    else:
        st.write('Satisfaciton')