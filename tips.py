# Importing Toolkit

import streamlit as st
import pandas as pd
import numpy as np
import plotly as px

# Page Settings

st.set_page_config( page_title = "Tips Dashbord", 
                    page_icon=None, 
                    layout="wide", 
                    initial_sidebar_state="auto" )

# Loading Data

df = pd.read_csv('tips.csv')

# Side Bar

st.sidebar.header("Tips Dashboard")
st.sidebar.image('tips.jpg')
st.sidebar.write("This dashboard is using Tips datasets from Kaggle for educational purposes.")
st.sidebar.write("")

## Filters

st.sidebar.write("Filter Your Data")

cat_filter = st.sidebar.selectbox("Categorical Filtering",(None, 'sex', 'smoker', 'day', 'time'))
num_filter = st.sidebar.selectbox("Numerical Filtering",(None, 'total_bill', 'tip'))
row_filter = st.sidebar.selectbox("Row Filtering",(None, 'sex', 'smoker', 'day', 'time'))
col_filter = st.sidebar.selectbox("Column Filtering",(None, 'sex', 'smoker', 'day', 'time'))

st.sidebar.write("")
st.sidebar.markdown("Made with :heart_eyes: by Ds. [Ziad Tarik](https://google.com)")

# Body

# Row A
a1, a2, a3, a4 = st.columns(4)

a1.metric("Max, Total Bill", df['total_bill'].max())
a2.metric("Max, Tip", df['tip'].max())
a3.metric("Min, Total Bill", df['total_bill'].min())
a4.metric("Min, Tip", df['tip'].min())

# Row B
st.subheader("Total Bills vs. Tips")
fig = px.scatter(data_frame = df,
                x = 'total_bill',
                y = 'tip',
                color = cat_filter,
                size = num_filter,
                facet_col = col_filter,
                facet_row = row_filter)
st.plotly_chart(fig, use_container_with = True)

# Row C
c1, c2, c3 = st.columns((4,3,3))

with c1:
     st.text("Sex vs. Total Bill",)
     fig = px.bar(data_frame = df, 
                  x = 'sex', 
                  y = 'total_bill', 
                  color = cat_filter)
     st.plotly_chart(fig, use_container_with = True)

with c2:
     st.text("Smoker vs. Total Bill")
     fig = px.pie(data_frame = df,
                    names="smoker", 
                    values="total_bill", 
                    color = cat_filter)
     st.plotly_chart(fig, use_container_with = True)

with c3:
     st.text("Day vs. Tip")
     fig = px.pie(data_frame = df, 
                    names="day", 
                    values="tip", 
                    color = cat_filter,
                    hole = 0.3)
     st.plotly_chart(fig, use_container_with = True)          
