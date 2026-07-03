import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nTotal Revenue:", df["Total_Sales"].sum())

category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nCategory Wise Sales")
print(category_sales)

df.to_csv("analysis_results.csv", index=False)

category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
