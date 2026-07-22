import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/loan_model.pkl")

st.set_page_config(page_title="Loan Prediction", page_icon="🤖")

st.title("🤖 Loan Approval Prediction")

st.write("Fill in the applicant details below.")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])

with col2:
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Amount Term", min_value=0)
    credit_history = st.selectbox("Credit History", [1.0, 0.0])
    property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

if st.button("Predict Loan Status"):

    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0

    dependents = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3+": 3
    }[dependents]

    education = 0 if education == "Graduate" else 1
    self_employed = 1 if self_employed == "Yes" else 0

    property_area = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }[property_area]

    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]

    confidence = max(probability) * 100

    st.markdown("---")

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.metric("Prediction Confidence", f"{confidence:.2f}%")