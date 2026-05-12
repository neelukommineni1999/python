1.Design a bridge table for Employee and Project.
Relationship:
One employee can work on many projects
One project can have many employees
--This is many-to-many, so we need a bridge table.

Bridge table--employee_project,employee_id,project_id,assigned_date,role

2.Design an order_items table for Orders and Products.
Relationship:
One order can have many products
One product can be in many orders
---Many-to-many → bridge table

order_items table---order_items,order_id,product_id,quantity,price_at_time_of_purchase

3.Explain why storing product_ids as comma-separated values inside Orders is a bad idea.
Storing multiple product IDs in one column like “101,102,103” is not a good idea because it makes the data hard to work with.
It becomes difficult to find a specific product, and connecting the data with other tables is not easy. Over time, the data can become messy and harder to manage or update.
Instead, it is better to use a separate table (like order_items) to store this information in a clean and organized way.

4.Identify the bridge table in a learning management system.
In a learning management system, students and courses are connected in a many-to-many way.
A student can take multiple courses, and each course can have many students enrolled in it.
To manage this relationship, we use a bridge table called student_course.
This table stores the connection between students and courses using fields like student_id and course_id.
It helps keep track of which student is enrolled in which course and makes the data easy to manage and organize.

