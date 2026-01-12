import pandas as pd

# File 1: Proper structure with headers
data1 = {
    "Email": ["alice@test.com", "bob@test.com", "alice@test.com"],
    "Name": ["Alice", "Bob", "Alice Duplicate"],
    "Age": [25, 30, 25]
}
df1 = pd.DataFrame(data1)
df1.to_excel("tests/test_data/file1.xlsx", index=False)
print(f"✓ Created file1.xlsx with columns: {list(df1.columns)}")

# File 2: Same structure
data2 = {
    "Email": ["charlie@test.com", "david@test.com"],
    "Name": ["Charlie", "David"],
    "Age": [35, 40]
}
df2 = pd.DataFrame(data2)
df2.to_excel("tests/test_data/file2.xlsx", index=False)
print(f"✓ Created file2.xlsx with columns: {list(df2.columns)}")