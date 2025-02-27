# import streamlit 
import streamlit as st
# import pandas 
import pandas as pd

# create a function to create BMI Calculator

st.title("BMI Calculator")
height = st.slider("Enter Your Height (in cm)",100,250,175)
weight = st.slider("Enter Your Weight (in Kg)",40,200,70)

bmi = weight / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:2f}")

st.write("### BMI Categories ###")
st.write("_ Underweight: BMI less than 18.5")
st.write("_ Normal Weight: BMI between 18.5 and 24.9")
st.write("_ Over Weight: BMI between 25 and 29.9")
st.write("_ Obesity Weight: BMI 30 or greater") 
