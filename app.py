
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Netflix Trend Forecasting",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Netflix Trend Forecasting Dashboard")
st.write(
    "Explore historical Netflix content additions, "
    "forecasting results, and future baseline projections."
)

# Load data
history = pd.read_csv("monthly_content_trends.csv")
evaluation = pd.read_csv("models/model_evaluation.csv")
future = pd.read_csv("models/future_forecast.csv")

history["date_added"] = pd.to_datetime(history["date_added"])
future["date"] = pd.to_datetime(future["date"])

# Sidebar
st.sidebar.header("Dashboard Filters")

start_date = st.sidebar.date_input(
    "Start date",
    value=history["date_added"].min().date()
)

end_date = st.sidebar.date_input(
    "End date",
    value=history["date_added"].max().date()
)

filtered = history[
    (history["date_added"].dt.date >= start_date) &
    (history["date_added"].dt.date <= end_date)
]

if start_date > end_date:
    st.error("Start date must be before end date.")
    st.stop()

# Key metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Titles", "8,790")

with col2:
    st.metric("Monthly Observations", len(history))

with col3:
    st.metric(
        "Best Model by MAE",
        evaluation.loc[evaluation["MAE"].idxmin(), "Model"]
    )

st.divider()

# Historical trend
st.subheader("Historical Monthly Content Additions")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    filtered["date_added"],
    filtered["content_added"],
    marker="o"
)

ax.set_xlabel("Date")
ax.set_ylabel("Content Additions")
ax.grid(True)

st.pyplot(fig)
plt.close(fig)

# Model evaluation
st.subheader("Forecasting Model Comparison")

st.dataframe(evaluation, use_container_width=True)

fig, ax = plt.subplots(figsize=(9, 4))

ax.bar(evaluation["Model"], evaluation["MAE"])
ax.set_ylabel("Mean Absolute Error")
ax.set_title("Model MAE Comparison")

st.pyplot(fig)
plt.close(fig)

# Forecast
st.subheader("Future 12-Month Baseline Forecast")

st.warning(
    "This is a simple naive baseline projection. "
    "It repeats the final observed monthly count and "
    "should not be interpreted as a reliable real-world forecast."
)

st.dataframe(future, use_container_width=True)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    history["date_added"],
    history["content_added"],
    label="Historical"
)

ax.plot(
    future["date"],
    future["predicted_content_additions"],
    linestyle="--",
    marker="o",
    label="Naive baseline forecast"
)

ax.set_xlabel("Date")
ax.set_ylabel("Content Additions")
ax.legend()
ax.grid(True)

st.pyplot(fig)
plt.close(fig)

# Download forecast
st.download_button(
    "Download Future Forecast CSV",
    data=future.to_csv(index=False),
    file_name="netflix_future_forecast.csv",
    mime="text/csv"
)

st.success("Dashboard loaded successfully!")
