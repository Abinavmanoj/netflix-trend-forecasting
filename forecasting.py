
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# Load monthly time-series data
df = pd.read_csv("monthly_content_trends.csv")

df["date_added"] = pd.to_datetime(df["date_added"])
series = df.set_index("date_added")["content_added"].asfreq("MS")

# Chronological train-test split
train = series.iloc[:-12]
test = series.iloc[-12:]

# Model 1: Naive baseline
naive_forecast = np.repeat(train.iloc[-1], len(test))

# Model 2: Seasonal naive baseline
seasonal_forecast = np.tile(train.iloc[-12:].values, 1)

# Model 3: ARIMA
model = ARIMA(train, order=(1, 1, 1))
fitted_model = model.fit()

arima_forecast = fitted_model.forecast(steps=len(test))

# Save predictions
results = pd.DataFrame({
    "date": test.index,
    "actual": test.values,
    "naive": naive_forecast,
    "seasonal_naive": seasonal_forecast,
    "arima": arima_forecast.values
})

results.to_csv("models/forecast_results.csv", index=False)

print("FORECASTING COMPLETED")
print("\nTraining observations:", len(train))
print("Testing observations:", len(test))

print("\nForecast comparison:")
print(results.to_string(index=False))

# Save trained ARIMA model
fitted_model.save("models/arima_model.pkl")

print("\nARIMA model saved successfully!")
