import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide")
st.title("Earthquake Data Analysis (MVP)")

data_path = "data/earthquakes_last30.csv"
df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["time_iso"]).dt.date

min_date, max_date = df["date"].min(), df["date"].max()
date_range = st.sidebar.date_input(
    "Select date range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)
if isinstance(date_range, tuple):
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

st.metric("Total Earthquakes", len(filtered))
if "magnitude" in filtered and filtered["magnitude"].notna().any():
    st.metric("Average Magnitude", f"{filtered['magnitude'].mean():.2f}")

# Handle negative magnitudes for sizing  
filtered['magnitude_size'] = filtered['magnitude'].clip(lower=0.1)  # Minimum size of 0.1

fig = px.scatter_map(
    filtered,
    lat="latitude",
    lon="longitude",
    color="magnitude",
    size="magnitude_size",
    hover_name="place",
    hover_data=["time_iso", "depth_km"],
    color_continuous_scale="Viridis",
    size_max=12,
    zoom=1,
    height=600,
)
st.plotly_chart(fig, use_container_width=True)