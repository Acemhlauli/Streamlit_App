import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("This is my Streamlit app for 13 March")
st.header("This module code is EDAB6808")
st.subheader("This is a fun and interactive module")

# Button to generate the plot
button_clicked = st.button("This is my button")

if button_clicked:
    # Generate random time series data
    time_series = np.random.randn(200)
    
    # Create figure and axis
    fig, ax = plt.subplots()
    
    # Plot the time series
    ax.plot(time_series)
    
    # Set labels and title
    ax.set_title("Random 200-Unit Time Series")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    # Display the plot in Streamlit
    st.pyplot(fig)
