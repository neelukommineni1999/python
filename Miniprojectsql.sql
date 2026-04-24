SELECT *
FROM customers_new;

SELECT *
FROM customers_new c
LEFT JOIN orders_new o
ON c.id = o.customer_id;

SELECT c.name, o.order_id, o.amount
FROM customers_new c
LEFT JOIN orders_new o
ON c.id = o.customer_id;


SELECT c.name,
       COUNT(o.order_id) AS total_orders,
       COALESCE(SUM(o.amount), 0) AS total_revenue
FROM customers_new c
LEFT JOIN orders_new o
ON c.id = o.customer_id
GROUP BY c.name;


SELECT c.name,
       COUNT(o.order_id) AS total_orders,
       SUM(o.amount) AS total_revenue
FROM customers_new c
LEFT JOIN orders_new o
ON c.id = o.customer_id
GROUP BY c.name;

SELECT c.name,
       COUNT(o.order_id) AS total_orders,
       COALESCE(SUM(o.amount), 0) AS total_revenue
FROM customers_new c
LEFT JOIN orders_new o
ON c.id = o.customer_id
GROUP BY c.name;
