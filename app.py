#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

# Title and Introduction
st.title('Welcome to My Streamlit App!')
st.write('This is a simple Streamlit web app.')

# Smaller Heading
st.markdown("### This is a smaller heading")

# Custom Styling
st.markdown("""
<style>
.big-font { font-size:30px !important; }
</style>
<p class="big-font">This is large text!</p>
""", unsafe_allow_html=True)

# Button Functionality
if st.button('Click me'):
    st.write('Button clicked!')

# Interactive Section
st.title('Interactive Streamlit App')

name = st.text_input('Enter your name:')
st.write(f'Hello, {name}!')

age = st.slider('Select your age:', 0, 100, 25)
st.write(f'You are {age} years old.')

# Data Visualization Section
st.title('Data Visualization Example')

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)

# File Upload Section
st.title('Upload Your File')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    try:
        # Read the uploaded file into a DataFrame
        data = pd.read_csv(uploaded_file)
        st.write('Uploaded Data:')
        st.write(data)
    except Exception as e:
        st.error(f"Error loading file: {e}")

