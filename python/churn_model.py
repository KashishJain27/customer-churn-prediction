import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/customer_churn.csv")

le = LabelEncoder()

categorical_columns = [
    "gender",
    "contract_type",
    "internet_service",
    "payment_method",
    "churn"
]

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

X = df.drop(
    ["customer_id", "churn"],
    axis=1
)

y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:")
print(accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

results = X_test.copy()
results["actual_churn"] = y_test
results["predicted_churn"] = y_pred

results.to_csv(
    "data/processed/churn_predictions.csv",
    index=False
)

print("Predictions saved successfully!")