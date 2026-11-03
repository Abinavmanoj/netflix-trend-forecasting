
import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

print("=" * 50)
print("NETFLIX DATASET ANALYSIS")
print("=" * 50)

# Dataset dimensions
print("\nDataset Shape:", df.shape)

# Column information
print("\nColumns:")
print(df.columns.tolist())

# First five records
print("\nFirst 5 Records:")
print(df.head())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Content type distribution
print("\nContent Type Distribution:")
print(df["type"].value_counts())

# Date added analysis
print("\nDate Added Information:")
print(df["date_added"].head(10))

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

print("\nDate Range:")
print("Earliest:", df["date_added"].min())
print("Latest:", df["date_added"].max())

# Year-wise additions
df["added_year"] = df["date_added"].dt.year

print("\nYear-wise Netflix Additions:")
print(df["added_year"].value_counts().sort_index())

print("\nAnalysis Completed Successfully!")
