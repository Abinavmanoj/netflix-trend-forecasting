
import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

# Remove records with invalid dates
df = df.dropna(subset=["date_added"])

# Extract year and month
df["year"] = df["date_added"].dt.year
df["month"] = df["date_added"].dt.month

# Create monthly content addition counts
monthly_data = (
    df.set_index("date_added")
      .resample("MS")
      .size()
      .rename("content_added")
      .reset_index()
)

# Save processed data
monthly_data.to_csv("monthly_content_trends.csv", index=False)

print("Monthly preprocessing completed!")
print("\nMonthly dataset shape:", monthly_data.shape)
print("\nFirst 10 months:")
print(monthly_data.head(10))

print("\nLast 10 months:")
print(monthly_data.tail(10))

print("\nTotal content additions:", monthly_data["content_added"].sum())
