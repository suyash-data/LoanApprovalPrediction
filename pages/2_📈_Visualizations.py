import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Visualizations", page_icon="📈")

st.title("📈 Loan Dataset Visualizations")

# Load dataset
df = pd.read_csv("data/train.csv")

# -------------------------
# Loan Status Distribution
# -------------------------

st.subheader("Loan Approval Distribution")

fig = px.pie(
    df,
    names="Loan_Status",
    title="Approved vs Rejected Loans"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Property Area
# -------------------------

st.subheader("Applicants by Property Area")

fig = px.histogram(
    df,
    x="Property_Area",
    color="Property_Area"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Education
# -------------------------

st.subheader("Education Distribution")

fig = px.histogram(
    df,
    x="Education",
    color="Education"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Applicant Income
# -------------------------

st.subheader("Applicant Income Distribution")

fig = px.histogram(
    df,
    x="ApplicantIncome",
    nbins=30
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Loan Amount
# -------------------------

st.subheader("Loan Amount Distribution")

fig = px.histogram(
    df,
    x="LoanAmount",
    nbins=30
)

st.plotly_chart(fig, use_container_width=True)