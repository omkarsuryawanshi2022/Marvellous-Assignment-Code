
import streamlit as st

# Application title
st.title("Addition of Two Numbers")

# Input fields
num1 = st.number_input("Enter First Number:")
num2 = st.number_input("Enter Second Number:")

# Add button
if st.button("Add"):
    result = num1 + num2
    st.success(f"Addition Result: {result}")
