WITH ranked_customers AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY updated_at DESC
           ) AS rn
    FROM customers
)
SELECT customer_id, name, city, age, updated_at
FROM ranked_customers
WHERE rn = 1;



When the same customer_id appears multiple times, it means we have duplicate records for that customer.

To fix this, we decide a rule to choose the correct one. Usually, we keep the record with the latest updated date because it has the most recent and accurate information.