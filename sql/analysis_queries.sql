USE customer_churn_prediction;

-- Total Customers
SELECT
    COUNT(*) AS total_customers
FROM customer_churn;

-- Churn Distribution
SELECT
    churn,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY churn;

-- Churn Rate
SELECT
    ROUND(
        SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM customer_churn;

-- Average Monthly Charges by Churn
SELECT
    churn,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges
FROM customer_churn
GROUP BY churn;

-- Average Satisfaction Score by Churn
SELECT
    churn,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction_score
FROM customer_churn
GROUP BY churn;

-- Churn by Contract Type
SELECT
    contract_type,
    churn,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY contract_type, churn
ORDER BY contract_type, churn;

-- Churn by Internet Service
SELECT
    internet_service,
    churn,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY internet_service, churn
ORDER BY internet_service, churn;

-- Churn by Support Tickets
SELECT
    support_tickets,
    churn,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY support_tickets, churn
ORDER BY support_tickets, churn;