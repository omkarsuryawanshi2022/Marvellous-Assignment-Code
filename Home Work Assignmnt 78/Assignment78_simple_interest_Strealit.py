
import streamlit as st

# Application title
st.title("Simple Interest Calculator")

# Input fields
principal = st.number_input(
    "Enter Principal Amount (₹):",
    min_value=0.0,
    value=1000.0
)

rate = st.number_input(
    "Enter Rate of Interest (%):",
    min_value=0.0,
    value=5.0
)

time = st.number_input(
    "Enter Time Period (Years):",
    min_value=0.0,
    value=2.0
)

# Calculate button
if st.button("Calculate"):
    # Simple Interest Formula
    simple_interest = (principal * rate * time) / 100

    # Display results
    st.success(f"Simple Interest: ₹{simple_interest:.2f}")

    total_amount = principal + simple_interest
    st.info(f"Total Amount: ₹{total_amount:.2f}")
