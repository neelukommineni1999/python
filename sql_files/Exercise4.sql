SELECT *
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;


SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;