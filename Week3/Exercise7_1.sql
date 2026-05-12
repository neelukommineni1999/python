SELECT customer_id, order_date, amount, status
FROM orders;


We should avoid using SELECT * in real projects.
It pulls all columns from a table, even unnecessary ones.
This can make the query slower.
It also uses more memory and increases data load.
So, we should select only the columns we need.