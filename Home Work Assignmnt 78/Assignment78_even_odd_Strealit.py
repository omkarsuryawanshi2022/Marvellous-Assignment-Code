
import streamlit as st

# Application title
st.title("Even or Odd Number Checker")

# Accept an integer from the user
number = st.number_input(
    "Enter an Integer:",
    value=0,
    step=1
)

# Check button
if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{number} is an Even Number.")
    else:
        st.success(f"{number} is an Odd Number.")
