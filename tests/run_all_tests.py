import subprocess
import json
import os

from datetime import datetime

# Change to parent directory to run main.py
original_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(parent_dir)
os.chdir(project_root)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print("="*70)
print("DATA CLEANER - AUTOMATED TEST SUITE")
print("="*70)
print()

# Define 5 test scenarios
tests = [
    {
        "name": "Test 1: Small Sales File",
        "description": "10 rows with 1 duplicate, mixed phone/date formats",
        "config": {
            "files": {
                "input_files": ["tests/test_data/test1_small_sales.xlsx"],
                "output_file": f"tests/test_results/test1_output_{timestamp}.xlsx"
            },
            "cleaning_options": {
                "duplicate_column": "CustomerEmail",
                "keep_rule": "first",
                "date_columns": ["OrderDate"],
                "phone_columns": ["Phone"],
                "remove_blank_rows": True,
                "format_excel": True
            }
        }
    },
    {
        "name": "Test 2: HR with Blank Rows",
        "description": "7 rows with 2 blank rows to remove",
        "config": {
            "files": {
                "input_files": ["tests/test_data/test2_hr_employees.xlsx"],
                "output_file": f"tests/test_results/test2_output_{timestamp}.xlsx"
            },
            "cleaning_options": {
                "duplicate_column": "Email",
                "keep_rule": "first",
                "date_columns": ["HireDate"],
                "phone_columns": ["Phone"],
                "remove_blank_rows": True,
                "format_excel": True
            }
        }
    },
    {
        "name": "Test 3: Medium Customer Database",
        "description": "50 rows with 3 duplicates",
        "config": {
            "files": {
                "input_files": ["tests/test_data/test3_medium_customers.xlsx"],
                "output_file": f"tests/test_results/test3_output_{timestamp}.xlsx"
            },
            "cleaning_options": {
                "duplicate_column": "Email",
                "keep_rule": "first",
                "date_columns": ["SignupDate"],
                "phone_columns": ["Phone"],
                "remove_blank_rows": True,
                "format_excel": True
            }
        }
    },
    {
        "name": "Test 4: Inventory with Phone Extensions",
        "description": "5 rows with phone extensions and special formats",
        "config": {
            "files": {
                "input_files": ["tests/test_data/test4_inventory.xlsx"],
                "output_file": f"tests/test_results/test4_output_{timestamp}.xlsx"
            },
            "cleaning_options": {
                "duplicate_column": "SKU",
                "keep_rule": "first",
                "date_columns": ["LastOrder"],
                "phone_columns": ["Phone"],
                "remove_blank_rows": True,
                "format_excel": True
            }
        }
    },
    {
        "name": "Test 5: Multi-File Merge",
        "description": "Merge 3 monthly transaction files",
        "config": {
            "files": {
                "input_files": [
                    "tests/test_data/test5_transactions_january.xlsx",
                    "tests/test_data/test5_transactions_february.xlsx",
                    "tests/test_data/test5_transactions_march.xlsx"
                ],
                "output_file": f"tests/test_results/test5_output_{timestamp}.xlsx"
            },
            "cleaning_options": {
                "duplicate_column": "Email",
                "keep_rule": "first",
                "date_columns": ["Date"],
                "phone_columns": ["Phone"],
                "remove_blank_rows": True,
                "format_excel": True
            }
        }
    }
]

# Store results
results = []

# Run each test
for i, test in enumerate(tests, 1):
    print(f"\n{'='*70}")
    print(f"[{i}/5] {test['name']}")
    print(f"Description: {test['description']}")
    print(f"{'='*70}")
    
    # Write test config temporarily
    with open("config.json", "w") as f:
        json.dump(test['config'], f, indent=2)
        
    print("⏳ Running test...")
    
    # Run main.py
    try:
        proc_result = subprocess.run(
            ['python3', 'main.py'],
            capture_output=True,
            text=True,
            timeout=30
        ) 
        
        # Check if successful
        if proc_result.returncode == 0:
            print("✅ TEST PASSED")
            
            # Extract key stats from output
            output_lines = proc_result.stdout.split('\n')
            stats = {}
            for line in output_lines:
                if "Total rows:" in line or "Total rows processed:" in line:
                    stats['total_rows'] = line.split(":")[-1].strip()
                if "Duplicates removed:" in line:
                    stats['duplicates_removed'] = line.split(":")[-1].strip()
                if "Final row count:" in line:
                    stats['final_rows'] = line.split(":")[-1].strip()
                    
            print(f"   📊 Stats: {stats}")    
            
            results.append({
                "test_number": i,
                "test_name": test['name'],
                "status": "PASSED",
                "stats": stats
            })
            
        else:
            print("❌ TEST FAILED")
            print("   Error Output:")
            print(f"   {proc_result.stderr[:200]}")
            
            results.append({
                "test_number": i,
                "test_name": test['name'],
                "status": "FAILED",
                "error": proc_result.stderr[:200]
            })
             
    except subprocess.TimeoutExpired:
        print("❌ TEST TIMEOUT (>30 seconds)")
        results.append({
            "test_number": i,
            "test_name": test['name'],
            "status": "TIMEOUT"
        })
        
    except Exception as e:
        print(f"❌ TEST ERROR: {e}")
        results.append({
            "test_number": i,
            "test_name": test['name'],
            "status": "ERROR",
            "error": str(e)
        })
        
        
#Final Summary
print(f"\n{'='*70}")
print("TEST SUITE COMPLETED - SUMMARY")
print(f"{'='*70}")

passed = sum(1 for r in results if r['status'] == "PASSED")
failed = len(results) - passed

print(f"\n📊 Results:")
print(f"   Total Tests: {len(results)}")
print(f"   ✅ Passed: {passed}")
print(f"   ❌ Failed: {failed}")
print()


print("📋 Detailed Results:")
for r in results:
    status_icon = "✅" if r['status'] == "PASSED" else "❌"
    print(f"   {status_icon} Test {r['test_number']}: {r['test_name']} - {r['status']}")
    
# Save the results to JSON
results_filename = f'tests/test_results/test_results_{timestamp}.json'
with open(results_filename, 'w') as f:
    json.dump(results, f, indent=2)
    
print(f"\n💾 Detailed results saved to {results_filename}")

# Restore original config 
print("\n🔄 Restoring original config.json...")
original_config = {
     "files": {
        "input_files": [
            "data/input/loyalty_file_1.xlsx",
            "data/input/loyalty_file_2.xlsx",
            "data/input/loyalty_file_3.xlsx"
        ],
        "output_file": "data/output/cleaned_loyalty_data.xlsx"
    },
    "cleaning_options": {
        "duplicate_column": "Email",
        "keep_rule": "first",
        "date_columns": ["Birthday", "JoinDate"],
        "phone_columns": ["Phone"],
        "remove_blank_rows": True,
        "format_excel": True
    }
}

with open('config.json', 'w') as f:
    json.dump(original_config, f, indent=2)
    
print("✅ Original config.json restored")

# List all created files
print(f"\n📂 Output files created:")
for r in results:
    if r['status'] == 'PASSED':
        # Extract output file from config
        test_config = tests[r['test_number']-1]['config']
        output_file = test_config['files']['output_file']
        print(f"   ✅ {output_file}")
print(f"   📊 {results_filename}")

print("\n" + "="*70)
print("TESTING COMPLETE")
print("="*70)

if passed == len(results):
    print("🎉 All tests passed! Your Data Cleaner is production-ready!")
else:
    print(f"⚠️  {failed} test(s) failed. Review errors above.")



print(f"Test Run Timestamp: {timestamp}\n")
print("="*70)