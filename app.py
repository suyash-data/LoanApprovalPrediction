import streamlit as st

st.set_page_config(
    page_title="AI Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Loan Approval Prediction Platform")

st.markdown("---")

st.markdown("""
## Welcome

This application predicts whether a loan application is likely to be **Approved** or **Rejected** using Machine Learning.

### Features

- 📊 Dataset Explorer
- 📈 Interactive Visualizations
- 🤖 Loan Approval Prediction
- 🏦 Banking Dashboard
- 📑 Project Information

Use the **sidebar** to navigate between pages.
""")

st.info("👈 Select a page from the sidebar.")