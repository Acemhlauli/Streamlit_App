import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("This is my streamlit app for 13 March")
st.heading("This module code is EDAB6808")
st.subheading("This is a fun and interactive module")
# Generate random time series data


variable = st.button("This is my button")
if variable:
   time_series = np.random.randn(2000)
   fig, ax = plt.subplots()
   # Plot the time series
  plt.plot(time_series)
  plt.title("Random 100-Unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Value")
  st.pyplot(fig)
