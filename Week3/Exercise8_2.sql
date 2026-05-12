SELECT order_id, customer_id, amount
FROM orders
WHERE order_date >= DATE '2024-02-01';


In this query the best column for indexing is order_date
It is used in the WHERE clause for filtering
The database will search based on this column
Indexing it will make the query faster by avoiding full table scan