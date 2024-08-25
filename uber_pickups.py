import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# import matplotlib.pyplot as plt



st.write("""
# :rainbow[Robokids World!]

> Place for young minds to develop their robotic skills...
---
"""
         )

st.write("Hello , *techies* :computer: **study well**")

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

st.write('Hello Data Nexus!!')
'hi this is magic!:100:'
':material/menu:'

st.write(pd.DataFrame({'first column': [10, 30, 50, 70],
                   'second column': [3, 4, 5, 6]}))

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f"col_{i}" for i in range(20) ]

)
# st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)


dataframe = pd.DataFrame(
    np.random.randn(20, 3),
    columns= list('ABC')

)
st.line_chart(dataframe)

st.bar_chart(dataframe['A'])

number = st.slider("Pick a number", 0, 100)
st.write(number)
file = st.file_uploader('Pick a file!')

df = pd.DataFrame(np.random.randint(10, 100, (20, 3)), columns=list('ABC'))
c = alt.Chart(df).mark_circle().encode(x='A', y='C', color='C')

st.altair_chart(c, use_container_width=True)