
import pandas as pd
import matplotlib.pyplot as plt

# Load monthly historical data
df = pd.read_csv("monthly_content_trends.csv")

df["date_added"] = pd.to_datetime(df["date_added"])

# Use the latest observed monthly value
last_value = df["content_added"].iloc[-1]

# Generate next 12 months
future_dates = pd.date_range(
    start=df["date_added"].max() + pd.offsets.MonthBegin(1),
    periods=12,
    freq="MS"
)

# Naive forecast
future_values = [last_value] * 12

forecast_df = pd.DataFrame({
    "date": future_dates,
    "predicted_content_additions": future_values
})

# Save predictions
forecast_df.to_csv(
    "models/future_forecast.csv",
    index=False
)

print("FUTURE 12-MONTH FORECAST")
print(forecast_df.to_string(index=False))

# Plot historical and future data
plt.figure(figsize=(12, 6))

plt.plot(
    df["date_added"],
    df["content_added"],
    label="Historical data"
)

plt.plot(
    future_dates,
    future_values,
    marker="o",
    linestyle="--",
    label="Naive forecast"
)

plt.title("Netflix Historical Trend and Future Forecast")
plt.xlabel("Date")
plt.ylabel("Monthly Content Additions")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("plots/future_forecast.png")
plt.show()

print("\nFuture forecast saved successfully!")
