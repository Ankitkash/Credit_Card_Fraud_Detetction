import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("credit_card_model.pkl", "rb"))

st.title("Credit Card Fraud Detection")
st.write("Enter transaction details to check fraud probability")

# Example inputs (adjust according to your dataset)
amount = st.number_input("Transaction Amount", min_value=0.0)
v1 = st.number_input("V1")
v2 = st.number_input("V2")

if st.button("Predict"):

    input_data = np.array([[amount, v1, v2]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraudulent Transaction")
    else:
        st.success("Genuine Transaction")