import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from cleaner import remove_duplicates, merge_excel_files, clean_excel_pipeline, standardize_dates, clean_phone_numbers, remove_blank_rows

# Sample DataFrame
data = {
    "Email": ["a@example.com", "b@example.com", "a@example.com", "c@example.com", "d@example.com", "g@example.com"],
    "Name": ["Alice", "Bob", "Alice", "Charlie", "David", "Grace"],
    "Age": [25, 30, 25, 35, 40, 28]
}
df = pd.DataFrame(data)

# TEST 1: Remove duplicates, keep first
cleaned_df, removed_count = remove_duplicates(df, subset_columns=["Email"], keep_rule="first")
assert len(cleaned_df) == 5
assert removed_count == 1

# TEST 2: Remove duplicates, keep last
cleaned_df, removed_count = remove_duplicates(df, subset_columns=["Email"], keep_rule="last")
assert len(cleaned_df) == 5
assert removed_count == 1

# TEST 3: Remove all duplicates
cleaned_df, removed_count = remove_duplicates(df, subset_columns=["Email"], keep_rule=False)
assert len(cleaned_df) == 4
assert removed_count == 2

# TEST 4: Remove duplicates using all columns
cleaned_df, removed_count = remove_duplicates(df, subset_columns=None, keep_rule="first")
assert len(cleaned_df) == 5
assert removed_count == 1

# TEST 5: Invalid keep_rule triggers error
try:
    remove_duplicates(df, subset_columns=["Email"], keep_rule="invalid")
    assert False
except ValueError:
    pass

# TEST 6: Merge files and pipeline
try:
    final_df, summary = clean_excel_pipeline(
        file_paths=["tests/test_data/file1.xlsx", "tests/test_data/file2.xlsx"],
        subset_columns=["Email"],
        keep_rule="first"
    )
    assert summary["files_merged"] == 2
    assert summary["rows_before"] == 5
    assert summary["rows_after"] == 4
    assert summary["duplicates_removed"] == 1
    assert len(final_df) == 4
except FileNotFoundError:
    pass  # Skip if files don't exist



#TEST 7: Standardize dates
data_dates = {
    "Name": ["Alice", "Bob", "Charlie"],
    "JoinDate": ["01/15/2024", "2024-02-20", "March 10, 2024"]
}

df_dates = pd.DataFrame(data_dates)

cleaned_dates, count = standardize_dates(df_dates, date_columns=["JoinDate"])


assert count == 3
assert cleaned_dates["JoinDate"].iloc[0] == "2024-01-15"
assert cleaned_dates["JoinDate"].iloc[1] == "2024-02-20"
assert cleaned_dates["JoinDate"].iloc[2] == "2024-03-10"

#TEST 8: Phone number cleaning
data_phones = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Phone": ["5551234567", "(555) 123-4567", "555.123.4567"]
}

df_phones = pd.DataFrame(data_phones)


cleaned_phones, count = clean_phone_numbers(df_phones, phone_columns=["Phone"])
assert count == 3
assert cleaned_phones["Phone"].iloc[0] == "(555) 123-4567"
assert cleaned_phones["Phone"].iloc[1] == "(555) 123-4567"
assert cleaned_phones["Phone"].iloc[2] == "(555) 123-4567"

#TEST 9: Remove blank rows

data_blanks = {
    "Name": ["Alice", "", "Bob"],
    "Email": ["alice@test.com", "", "bob@test.com"],
    "Age": [25, None, 30]
}

df_blanks = pd.DataFrame(data_blanks)

cleaned_blanks, removed = remove_blank_rows(df_blanks)
assert len(cleaned_blanks) == 2
assert removed == 1


print("✓ All tests passed")