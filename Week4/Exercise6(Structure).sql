1.Define grain for an orders table.
One row represents one order.

2.Define grain for order_items table.
One row represents one product within an order.

3.Explain why order-level and product-line-level data should not be mixed blindly.
Order-level data and product-level data are different. 
If we mix them, the same data can repeat multiple times. 
This can lead to wrong results, like counting revenue more than once.

4.Given a sample dataset, write the grain in one sentence.
One row represents one record at the lowest level of detail in the dataset.
