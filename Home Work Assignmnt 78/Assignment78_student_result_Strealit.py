
import streamlit as st

# Application title
st.title("Student Result Calculator")

# Student name
name = st.text_input("Enter Student Name:")

# Subject marks
st.subheader("Enter Subject Marks")

subject1 = st.number_input(
    "Subject 1 Marks (out of 100):",
    min_value=0,
    max_value=100,
    value=0
)

subject2 = st.number_input(
    "Subject 2 Marks (out of 100):",
    min_value=0,
    max_value=100,
    value=0
)

subject3 = st.number_input(
    "Subject 3 Marks (out of 100):",
    min_value=0,
    max_value=100,
    value=0
)

# Calculate result
if st.button("Calculate Result"):

    if name.strip() == "":
        st.warning("Please enter the student's name.")

    else:
        # Calculate total and percentage
        total = subject1 + subject2 + subject3
        percentage = (total / 300) * 100

        # Display student details
        st.subheader("Student Result")
        st.write("Student Name:", name)
        st.write("Total Marks:", total, "/ 300")
        st.write(f"Percentage: {percentage:.2f}%")

        # Check pass or fail
        if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
            st.success("Result: PASS")
        else:
            st.error("Result: FAIL")
