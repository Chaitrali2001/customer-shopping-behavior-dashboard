import pandas as pd

# Load dataset
df = pd.read_csv("customer_shopping_behavior.csv")

# Fill missing Review Rating values with average rating
df["Review Rating"] = df["Review Rating"].fillna(
    df["Review Rating"].mean()
)

# Verify
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_customer_shopping_behavior.csv", index=False)

print("Dataset cleaned successfully!")