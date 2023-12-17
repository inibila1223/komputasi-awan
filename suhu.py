import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('Nabila :sparkles:')
st.subheader('Plot')

nama = st.text_input('Nama', 'Nabila', label_visibility='collapsed')
st.write('Halo ', nama)

f1 = st.number_input('f1= ', value=1)


st.caption('source: Nabila.xyz')
