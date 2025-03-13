import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("This is my streamlit app for 13 March")
st.header("This module code is EDAB6808")
st.subheader("This is a fun and interactive module")
# Generate random time series data


variable = st.button("This is my button")
if variable:
   time_series = np.random.randn(2000)
   fig, ax = plt.subplots()
   # Plot the time series
  plt.set_title("Random 100-Unit Time Series")
  plt.set_xlabel("Time")
  plt.set_ylabel("Value")
  st.pyplot(fig)
