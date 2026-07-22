import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="📊")

st.title("📊 Loan Dataset Explorer")

df = pd.read_csv("data/train.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.subheader("Column Information")

st.write(df.dtypes)

st.subheader("Missing Values")

st.write(df.isnull().sum())