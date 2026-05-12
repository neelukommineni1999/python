SELECT order_id, customer_id, order_date, amount,
       ROW_NUMBER() OVER (
           PARTITION BY customer_id
           ORDER BY amount DESC
       ) AS order_rank
FROM orders;