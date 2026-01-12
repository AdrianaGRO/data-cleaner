import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from cleaner import standardize_dates, clean_phone_numbers, remove_blank_rows

#Messy test data

data = {
    "Name": ["Alice", "", "Bob", "Charlie"],
    "Phone": ["555-1234567", "", "(555) 987-6543", "5559876543"],
    "JoinDate": ["01/15/2024", "", "2024-02-20", "March 10, 2024"],
    "Sales": [1000, None, 2000, 3000]
}

df = pd.DataFrame(data)

print("=" * 50)
print("BEFORE CLEANING")
print("=" * 50)
print(df)
print("\n")


#Step 1: Remove blank rows
df_clean, blank_removed = remove_blank_rows(df)
print(f" ✓ Removed {blank_removed} blank row(s)")

#Step 2: Standardize dates
df_clean, dates_fixed = standardize_dates(df_clean, date_columns=["JoinDate"])
print(f" ✓ Standardized {dates_fixed} date(s)")

#Step 3: Clean phone numbers

df_clean, phone_fixed = clean_phone_numbers(df_clean, phone_columns=["Phone"])
print(f" ✓ Cleaned {phone_fixed} phone number(s)")

print()
print("=" * 50)
print("AFTER CLEANING")
print("=" * 50)
print(df_clean)
