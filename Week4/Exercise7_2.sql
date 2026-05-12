CREATE VIEW customer_order_report AS
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.amount
FROM customers_ex7 c
JOIN orders_ex7 o
ON c.customer_id = o.customer_id;