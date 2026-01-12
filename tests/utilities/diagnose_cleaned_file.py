import pandas as pd

df = pd.read_excel("data/output/cleaned_loyalty_data.xlsx")

print("=" * 60)
print("DIAGNOSIS: Cleaned File Issues")
print("=" * 60)
print()

# Check 1: Date formats
print("1. Date Format Check:")
print(f"   Birthday sample: {df['Birthday'].iloc[0]}")
print(f"   JoinDate sample: {df['JoinDate'].iloc[0]}")
print(f"   Are dates standardized? {df['Birthday'].iloc[0] == '1992-03-10'}")
print()

# Check 2: Phone formats
print("2. Phone Format Check:")
print(f"   Phone samples:")
for i in range(5):
    print(f"      {df['Phone'].iloc[i]}")
print()

# Check 3: Blank rows
print("3. Blank Row Check:")
blank_rows = df[df['FirstName'].isna() & df['LastName'].isna() & df['Email'].isna()]
print(f"   Blank rows found: {len(blank_rows)}")
if len(blank_rows) > 0:
    print(f"   Row indexes: {blank_rows.index.tolist()}")
print()

# Check 4: Phone number issues
print("4. Phone Number Issues:")
has_extensions = df['Phone'].str.contains('x', case=False, na=False).sum()
has_plus = df['Phone'].str.contains(r'\+', na=False).sum()
has_dots = df['Phone'].str.contains(r'\.', na=False).sum()
print(f"   Phones with extensions (x): {has_extensions}")
print(f"   Phones with + prefix: {has_plus}")
print(f"   Phones with dots: {has_dots}")