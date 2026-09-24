import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Order Date": pd.date_range("2025-01-01", periods=24, freq="MS"),
    "Sales": [
        12000, 13500, 12800, 14200, 15000, 16200,
        15800, 17100, 16500, 18000, 19200, 20500,
        21000, 22500, 21800, 23500, 24200, 25000,
        26500, 27200, 28000, 29500, 31000, 32500
    ]
}

df = pd.DataFrame(data)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].dt.to_timestamp()

print(monthly_sales)

plt.figure(figsize=(7, 4))
plt.plot(monthly_sales["Order Date"], monthly_sales["Sales"], marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("monthly_sales_trend.png")
plt.show()

monthly_sales.to_csv("monthly_sales_table.csv", index=False)