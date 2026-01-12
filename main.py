from cleaner import (
    clean_excel_pipeline, 
    standardize_dates, 
    clean_phone_numbers, 
    remove_blank_rows,
    format_excel_output
)

from config_loader import load_config
import sys

def run_pipeline():
    """Main pipeline with error handling."""
    
    print("=" * 60)
    print(" Excel Cleaner - FULL PIPELINE ")
    print("=" * 60)
    print()
    
    #Load configuration 
    print("Loading configuration from config.json...")
    config = load_config()
    print("✅ Configuration loaded")
    print()
    #Extract settings
    file_paths = config['files']['input_files']
    output_file = config['files']['output_file']
    duplicate_column = config['cleaning_options']['duplicate_column']
    keep_rule = config['cleaning_options'].get('keep_rule', 'first')
    date_columns = config['cleaning_options'].get('date_columns', [])
    phone_columns = config['cleaning_options'].get('phone_columns', [])
    remove_blanks = config['cleaning_options'].get('remove_blank_rows', True)
    do_formatting = config['cleaning_options'].get('format_excel', True)
    
    
    print(f"Settings:")
    print(f"    - Input files: {len(file_paths)} file(s)")
    print(f"    - Output file: {output_file}") 
    print(f"    - Duplicate check: {duplicate_column}")
    print(f"    - Date columns: {date_columns if date_columns else 'None'}")
    print(f"    - Phone columns: {phone_columns if phone_columns else 'None'}")
    print(f"    - Remove blank rows: {remove_blanks}")
    print(f"    - Format Excel output: {do_formatting}")
    
    
    try:
        #==== Step 1: Merge files ====#
        print(f"Step 1: Merging {len(file_paths)} files...")
        
        try:
            # First, just merge without deduplication
            merged_df, summary = clean_excel_pipeline(
                file_paths=file_paths,
                subset_columns=[duplicate_column],
                keep_rule="first"
            )
            print(f"✅ Merged {summary['files_merged']} files")
            print(f"✅ Total rows: {summary['rows_before']}")
            print()
        except FileNotFoundError as e:
            print(f"❌ ERROR: Could not find one or more files")
            print(f"   Missing file: {e}")
            print(f"   Check that these files exist:")
            for fp in file_paths:
                print(f"     - {fp}")
            sys.exit(1)
        except ValueError as e:
            print(f"❌ ERROR: Column mismatch between files")
            print(f"   {e}")
            print(f"   Make sure all files have the same column structure")
            sys.exit(1)
        
        #==== Step 2: Remove blank rows FIRST ====#
        print("Step 2: Removing blank rows...")
        merged_df, blanks_removed = remove_blank_rows(merged_df)
        print(f"✅ Removed {blanks_removed} blank row(s)")
        print()
        
        #==== Step 3: Remove duplicates ====#
        print("Step 3: Removing duplicates...")
        rows_before_dedup = len(merged_df)
        merged_df = merged_df.drop_duplicates(subset=[duplicate_column], keep="first")
        duplicates_removed = rows_before_dedup - len(merged_df)
        print(f"✅ Duplicates removed: {duplicates_removed}")
        print(f"✅ Final rows: {len(merged_df)}")
        print()
        
        #==== Step 4: Standardize dates ====#
        print("Step 4: Standardizing date columns...")
        try:
            merged_df, dates_fixed = standardize_dates(merged_df, date_columns=date_columns)
            print(f"✅ Standardized {dates_fixed} date(s) to YYYY-MM-DD")
        except ValueError as e:
            print(f"⚠️  Date standardization skipped: {e}")
            print(f"   Available columns: {list(merged_df.columns)}")
        print()
        
        #==== Step 5: Clean phone numbers ====#
        print("Step 5: Cleaning phone numbers...")
        try:
            merged_df, phone_fixed = clean_phone_numbers(merged_df, phone_columns=phone_columns)
            print(f"✅ Cleaned {phone_fixed} phone number(s)")
        except ValueError as e:
            print(f"⚠️  Phone cleaning skipped: {e}")
            print(f"   Available columns: {list(merged_df.columns)}")
        print()
        
        #==== Step 6: Save file ====#
        print(f"Step 6: Saving to {output_file}...")
        try:
            merged_df.to_excel(output_file, index=False)
            print("✅ File saved successfully")
        except PermissionError:
            print(f"❌ ERROR: Cannot write to {output_file}")
            print(f"   The file may be open in Excel - close it and try again")
            sys.exit(1)
        except Exception as e:
            print(f"❌ ERROR: Could not save file")
            print(f"   {e}")
            sys.exit(1)
        print()
        
        #==== Step 7: Format Excel ====#
        print("Step 7: Formatting Excel output...")
        try:
            format_excel_output(output_file)
            print("✅ Applied formatting (bold headers, auto-width)")
        except Exception as e:
            print(f"⚠️  Formatting failed (file still usable): {e}")
        print()
        
        #==== Success! ====#
        print("=" * 60)
        print("✅ PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print(f"📊 Final Statistics:")
        print(f"   Total rows processed: {summary['rows_before']}")
        print(f"   Blank rows removed: {blanks_removed}")
        print(f"   Duplicates removed: {duplicates_removed if 'duplicates_removed' in locals() else 0}")
        print(f"   Dates standardized: {dates_fixed if 'dates_fixed' in locals() else 0}")
        print(f"   Phones cleaned: {phone_fixed if 'phone_fixed' in locals() else 0}")
        print(f"   Final row count: {len(merged_df)}")
        print()
        print(f"📂 Output: {output_file}")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
        print("   No files were modified")
        sys.exit(0)
    except Exception as e:
        print("\n")
        print("=" * 60)
        print("❌ UNEXPECTED ERROR")
        print("=" * 60)
        print(f"An unexpected error occurred: {e}")
        print()
        print("Please report this error with:")
        print(f"  - Python version: {sys.version}")
        print(f"  - Error message: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()