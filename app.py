import streamlit as st
import numpy as np 
import pandas as pd

df = pd.DataFrame(np.random.randn(500,2) / [50, 50] + [37,75 -122, 4])
st.map(df)

x = st.slider('Select a value')
st.write(x, 'squared is ', x*x)
