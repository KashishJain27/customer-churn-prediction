from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

os.makedirs("data/raw", exist_ok=True)

customers = []

for i in range(1, 10001):
    tenure = random.randint(1, 72)
    monthly_charges = round(random.uniform(300, 3000), 2)
    total_charges = round(tenure * monthly_charges, 2)
    support_tickets = random.randint(0, 10)
    satisfaction_score = random.randint(1, 10)

    churn_score = 0

    if tenure < 12:
        churn_score += 1

    if monthly_charges > 2000:
        churn_score += 1

    if support_tickets > 5:
        churn_score += 1

    if satisfaction_score < 5:
        churn_score += 1

    if churn_score >= 2:
        churn = "Yes"
    else:
        churn = "No"

    customers.append([
        f"CUST{i:05d}",
        random.choice(["Male", "Female"]),
        random.randint(18, 70),
        tenure,
        monthly_charges,
        total_charges,
        random.choice(["Monthly", "Yearly", "Two Year"]),
        random.choice(["Fiber", "DSL", "None"]),
        random.choice(["UPI", "Credit Card", "Debit Card", "Net Banking"]),
        support_tickets,
        satisfaction_score,
        churn
    ])

df = pd.DataFrame(
    customers,
    columns=[
        "customer_id",
        "gender",
        "age",
        "tenure",
        "monthly_charges",
        "total_charges",
        "contract_type",
        "internet_service",
        "payment_method",
        "support_tickets",
        "satisfaction_score",
        "churn"
    ]
)

df.to_csv("data/raw/customer_churn.csv", index=False)

print("customer_churn.csv created successfully!")
print(df["churn"].value_counts())