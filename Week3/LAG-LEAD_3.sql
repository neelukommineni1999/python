ORDER BY order_date is needed because LAG and LEAD work based on sequence, not actual time.

SQL tables don’t store data in a fixed order, so without ORDER BY, the database doesn’t know which row is before or after another.

By using ORDER BY order_date, I’m telling SQL to arrange the rows as a flow from earliest order to latest.