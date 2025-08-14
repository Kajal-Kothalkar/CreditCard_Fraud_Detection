# Streamlit app with all 30 features
import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Credit Card Fraud Detection App")

# Input for all 30 features
features = []
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

st.markdown("Enter all transaction features:")

for name in feature_names:
    val = st.number_input(name, value=0.0, step=0.1)
    features.append(val)

# Prediction
if st.button("Predict"):
    input_data = np.array([features])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]
    prob = model.predict_proba(scaled_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraudulent Transaction! (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Legitimate Transaction (Probability: {1 - prob:.2f})")
