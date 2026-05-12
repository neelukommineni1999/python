SELECT customer_id, order_date, amount, status
FROM orders
WHERE order_date >= DATE '2024-02-01';


I use a date filter in the WHERE clause to limit the data.
This helps the query read only needed records instead of the whole table.
For example, it only processes data from 2024-02-01 onwards.
This makes the query faster and reduces unnecessary processing.