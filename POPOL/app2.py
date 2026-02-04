import streamlit as st

st.title("my age and city app")

age= st.number_input("enter your age0", 1 ,100)
city= st.selectbox("select your city",["mumbai","delhi","banglore","chennai"])

if st.button("show details"):
    st.write("age",age)
    st.writw("city",city)