
import pandas as pd
import matplotlib.pyplot as plt

# Load monthly data
df = pd.read_csv("monthly_content_trends.csv")

df["date_added"] = pd.to_datetime(df["date_added"])

# Extract time features
df["year"] = df["date_added"].dt.year
df["month"] = df["date_added"].dt.month

# Yearly trend
yearly_trend = (
    df.groupby("year")["content_added"]
    .sum()
)

print("YEARLY CONTENT ADDITIONS")
print(yearly_trend)

# Monthly average trend
monthly_average = (
    df.groupby("month")["content_added"]
    .mean()
)

print("\nAVERAGE ADDITIONS BY MONTH")
print(monthly_average)

# Highest and lowest months
print("\nHighest monthly addition:")
print(df.loc[df["content_added"].idxmax()])

print("\nLowest monthly addition:")
print(df.loc[df["content_added"].idxmin()])

# Plot monthly trend
plt.figure(figsize=(12, 5))
plt.plot(
    df["date_added"],
    df["content_added"],
    label="Monthly additions"
)

plt.title("Netflix Monthly Content Addition Trend")
plt.xlabel("Date")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("plots/monthly_trend.png")
plt.show()

# Plot yearly trend
plt.figure(figsize=(10, 5))
yearly_trend.plot(kind="bar")

plt.title("Netflix Yearly Content Additions")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig("plots/yearly_trend.png")
plt.show()

print("\nTrend analysis completed!")
