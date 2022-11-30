import numpy as np
import pandas as pd
import streamlit as st
st.write("This is program for Addition of 2 numbers")
num1 = st.number_input("1 st number")
num2 = st.number_input("2 nd number")
ans = num1+num2
st.write("Result is")
st.write(ans)
