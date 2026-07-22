import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.title("ℹ️ About the Project")

st.markdown("---")

st.header("🏦 AI Loan Approval Prediction Platform")

st.write("""
This project predicts whether a loan application is likely to be **Approved** or **Rejected**
using Machine Learning.

It is developed as part of an internship project to demonstrate data preprocessing,
model training, evaluation, and deployment using Streamlit.
""")

st.markdown("## 🛠️ Technologies Used")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib
- XGBoost
""")

st.markdown("## 🤖 Machine Learning Model")

st.success("Logistic Regression")

st.markdown("## 📊 Dataset")

st.info("""
Loan Approval Prediction Dataset

Features:
- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

Target:
Loan Status
""")

st.markdown("---")
