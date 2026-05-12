1.Classify examples as OLTP or OLAP.
Order placing system → OLTP (used for doing transactions like placing orders)
Sales dashboard → OLAP (used for analyzing sales data)
Bank money transfer → OLTP (used for real-time transactions)
Business reporting system → OLAP (used for reports and analysis)


2.Explain why a dashboard should not directly query highly normalized operational tables in many cases.
Dashboards should not directly use OLTP tables because they are designed for daily transactions,not for heavy analysis. 
Running reports on them can be slow and complicated.


3.Compare order entry system and sales dashboard.
Order system (OLTP): used to place and update orders in real time.
Sales dashboard (OLAP): used to understand trends and analyze business performance.


4.Describe how source tables become warehouse tables.
Data from operational systems is first cleaned and organized. 
Then it is transformed into a simpler structure for reporting, like combining related data into fact and dimension tables. 
This makes it easier to analyze in dashboards.
