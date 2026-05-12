1.Design a star schema for sales reporting.
In a star schema, we keep one main table for sales (fact table)
and connect it to other tables like customer, product, date, and store. 
All these tables are directly connected to the sales table.


2.Convert a product dimension into a snowflake design with category table.
In a snowflake design, we split the product information into two tables. 
One table stores product details, and another table stores category details. 
The product table is linked to the category table.


3.Explain which design is easier for dashboards.
Star schema is easier for dashboards because it is simple, has fewer joins, and is easy to understand. 
Reports can be created faster.


4.Compare star and snowflake trade-offs.
Star schema is simple and easy to use, but may have some repeated data. 
Snowflake schema is more organized and reduces duplication, 
but it is more complex and slower because it needs more joins.

