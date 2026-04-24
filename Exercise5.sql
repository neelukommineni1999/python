SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city;

SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;