WITH completed_orders AS (
    SELECT order_id, customer_id, order_date, amount
    FROM orders
    WHERE status = 'completed'
)
SELECT *
FROM completed_orders;