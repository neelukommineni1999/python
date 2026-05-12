WITH ranked_orders AS (
    SELECT order_id, customer_id, order_date, amount,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY amount DESC
           ) AS rn
    FROM orders
)
SELECT order_id, customer_id, order_date, amount
FROM ranked_orders
WHERE rn = 1;