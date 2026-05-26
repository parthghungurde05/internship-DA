import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales & Revenue Analysis Dashboard")

df = pd.read_csv("data/sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()

col1,col2=st.columns(2)

col1.metric("Total Sales",total_sales)
col2.metric("Total Revenue",total_revenue)

region=st.sidebar.selectbox(
"Select Region",
["All"]+list(df["Region"].unique())
)

if region!="All":
    df=df[df["Region"]==region]

fig1=px.line(
df,
x="Date",
y="Revenue",
title="Revenue Trend"
)

st.plotly_chart(fig1)

fig2=px.bar(
df,
x="Product",
y="Revenue",
title="Top Products"
)

st.plotly_chart(fig2)

fig3=px.pie(
df,
names="Region",
values="Revenue",
title="Region Revenue"
)

st.plotly_chart(fig3)

st.dataframe(df)
