INSERT INTO customers (name, phone)
VALUES ('Alice', '1234567890'), ('Bob', '9876543210');

INSERT INTO restaurants (name, location)
VALUES ('Pizza Place', 'NY'), ('Burger House', 'LA');

INSERT INTO drivers (name)
VALUES ('John'), ('Mike');

INSERT INTO orders (customer_id, restaurant_id, driver_id, order_date, total_amount, delivery_time)
VALUES 
(1, 1, 1, NOW(), 25.50, 30),
(2, 2, 2, NOW(), 15.00, 20);

INSERT INTO payments (order_id, amount, payment_status)
VALUES 
(1, 25.50, 'Completed'),
(2, 15.00, 'Completed');