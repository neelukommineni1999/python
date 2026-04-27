SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
HAVING COUNT(*) > 1;