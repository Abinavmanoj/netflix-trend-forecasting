# Netflix Trend Forecasting

A time-series forecasting project that analyzes historical Netflix content additions and compares forecasting models to understand content release trends.

## Project Overview

This project uses the Netflix titles dataset to:
- Analyze historical Movies and TV Shows added to Netflix.
- Identify monthly and yearly content addition trends.
- Preprocess dates and aggregate content additions monthly.
- Build and compare time-series forecasting models.
- Evaluate forecasting performance using MAE, RMSE, and MAPE.
- Visualize historical trends and future baseline projections.
- Present results through an interactive Streamlit dashboard.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Statsmodels (ARIMA)
- Scikit-learn
- Streamlit
- Joblib

## Project Structure

```text
Netflix-Trend-Forecasting/
│
├── app.py
├── data_analysis.py
├── preprocessing.py
├── trend_analysis.py
├── forecasting.py
├── model_evaluation.py
├── visualization.py
├── future_forecast.py
├── requirements.txt
├── monthly_content_trends.csv
│
├── models/
│   ├── arima_model.pkl
│   ├── forecast_results.csv
│   ├── future_forecast.csv
│   └── model_evaluation.csv
│
└── plots/
    ├── monthly_trend.png
    ├── yearly_trend.png
    ├── forecast_comparison.png
    ├── model_comparison.png
    └── future_forecast.png
```

## Dataset

The project uses a Netflix titles dataset containing 8,790 records and 10 columns.

- Movies: 6,126
- TV Shows: 2,664
- Historical content addition dates: January 2008 – September 2021

**Note:** The original `Dataset.csv` is excluded from this repository. Obtain the dataset separately from a source that permits its use.

## Forecasting Models

Three forecasting approaches were evaluated:

1. **Naive Forecast:** Uses the last observed training value as the forecast.
2. **Seasonal Naive Forecast:** Uses values from the corresponding months in the previous year.
3. **ARIMA (1,1,1):** A statistical time-series forecasting model.

## Model Evaluation Results

| Model | MAE | RMSE | MAPE |
|---|---:|---:|---:|
| Naive | 31.33 | 40.39 | 20.57% |
| Seasonal Naive | 44.83 | 55.73 | 26.58% |
| ARIMA (1,1,1) | 33.03 | 41.46 | 20.10% |

The Naive model achieved the lowest MAE and RMSE, while ARIMA achieved the lowest MAPE.

The evaluation used a chronological split: 153 months for training and the final 12 months for testing.

## Dashboard

The Streamlit dashboard provides:
- Historical monthly content trends.
- Model performance comparison.
- Future baseline forecast visualization.
- Date filtering and CSV download options.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Abinavmanoj/netflix-trend-forecasting.git
cd netflix-trend-forecasting
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the dashboard

```bash
python -m streamlit run app.py
```

## Important Limitation

The dataset ends in September 2021. Therefore, the October 2021–September 2022 forecast is a simple historical baseline projection, not a prediction of Netflix's current content strategy or future releases.

## Author

**Abinav Manoj**

B.Tech Computer Science and Engineering

GitHub: [Abinavmanoj](https://github.com/Abinavmanoj)
