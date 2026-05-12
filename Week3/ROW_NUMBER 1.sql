SELECT name, city, age,
       ROW_NUMBER() OVER (
           PARTITION BY city
           ORDER BY age DESC
       ) AS city_age_rank
FROM customers;