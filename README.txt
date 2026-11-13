BANKING PROJECT - SMALL PRACTICE DATASET

All records are fictional and created for practice. No real banking/customer data is included.

Row counts:
- Customers.csv: 20
- Accounts.csv: 30
- Transactions.csv: 100
- Branches.csv: 5
- Loans.csv: 10
Total: 165 data rows.

Relationships:
- Accounts.Customer_ID -> Customers.Customer_ID
- Accounts.Branch_ID -> Branches.Branch_ID
- Transactions.Account_ID -> Accounts.Account_ID
- Loans.Customer_ID -> Customers.Customer_ID

Amounts are fictional practice values in IRR.
Practice_Flag marks only the three largest transactions as examples for learning filters.
It is not a fraud label or a real risk assessment.
This is not a reconciled banking ledger.
