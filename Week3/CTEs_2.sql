WITH recent_orders AS (
    SELECT order_id, customer_id, order_date, amount
    FROM orders
    WHERE order_date > '2024-02-01'
)
SELECT *
FROM recent_orders;