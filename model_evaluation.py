
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load forecast results
df = pd.read_csv("models/forecast_results.csv")

actual = df["actual"]

predictions = {
    "Naive": df["naive"],
    "Seasonal Naive": df["seasonal_naive"],
    "ARIMA": df["arima"]
}

results = []

for model_name, forecast in predictions.items():

    mae = mean_absolute_error(actual, forecast)

    rmse = np.sqrt(
        mean_squared_error(actual, forecast)
    )

    # MAPE can be unstable when actual values are near zero
    mape = np.mean(
        np.abs((actual - forecast) / actual)
    ) * 100

    results.append({
        "Model": model_name,
        "MAE": round(mae, 2),
        "RMSE": round(rmse, 2),
        "MAPE (%)": round(mape, 2)
    })

evaluation = pd.DataFrame(results)

evaluation.to_csv(
    "models/model_evaluation.csv",
    index=False
)

print("\nMODEL PERFORMANCE COMPARISON")
print(evaluation.to_string(index=False))

best_model = evaluation.loc[
    evaluation["MAE"].idxmin()
]

print("\nBest model based on MAE:")
print(best_model)

print("\nEvaluation completed!")
