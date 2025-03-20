import streamlit as st
import pickle
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# Load the model and dataset
with open('pipe.pkl', 'rb') as pickled_in:
    pipe = pickle.load(pickled_in)
cars_df = pd.read_csv('car_price_dataset.csv')

# Print column names for debugging
print("Columns in the dataset:", cars_df.columns)

st.title("Car Price Prediction :car:")

# User inputs
car_brand = st.selectbox("Brand", cars_df['Brand'].unique())
car_model = st.selectbox("Model", cars_df["Model"].unique())
year_sorted = cars_df['Year'].sort_values(ascending=True)
car_year = st.selectbox("Year", year_sorted.unique())
car_engine_sorted = cars_df['Engine_Size'].sort_values(ascending=True)
car_engine = st.select_slider("Engine Size (in litres)", car_engine_sorted.unique())
car_fuel = st.selectbox("Fuel Type", cars_df["Fuel_Type"].unique())
car_transmission = st.selectbox("Transmission Type", cars_df["Transmission"].unique())
car_mileage = st.number_input("Mileage", min_value=12247, max_value=299447)

if st.button("Predict"):
    # Create a DataFrame from user inputs
    input_data = pd.DataFrame([{
        'brand': car_brand,
        'model': car_model,
        'year': car_year,
        'engine_size': car_engine,
        'fuel_type': car_fuel,
        'transmission': car_transmission,
        'mileage': car_mileage
    }])

    # Ensure the columns are in the correct order and match the dataset
    input_data = input_data[['brand', 'model', 'year', 'engine_size', 'fuel_type', 'transmission', 'mileage']]

    # Print input data for debugging
    print("Input data for prediction:", input_data)

    # Predict the price
    try:
        predicted_price = int(pipe.predict(input_data)[0])
        st.title(f"The predicted price of the car is: {predicted_price}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")