SELECT order_id, customer_id, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_number,
       RANK() OVER (ORDER BY amount DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank
FROM orders;



When two orders have the same amount:

ROW_NUMBER - It ignores the tie and still gives each row a different number
RANK - It gives them the same rank, but skips the next number
DENSE_RANK - It gives them the same rank and keeps the sequence continuous