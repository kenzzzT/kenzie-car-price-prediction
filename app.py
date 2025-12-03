import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Car Price Prediction App (Tanpa Pickle)")

# Load dataset
df = pd.read_csv("car_price_prediction_.csv")

# Pilih fitur
X = df[['year', 'km_driven', 'mileage']]
y = df['selling_price']

# Train model langsung di Streamlit
model = LinearRegression()
model.fit(X, y)

# Input user
year = st.number_input("Tahun Mobil", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometer Tempuh", min_value=0)
mileage = st.number_input("Milege (kmpl)", min_value=0.0, max_value=50.0, step=0.1)

# Prediksi
if st.button("Prediksi Harga"):
    features = [[year, km_driven, mileage]]
    pred = model.predict(features)[0]
    st.success(f"Harga Mobil Diprediksi: Rp {pred:,.0f}")
