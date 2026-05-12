3.Explain why an index may not help if the query returns most of the table.

An index is not always useful.
If a query returns most of the table data, the database still has to read almost everything.
In that case, scanning the whole table can be faster than using an index.
So indexes help more when we are fetching only a small part of the data.