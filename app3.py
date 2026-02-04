import streamlit as st

st.title("basic calculator app")

num1=st.number_input("enter the first number:")
num2=st.number_input("enter the second number:")
operation = st.selectbox(
    "Select operation:",
    ["add", "subtract", "multiply", "divide"]
)

if st.button("Calculate"):
    if operation == "add":
        st.write("Result:", num1 + num2)

    elif operation == "subtract":
        st.write("Result:", num1 - num2)

    elif operation == "multiply":
        st.write("Result:", num1 * num2)

    elif operation == "divide":
        if num2 != 0:
            st.write("Result:", num1 / num2)
        else:
            st.error("Cannot divide by zero")