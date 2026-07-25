import streamlit as st
import pandas as pd
import numpy as np


### Title of the application
st.title("hello streamlit")

###  Display a simple text
st.write("This is a simple text")

#### creating a simple dataframe
df = pd.DataFrame({
    'data1':[1,2,3,4,5],
    'data2':[10,20,30,40,50]
})
### display the datframe
st.write("Here is my sample dataframe")
st.write(df)

### creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
