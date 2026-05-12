-- Raw Layer
CREATE TABLE raw_orders (
    order_id INT,
    customer_name TEXT,
    amount NUMERIC
);

-- Cleaned Layer
CREATE TABLE silver_orders_cleaned AS
SELECT DISTINCT
    order_id,
    TRIM(customer_name) AS customer_name,
    amount
FROM raw_orders
WHERE order_id IS NOT NULL;

-- Curated Layer
CREATE TABLE fact_sales AS
SELECT
    customer_name,
    SUM(amount) AS total_sales
FROM silver_orders_cleaned
GROUP BY customer_name;