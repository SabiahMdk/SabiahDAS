import streamlit as st
import pandas as pd
st.title("streamlist text input")
name = st.text_input("enter your name")

age=st.slider("Select your age:",0,100,25)
st.write(f"your age is {age}")
if name:
    st.write(f"hello,{name}")
    
    
options = ["java script","java","c++","python"]
choice = st.selectbox("choose your favorite programming language:",options)
st.write(f"you selected {choice}.") 

data = {
    "name":["John","Colin","Kelvin","Matte"],
    "AGE":[23,17,29,27],
    "CITY":["Nigeria","New york","India","Chicago"]
}
df = pd.DataFrame(data)
st.write(df)