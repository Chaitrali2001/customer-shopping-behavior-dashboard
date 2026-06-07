import pandas as pd

df = pd.read_csv("cleaned_customer_shopping_behavior.csv")

print("Average Purchase Amount:")
print(df["Purchase Amount (USD)"].mean())

print("\nSales by Category:")
print(
    df.groupby("Category")["Purchase Amount (USD)"]
      .sum()
      .sort_values(ascending=False)
)

print("\nMost Used Payment Methods:")
print(df["Payment Method"].value_counts())