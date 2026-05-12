SELECT DISTINCT c.customer_id, c.name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;


Explanation: Both queries give the same result, they show customers who have placed at least one order.

In the subquery method, we first find all customer IDs from the orders table and then use that list to filter the customers table.

In the JOIN method, we directly connect the customers and orders tables using customer_id to get matching records.