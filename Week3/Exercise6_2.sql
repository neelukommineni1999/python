SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC) AS rn
    FROM customers
) t
WHERE rn = 1;


First,I would find what makes a record duplicate. Here, it is the customer_id, meaning the same customer appears more than once.

Next,I would decide which record to keep. The rule is to keep the most recent one, so I will use the updated_at column.