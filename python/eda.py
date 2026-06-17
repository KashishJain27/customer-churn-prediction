import pandas as pd

df = pd.read_csv("data/raw/customer_churn.csv")

print("Dataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nChurn Distribution:")
print(df["churn"].value_counts())

print("\nStatistical Summary:")
print(df.describe())