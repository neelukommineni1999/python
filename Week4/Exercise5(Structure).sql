1.Identify primary and foreign keys in customers and orders.
In the Customer table, customer_id is the primary key.
It is used to identify each customer.
In the Order table, order_id is the primary key.
The customer_id is a foreign key because it links each order to a customer.

2.List two natural keys and two surrogate keys.
Natural keys are values that come from real life, like email and phone number.
Surrogate keys are created by the system, like customer_id and order_id. These do not change.

3.Explain why email may not be a safe primary key.
Email is not a good primary key because it can change.
If it changes, it can break links in the database.
So we use a system ID like customer_id instead.

4.Design keys for Product, Order, and Payment tables.
In the Product table, product_id is the main ID for each product.
In the Order table, order_id is the main ID, and customer_id connects it to a customer.
In the Payment table, payment_id is the main ID, and order_id links it to an order.