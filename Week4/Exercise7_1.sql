CREATE TABLE customers_ex7 (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE orders_ex7 (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id)
    REFERENCES customers_ex7(customer_id)
);


I created separate tables for exercise 7 (customers_ex7 and orders_ex7) 
and linked them using a foreign key from orders_ex7.customer_id 
to customers_ex7.customer_id.
