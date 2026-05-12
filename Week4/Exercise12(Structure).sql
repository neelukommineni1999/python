1.Classify example tables into raw, cleaned, or curated layer.
The table vendor_orders_csv belongs to the Raw/Bronze layer because it stores source data as received.
The table cleaned_orders belongs to the Cleaned/Silver layer because duplicates and missing values were handled.
The table fact_sales belongs to the Curated/Gold layer because it is designed for reporting and analytics.


3.Explain why analysts should usually use curated data instead of raw files.
Analysts should use curated data because it is already cleaned and ready to use.

Raw files can have mistakes, missing values, and messy formats, so they are harder to work with and can lead to wrong results.

Curated data is more reliable, easier to use, and ensures everyone gets the same correct numbers in reports.


4.Connect Week 1 CSV cleaning to raw-to-cleaned thinking.
In Week 1, when we clean CSV files, we are basically doing the same thing as moving data from raw to cleaned layer. 
The raw data is messy,it can have missing values, wrong formats, or duplicate rows. 
In Week 1, we use Python to fix these issues by cleaning the data, standardizing columns, and removing or handling bad values. 
So it becomes clean and ready to use. 
That is exactly what happens in the cleaned (silver) layer of a real data pipeline

