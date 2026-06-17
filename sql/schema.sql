CREATE DATABASE IF NOT EXISTS customer_churn_prediction;

USE customer_churn_prediction;

CREATE TABLE customer_churn (
    customer_id VARCHAR(10) PRIMARY KEY,
    gender VARCHAR(10),
    age INT,
    tenure INT,
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    contract_type VARCHAR(20),
    internet_service VARCHAR(20),
    payment_method VARCHAR(30),
    support_tickets INT,
    satisfaction_score INT,
    churn VARCHAR(5)
);