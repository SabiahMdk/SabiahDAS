import streamlit as st

st.title("streamlist text input")
name = st.text_input("enter your name")

age=st.slider("Select your age:",0,100,25)
st.write(f"your age is {age}")
if name:
    st.write(f"hello,{name}")
    
    
options = ["java script","java","c++","python"]
choice = st.selectbox("choose your favorite programming language:",options)
st.write(f"you selected  {choice}.")  