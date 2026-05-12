CREATE TABLE products (
    product_id INT PRIMARY KEY,        -- Surrogate Key
    product_name VARCHAR(100)
);

CREATE TABLE orders_ex5 (
    order_id INT PRIMARY KEY,          -- Surrogate Key
    customer_id INT,
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE payments_ex5 (
    payment_id INT PRIMARY KEY,        -- Surrogate Key
    order_id INT,
    FOREIGN KEY (order_id)
    REFERENCES orders_ex5(order_id)
);