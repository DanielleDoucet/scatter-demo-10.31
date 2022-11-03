import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

#import WHO dataset with pandas

who_data=pd.read_csv("WHO_data (1).csv")
st.write(who_data)

st.sidebar.header("Pick two variables for your scatterplot")
x_val=st.sidebar.selectbox("Pick your x axis", who_data.select_dtypes(include=np.number).columns.tolist())
y_val=st.sidebar.selectbox("Pick your y axis", who_data.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(who_data, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=(x_val,y_val)
)
st.altair_chart(scatter, use_container_width=True)

#calculate the correlation
corr=round ((who_data[x_val]).corr(who_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")
