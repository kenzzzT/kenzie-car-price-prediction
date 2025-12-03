import streamlit as st
import numpy as np
import pandas as pd
import joblib


with open("model_linear.pkl", "rb") as file:
model = joblib.load(file)


st.title("Car Price Prediction App (Linear Regression)")


brand = st.selectbox("Brand", ["Tesla", "BMW", "Audi", "Ford"])
year = st.number_input("Tahun Mobil", min_value=1990, max_value=2025, step=1)
engine = st.number_input("Engine Size (L)", min_value=1.0, max_value=6.0, step=0.1)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
trans = st.selectbox("Transmission", ["Manual", "Automatic"])
mileage = st.number_input("Mileage (km)", min_value=0, step=100)
condition = st.selectbox("Condition", ["New", "Used", "Like New"])

if st.button("Prediksi Harga"):
    data = pd.DataFrame([{
        "Brand": brand,
        "Year": year,
        "Engine Size": engine,
        "Fuel Type": fuel,
        "Transmission": trans,
        "Mileage": mileage,
        "Condition": condition
    }])

    result = model.predict(data)[0]

    st.success(f" Prediksi Harga Mobil: **USD {result:,.2f}**")

