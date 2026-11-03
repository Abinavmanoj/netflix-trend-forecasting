
import pandas as pd
import matplotlib.pyplot as plt

# Load historical data and forecast results
history = pd.read_csv("monthly_content_trends.csv")
results = pd.read_csv("models/forecast_results.csv")

history["date_added"] = pd.to_datetime(history["date_added"])
results["date"] = pd.to_datetime(results["date"])

# Plot historical trend
plt.figure(figsize=(13, 6))

plt.plot(
    history["date_added"],
    history["content_added"],
    label="Historical",
    linewidth=2
)

# Plot actual test values
plt.plot(
    results["date"],
    results["actual"],
    label="Actual Test Values",
    marker="o"
)

# Plot model predictions
plt.plot(
    results["date"],
    results["naive"],
    label="Naive Forecast",
    linestyle="--"
)

plt.plot(
    results["date"],
    results["arima"],
    label="ARIMA Forecast",
    linestyle="--"
)

plt.title("Netflix Content Trend Forecasting")
plt.xlabel("Date")
plt.ylabel("Monthly Content Additions")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("plots/forecast_comparison.png")
plt.show()

# Model performance chart
evaluation = pd.read_csv("models/model_evaluation.csv")

plt.figure(figsize=(9, 5))

plt.bar(
    evaluation["Model"],
    evaluation["MAE"]
)

plt.title("Forecasting Model MAE Comparison")
plt.ylabel("Mean Absolute Error")
plt.tight_layout()

plt.savefig("plots/model_comparison.png")
plt.show()

print("Forecast visualizations saved successfully!")
