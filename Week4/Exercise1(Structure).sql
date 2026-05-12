1.Given a food delivery app, identify at least five entities.
Customer
Restaurant
Order
Driver
Payment

2.For each entity, write three possible attributes.
Customer
    customer_id
    name
    phone
Restaurant
    restaurant_id
    name
    location
Order
    order_id
    order_date
    total_amount
Driver
    driver_id
    name
    (delivery_time is tracked via orders)
Payment
    payment_id
    amount
    payment_status

3.Explain how Customer, Restaurant, Order, and Driver are related.
A Customer places Orders
A Restaurant receives Orders
A Driver delivers Orders
An Order has one Payment

4.Convert one business sentence into a rough table design.
Customer
   customer_id (Primary Key)
   name
   phone
Restaurant
   restaurant_id (Primary Key)
   name
   location
Driver
   driver_id (Primary Key)
   name
Order
   order_id (Primary Key)
   customer_id (Foreign Key → Customer)
   restaurant_id (Foreign Key → Restaurant)
   driver_id (Foreign Key → Driver)
   order_date
   total_amount
   delivery_time
Payment
   payment_id (Primary Key)
   order_id (Foreign Key → Order)
   amount
   payment_status
Relationship
   Customer → places Orders
   Restaurant → receives Orders
   Driver → delivers Orders
   Order → has Payment