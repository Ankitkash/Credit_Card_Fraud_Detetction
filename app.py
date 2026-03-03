import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Credit Card Fraud Detection")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to check fraud probability")

# Load model
model = pickle.load(open("model.pkl", "rb"))

features = []

# V1 to V28
for i in range(1, 29):
    value = st.number_input(f"V{i}", value=0.0)
    features.append(value)

# Amount
amount = st.number_input("Amount", value=0.0)
features.append(amount)

if st.button("Predict"):

    input_data = np.array([features])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Result:")

    if prediction[0] == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Genuine Transaction")

    st.write(f"Fraud Probability: {probability:.2%}")
