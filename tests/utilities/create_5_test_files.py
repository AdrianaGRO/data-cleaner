import pandas as pd
import random
from datetime import datetime, timedelta

print("Creating 5 different test file types...\n")

#===========================================================
# TEST FILE 1: Small Sales Data (Basic Test)
#===========================================================
print("1. Creating small_sales_data.xlsx (10 rows, clean)")

data1 = {
    "OrderID": ["ORD001", "ORD002", "ORD003", "ORD004", "ORD005", 
                "ORD006", "ORD007", "ORD008", "ORD009", "ORD010"],
    "CustomerEmail": [
        "john@example.com", "mary@example.com", "john@example.com",
        "bob@example.com", "alice@example.com", "jane@example.com",
        "tom@example.com", "sarah@example.com", "mike@example.com", "lisa@example.com"
    ],
    "CustomerName": [
        "John Smith", "Mary Johnson", "John Smith", "Bob Wilson", "Alice Brown",
        "Jane Davis", "Tom Miller", "Sarah Garcia", "Mike Rodriguez", "Lisa Martinez"
    ],
    "Phone": [
        "555-1234", "(555) 234-5678", "555.123.4567", "5551234567", "+1-555-123-4567",
        "555 123 4567", "(555)123-4567", "555-123-4567x100", "555.234.5678", "5552345678"
    ],
    "OrderDate": [
        "01/15/2024", "2024-02-20", "March 10, 2024", "04/15/2024", "2024-05-20",
        "June 10, 2024", "07/15/2024", "2024-08-20", "September 10, 2024", "10/15/2024"
    ],
    "Amount": [100.50, 250.75, 150.00, 300.25, 175.50, 425.00, 200.00, 325.50, 275.25, 150.75]
}
df1 = pd.DataFrame(data1)
df1.to_excel("tests/test_data/test1_small_sales.xlsx", index=False)
print("   ✓ Created: 10 rows, 1 duplicate\n")

#===========================================================
# TEST FILE 2: HR Employee Data with Blank Rows
#===========================================================
print("2. Creating hr_employee_data.xlsx (with blank rows)")

data2 = {
    "EmployeeID": ["E001", "E002", "", "E003", "E004", None, "E005"],
    "Name": ["Alice Johnson", "Bob Smith", "", "Charlie Brown", "Diana Prince", None, "Eve Adams"],
    "Email": ["alice@company.com", "bob@company.com", "", "charlie@company.com", 
              "diana@company.com", None, "eve@company.com"],
    "Phone": ["555-0001", "555-0002", "", "(555) 000-0003", "555.000.0004", None, "5550005"],
    "HireDate": ["2020-01-15", "01/20/2020", "", "March 1, 2020", "2020-04-15", None, "05/01/2020"],
    "Department": ["Sales", "IT", "", "Marketing", "HR", None, "Finance"]
}
df2 = pd.DataFrame(data2)
df2.to_excel("tests/test_data/test2_hr_employees.xlsx", index=False)
print("   ✓ Created: 7 rows, 2 blank rows\n")

#===========================================================
# TEST FILE 3: Simplified Customer Data (50 rows)
#===========================================================
print("3. Creating medium_customers.xlsx (50 rows)")

emails = []
for i in range(50):
    emails.append(f"customer{i}@example.com")

# Add some duplicates
emails[5] = emails[0]
emails[15] = emails[0]
emails[25] = emails[10]

data3 = {
    "CustomerID": [f"CUST{i:03d}" for i in range(1, 51)],
    "Email": emails,
    "Phone": [f"555-{random.randint(1000,9999)}" for _ in range(50)],
    "SignupDate": [f"0{random.randint(1,9)}/15/2024" for _ in range(50)],
    "Amount": [round(random.uniform(10, 500), 2) for _ in range(50)]
}
df3 = pd.DataFrame(data3)
df3.to_excel("tests/test_data/test3_medium_customers.xlsx", index=False)
print("   ✓ Created: 50 rows, 3 duplicates\n")

#===========================================================
# TEST FILE 4: Inventory with Special Characters
#===========================================================
print("4. Creating inventory_special_chars.xlsx")

data4 = {
    "SKU": ["PROD-001", "PROD-002", "PROD-003", "PROD-004", "PROD-005"],
    "ProductName": [
        "Widget Pro", "Gadget Plus", "Tool Heavy Duty",
        "Device Premium", "Accessory More"
    ],
    "Supplier": ["Acme Corp", "TechCo Ltd", "BuildIt Inc", "MakersRUs", "Supply Co"],
    "Phone": ["+1-555-1000x500", "001-555-2000", "(555) 3000", "555.4000x999", "+1 (555) 5000"],
    "LastOrder": ["01/15/2024", "2024-02-20", "March 15, 2024", "04/10/2024", "2024-05-01"],
    "Price": [19.99, 29.50, 45.00, 12.75, 33.25]
}
df4 = pd.DataFrame(data4)
df4.to_excel("tests/test_data/test4_inventory.xlsx", index=False)
print("   ✓ Created: 5 rows, extensions in phones\n")

#===========================================================
# TEST FILE 5: Multi-File Merge Test
#===========================================================
print("5. Creating 3 monthly transaction files")

for i, month in enumerate(["january", "february", "march"], 1):
    data = {
        "TransactionID": [f"TXN{(i-1)*3+j:03d}" for j in range(1, 4)],
        "Email": [f"customer{j}@example.com" for j in range(1, 4)],
        "Amount": [round(random.uniform(10, 500), 2) for _ in range(3)],
        "Date": [f"{i:02d}/{j:02d}/2024" for j in range(10, 13)],
        "Phone": [f"555-{random.randint(1000,9999)}" for _ in range(3)]
    }
    df = pd.DataFrame(data)
    df.to_excel(f"tests/test_data/test5_transactions_{month}.xlsx", index=False)
    print(f"   ✓ Created: test5_transactions_{month}.xlsx")

print("\n" + "="*60)
print("✅ ALL TEST FILES CREATED")
print("="*60)
print("\nFiles in tests/test_data/:")
print("  1. test1_small_sales.xlsx")
print("  2. test2_hr_employees.xlsx")
print("  3. test3_medium_customers.xlsx")
print("  4. test4_inventory.xlsx")
print("  5. test5_transactions_*.xlsx (3 files)")