
import streamlit as st

# Application title
st.title("Celsius to Fahrenheit Converter")

# Accept temperature in Celsius
celsius = st.number_input(
    "Enter Temperature in Celsius (°C):",
    value=0.0
)

# Convert button
if st.button("Convert"):
    # Conversion formula
    fahrenheit = (celsius * 9 / 5) + 32

    # Display result
    st.success(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
