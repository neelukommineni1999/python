1.Given customer city changes, decide Type 1 or Type 2.
Use Type 1 if we only need the latest city
Use Type 2 if we need to keep old and new cities (history)


2.Design columns needed for a Type 2 dimension.
In Type 2, we store extra details to track changes:
   customer_id
   customer_name
   city
   start date (when the record became valid)
   end date (when it stopped being valid)
   is_current (shows the latest record)


3.Explain what is_current means.
Old record → not current
New record → current


4.Explain one situation where Type 1 is enough.
Type 1 is used when old data is not important at all, 
only the latest correct value matters.

