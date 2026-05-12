CREATE TABLE customers (
    customer_id INT,
    name TEXT,
    city TEXT,
    age INT,
    updated_at DATE
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount INT,
    status TEXT
);