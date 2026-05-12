SELECT *
FROM customers;

SELECT *
FROM customers
WHERE city = 'Hyderabad';

SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;


SELECT c.name, SUM(o.amount) AS total_amount
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id
GROUP BY c.name;


SELECT *
FROM customers
WHERE age IS NULL
   OR city IS NULL
   OR name IS NULL;