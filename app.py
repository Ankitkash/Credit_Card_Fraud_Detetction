import streamlit as st
import pickle
import numpy as np

st.title("💳 Credit Card Fraud Detection")

model = pickle.load(open("credit_card_model.pkl", "rb"))

features = []

time = st.number_input("Time")
features.append(time)

for i in range(1, 29):
    value = st.number_input(f"V{i}")
    features.append(value)

amount = st.number_input("Amount")
features.append(amount)

if st.button("Predict"):
    input_data = np.array([features])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Genuine Transaction")
