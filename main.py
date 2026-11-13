import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
customers=pd.read_csv("data\Customers.csv")
accounts=pd.read_csv("data\Accounts.csv")
transactions=pd.read_csv("data\Transactions.csv")
branches=pd.read_csv("data\Branches.csv")
loans=pd.read_csv("data\Loans.csv")
print(" BANKING DATA ANALYSIS PROJECT")
print("\nCustomers:")
print(customers.head())

print("\nAccounts:")
print(accounts.head())

print("\ntransactions:")
print(transactions.head())

print("\nBranches:")
print(branches.head())

print("\nLoans")
print(loans.head())

datasets={
    "Customers":customers,
    "Accounts":accounts,
    "Transactions":transactions,
    "Branches":branches,
    "Loans":loans,
}

print("\n======== DATA QUALITY REPORT========")
for name , df in datasets.items():
    print(f"\nDatasets:{name}")
    print("Shape:",df.shape)
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
    print("\nColumns Names:")
    print(df.columns.tolist())
    
print("\n=======REPORT COMPLETED========")

print("\n========== TRANSACTION ANALYSIS ==========")

transactions["Transaction_Date"] = pd.to_datetime(
    transactions["Transaction_Date"]
)

# Total transactions
print("\nTotal Transactions:")
print(len(transactions))

# Successful transactions
successful = transactions[
    transactions["Transaction_Status"] == "Successful"
]

print("\nSuccessful Transactions:")
print(len(successful))

# Total transaction amount
print("\nTotal Successful Amount:")
print(successful["Amount"].sum())

# Transaction type analysis
print("\nTransaction Type Analysis:")

print(
    successful.groupby("Transaction_Type")["Amount"]
    .agg(["count", "sum", "mean"])
)

# Channel analysis
print("\nTransaction Channel Analysis:")

print(
    successful.groupby("Channel")["Amount"].agg(["count", "sum"])
)
print("\n========== CUSTOMER ANALYSIS ==========")

# Total customers
print("Total Customers:", len(customers))

# Average age
print("Average Customer Age:", customers["Age"].mean())

# Customers by city
print("\nCustomers by City:")
print(customers["City"].value_counts())


print("\n========== ACCOUNT ANALYSIS ==========")

# Total accounts
print("Total Accounts:", len(accounts))

# Active accounts
active_accounts = accounts[
    accounts["Account_Status"] == "Active"
]

print("Active Accounts:", len(active_accounts))

# Total account balance
print("Total Account Balance:", accounts["Balance"].sum())

# Balance by account type
print("\nBalance by Account Type:")

print(
    accounts.groupby("Account_Type")["Balance"]
    .agg(["count", "sum", "mean"])
)

# Accounts per customer
customer_accounts = accounts.groupby("Customer_ID").size()

print("\nAccounts Per Customer:")
print(customer_accounts.head(10))

print("\n========== CUSTOMER ACCOUNT REPORT ==========")

customer_account_report = pd.merge(
    customers,
    accounts,
    on="Customer_ID",
    how="inner"
)

print(
    customer_account_report[
        [
            "Customer_ID",
            "Full_Name",
            "City",
            "Account_ID",
            "Account_Type",
            "Balance"
        ]
    ].head(10)
)

print("\nTotal Records:", len(customer_account_report))

# Save merged report
customer_account_report.to_csv(
    "Customer_Account_Report.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nReport Saved Successfully!")
print("\n========== LOAN DATA INSPECTION ==========")

print("\nLoan Table Columns:")
print(loans.columns.tolist())

print("\nFirst 10 Loan Records:")
print(loans.head(10))

print("\nLoan Table Information:")
loans.info()
print("\n========== LOAN ANALYSIS ==========")

# Total loans
print("Total Loans:", len(loans))

# Total loan amount
print("Total Loan Amount:", loans["Loan_Amount"].sum())

# Average loan amount
print("Average Loan Amount:", loans["Loan_Amount"].mean())

# Loan status distribution
print("\nLoan Status Distribution:")
print(loans["Loan_Status"].value_counts())

# Loan amount by status
print("\nLoan Amount by Status:")

print(
    loans.groupby("Loan_Status")["Loan_Amount"]
    .agg(["count", "sum", "mean"])
)

print("\nLOAN ANALYSIS COMPLETED")


# Calculate transaction amount by type
transaction_summary = successful.groupby(
    "Transaction_Type"
)["Amount"].sum()
# Anomaly Detection using Isolation Forest

X = transactions[["Amount"]]

model = IsolationForest(contamination=0.03, random_state=42)

transactions["Anomaly"] = model.fit_predict(X)

transactions["Anomaly"] = transactions["Anomaly"].map({
    1: "Normal",
    -1: "Unusual"
})

print(transactions["Anomaly"].value_counts())

unusual_transactions = transactions[
    transactions["Anomaly"] == "Unusual"
]

print(unusual_transactions.head(10))

transactions.to_csv(
    "Transaction_Anomaly_Report.csv",
    index=False,
    encoding="utf-8-sig"
)

# Create bar chart
plt.figure(figsize=(8, 5))

transaction_summary.plot(
    kind="bar",
    title="Total Transaction Amount by Type"
)

plt.xlabel("Transaction Type")
plt.ylabel("Total Amount")
plt.xticks(rotation=0)

plt.tight_layout()

# Save chart
plt.savefig("Transaction_Analysis.png")

plt.show()

print("Transaction chart saved successfully!")

# ==================================
# TRANSACTION STATUS VISUALIZATION
# ==================================

import matplotlib.pyplot as plt

# Count transactions by status
status_summary = transactions["Transaction_Status"].value_counts()

# Create pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    status_summary,
    labels=status_summary.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Transaction Status Distribution")

plt.tight_layout()

# Save chart
plt.savefig("Transaction_Status.png")

plt.show()

print("Transaction status chart saved successfully!")
