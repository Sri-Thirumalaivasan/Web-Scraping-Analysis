import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('cleaned_laptops_data.csv')

# Dashboard
st.title("Laptops Data Dashboard")
st.write("Visualize scraped laptops data")

# Table
st.dataframe(data)

# Plot
fig, ax = plt.subplots()
data.plot(kind='scatter', x='Price', y='Rating', ax=ax, color='blue')
plt.title("Price vs Rating")
st.pyplot(fig)
