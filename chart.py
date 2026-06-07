import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cleaned_customer_shopping_behavior.csv")

# KPIs
total_sales = df["Purchase Amount (USD)"].sum()
avg_purchase = df["Purchase Amount (USD)"].mean()
total_customers = len(df)

print("===== DASHBOARD KPIs =====")
print("Total Sales:", total_sales)
print("Average Purchase:", round(avg_purchase, 2))
print("Total Customers:", total_customers)

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1: Sales by Season
df.groupby("Season")["Purchase Amount (USD)"].sum().plot(
    kind="bar",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Sales by Season")
axes[0, 0].set_xlabel("Season")
axes[0, 0].set_ylabel("Sales (USD)")

# Chart 2: Gender Distribution
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Gender Distribution")
axes[0, 1].set_ylabel("")

# Chart 3: Payment Method Usage
df["Payment Method"].value_counts().plot(
    kind="bar",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Payment Method Usage")
axes[1, 0].set_xlabel("Payment Method")
axes[1, 0].set_ylabel("Customers")

# Chart 4: Average Purchase by Age Group
df["Age Group"] = pd.cut(
    df["Age"],
    bins=[18, 25, 35, 45, 55, 70],
    labels=["18-25", "26-35", "36-45", "46-55", "56-70"]
)

age_group_sales = df.groupby("Age Group")["Purchase Amount (USD)"].mean()

age_group_sales.plot(
    kind="bar",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Average Purchase by Age Group")
axes[1, 1].set_xlabel("Age Group")
axes[1, 1].set_ylabel("Average Purchase (USD)")
print("Opening dashboard...")

plt.tight_layout()
plt.show()

print("Dashboard closed")

plt.tight_layout()
plt.show()