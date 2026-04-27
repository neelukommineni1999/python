SELECT name,
       CASE 
           WHEN age >= 60 THEN 'Senior'
           WHEN age >= 18 THEN 'Adult'
           ELSE 'Minor'
       END AS age_group
FROM customers;