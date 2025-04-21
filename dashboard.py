import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Customer Segmentation & Churn Dashboard")

# Load RFM data
df = pd.read_csv('rfm_final.csv')

# Sidebar segment selector
segment = st.sidebar.selectbox("Choose Cluster Segment", sorted(df['Cluster'].unique()))

# Filtered view
filtered = df[df['Cluster'] == segment]

# KPIs
st.metric("Average Recency", round(filtered['Recency'].mean(), 1))
st.metric("Average Frequency", round(filtered['Frequency'].mean(), 1))
st.metric("Average Monetary", round(filtered['Monetary'].mean(), 1))

# RFM Distribution
st.subheader("RFM Distributions")
fig, ax = plt.subplots(1, 3, figsize=(15, 4))

sns.histplot(filtered['Recency'], ax=ax[0], kde=True).set_title("Recency")
sns.histplot(filtered['Frequency'], ax=ax[1], kde=True).set_title("Frequency")
sns.histplot(filtered['Monetary'], ax=ax[2], kde=True).set_title("Monetary")

st.pyplot(fig)
