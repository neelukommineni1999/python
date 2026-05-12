1.Identify entities and attributes for a banking app.

From a system like Bank Of America:
  Customer
  Account
  Transaction
  Loan
  Branch
  
Attributes for each entity
Customer---customer_id,name,email,phone,city
Account---account_id,customer_id,account_type,balance,created_date
Transaction--transaction_id,account_id,transaction_type (debit/credit),amount,transaction_date
Loan---loan_id,customer_id,loan_amount,interest_rate,status
Branch--branch_id,branch_name,city

2.Separate attributes that belong to Customer and Account.
Customer---customer_id,name,email,phone,city
Account (bank relationship)--account_id,customer_id,account_type,balance,created_date

3.Given a messy list of fields, group them under correct entities.
Messy field list (example)
Imagine your trainer gives you this--customer_id,customer_name,email,account_id,account_type,balance,transaction_id,transaction_date,amount,branch_name,city.

Step 1:Identify entities first
Customer
Account
Transaction
Branch

Step 2:Group fields correctly
Customer--customer_id,customer_name,email
Account--account_id,account_type,balance,customer_id (link to Customer)
Transaction--transaction_id,transaction_date,amount,account_id (link to Account)
Branch--branch_name,city

Fields were grouped into entities based on meaning. 
Customer contains identity data, Account contains financial data, Transaction contains activity data, and Branch contains location data.


4.Explain why order_amount belongs to Order and not Customer.
order_amount belongs to Order
because:
A customer has MANY orders
Each order has a different amount
