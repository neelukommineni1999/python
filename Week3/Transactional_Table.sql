CREATE TABLE transactions (
    transaction_id INT,
    customer_id INT,
    status VARCHAR(20),
    amount NUMERIC,
    updated_at DATE,
    source_system VARCHAR(50)
);