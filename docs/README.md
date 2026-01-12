# Data Cleaner - Automated Data Processing Tool

![Status](https://img.shields.io/badge/status-production%20ready-brightgreen)
![Tests](https://img.shields.io/badge/tests-5%2F5%20passing-success)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Performance](https://img.shields.io/badge/performance-5.3k%20rows%2Fs-brightgreen)

**Professional data cleaning tool for Excel and CSV files with automated testing and proven large-scale performance.**

Transform messy, duplicate-filled data files into clean, standardized datasets in seconds.

---

## 🎯 What It Does

Data Cleaner automates time-consuming data cleaning tasks for your spreadsheet files:

- **Merge Multiple Files** - Combine 2-100 Excel or CSV files into one dataset
- **Mix File Types** - Merge Excel and CSV files together in one operation
- **Remove Duplicates** - Eliminate duplicate rows based on any column (Email, ID, etc.)
- **Standardize Dates** - Convert 6+ date formats to consistent YYYY-MM-DD format
- **Clean Phone Numbers** - Format to (XXX) XXX-XXXX, remove extensions and country codes
- **Remove Blank Rows** - Automatically detect and eliminate empty rows
- **Professional Formatting** - Bold headers, auto-adjusted column widths

**Perfect for:** Data analysts, HR departments, sales teams, and anyone managing spreadsheet files.

---

## 📁 Supported File Formats

| Format | Extension | Support | Notes |
|--------|-----------|---------|-------|
| Excel 2007+ | `.xlsx` | ✅ Full support | Recommended format |
| Excel 97-2003 | `.xls` | ✅ Full support | Legacy format |
| CSV | `.csv` | ✅ Full support | Comma-separated values |
| **Mixed Operations** | Any combination | ✅ Full support | Merge different formats together! |

**Flexibility:** Process any combination of Excel and CSV files in a single operation.

**Example Use Case:**
```json
{
  "input_files": [
    "data/input/sales_2024.xlsx",
    "data/input/customers.csv",
    "data/input/orders_q1.xlsx",
    "data/input/orders_q2.csv"
  ]
}
```
All merged, cleaned, and deduplicated in one pass! ✨

---

## ⚡ Performance & Validation

**Tested at Scale:**

| Test Type | Dataset Size | Processing Time | Rate | Status |
|-----------|--------------|-----------------|------|--------|
| **Development** | 3,000 rows | 8 seconds | 375 rows/sec | ✅ Pass |
| **Large-Scale** | 450,000 rows | 84 seconds | 5,350 rows/sec | ✅ Pass |
| **Automated Suite** | 5 scenarios | < 1 minute | All passing | ✅ Pass |

**Large-Scale Test Details:**
```
Input:     3 files × 150,000 rows = 450,000 total rows
Process:   Merge + deduplicate + clean dates/phones + format
Output:    295,337 clean rows (154,663 duplicates removed)
Time:      84 seconds
Memory:    Efficient (tested on MacBook Air)
```

**Testing Note:** Validation performed with realistic generated data to simulate production scenarios. Always backup important files before processing.

---

## ✨ Key Features

### Data Cleaning
- ✅ **Duplicate Removal** - Based on any column (Email, CustomerID, OrderID, etc.)
- ✅ **Date Standardization** - Handles mixed formats: `01/15/2024`, `2024-02-20`, `March 10, 2024`
- ✅ **Phone Formatting** - Cleans `555-123-4567x100` → `(555) 123-4567`
- ✅ **Blank Detection** - Removes rows with all empty cells or null values

### File Processing
- ✅ **Multi-Format Support** - Excel (.xlsx, .xls) and CSV files
- ✅ **Mixed File Merging** - Combine Excel and CSV files in one operation
- ✅ **Column Validation** - Ensures consistent structure across all files
- ✅ **Large Dataset Support** - Tested up to 450,000 rows
- ✅ **Fast Processing** - 5,000+ rows per second

### Output Quality
- ✅ **Excel Formatting** - Bold headers, auto-width columns
- ✅ **Summary Statistics** - Detailed processing report
- ✅ **Error Handling** - Clear messages with recovery guidance
- ✅ **Timestamped Results** - Track multiple processing runs

---

## 🚀 Quick Start

### Prerequisites

**System Requirements:**
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended for large files)
- macOS, Linux, or Windows

**Install Dependencies:**
```bash
pip install pandas openpyxl --break-system-packages
```

---

### Installation
```bash
# Clone the repository
git clone https://github.com/AdrianaGRO/data-cleaner.git
cd data_cleaner

# Test the installation
python3 -c "import pandas; import openpyxl; print('✅ Dependencies installed!')"
```

---

### Basic Usage

**1. Place your files in `data/input/`**
```bash
# Copy your Excel/CSV files
cp ~/Downloads/*.xlsx data/input/
cp ~/Downloads/*.csv data/input/
```

**2. Configure `config.json`**
```json
{
  "files": {
    "input_files": [
      "data/input/sales_q1.xlsx",
      "data/input/sales_q2.csv",
      "data/input/sales_q3.xlsx"
    ],
    "output_file": "data/output/cleaned_sales_2024.xlsx"
  },
  "cleaning_options": {
    "duplicate_column": "Email",
    "keep_rule": "first",
    "date_columns": ["OrderDate", "ShipDate"],
    "phone_columns": ["CustomerPhone"],
    "remove_blank_rows": true,
    "format_excel": true
  }
}
```

**3. Run the cleaner**
```bash
python3 main.py
```

**4. Get your results**
```
============================================================
✅ PIPELINE COMPLETED SUCCESSFULLY
============================================================
📊 Final Statistics:
   Total rows processed: 15,000
   Duplicates removed: 234
   Blank rows removed: 12
   Dates standardized: 29,532
   Phones cleaned: 14,766
   Final row count: 14,754

📂 Output: data/output/cleaned_sales_2024.xlsx
```

---

## 📖 Configuration Guide

### Configuration Options

| Option | Type | Description | Example Values |
|--------|------|-------------|----------------|
| `input_files` | list | Files to process | `["file1.xlsx", "file2.csv"]` |
| `output_file` | string | Save location | `"output/cleaned.xlsx"` |
| `duplicate_column` | string | Column to check | `"Email"`, `"CustomerID"` |
| `keep_rule` | string | Which duplicate to keep | `"first"`, `"last"`, `false` |
| `date_columns` | list | Date columns | `["OrderDate", "BirthDate"]` |
| `phone_columns` | list | Phone columns | `["Phone", "Mobile"]` |
| `remove_blank_rows` | boolean | Remove empty rows | `true` / `false` |
| `format_excel` | boolean | Apply formatting | `true` / `false` |

---

### Date Format Support

Automatically handles these formats (and more):

| Input | Output |
|-------|--------|
| `01/15/2024` | `2024-01-15` |
| `2024-02-20` | `2024-02-20` |
| `March 10, 2024` | `2024-03-10` |
| `15-Jan-2024` | `2024-01-15` |
| `2024/03/25` | `2024-03-25` |

---

### Phone Number Cleaning

Handles various formats and removes extensions:

| Input | Output |
|-------|--------|
| `555-1234567` | `(555) 123-4567` |
| `(555) 123-4567` | `(555) 123-4567` |
| `555.123.4567` | `(555) 123-4567` |
| `5551234567` | `(555) 123-4567` |
| `+1-555-123-4567` | `(555) 123-4567` |
| `555-123-4567x100` | `(555) 123-4567` ← Extension removed |

---

## 🧪 Testing & Quality Assurance

### Automated Test Suite

Run comprehensive tests:
```bash
python3 tests/run_all_tests.py
```

**Test Coverage:**

| Test # | Description | Dataset | Status |
|--------|-------------|---------|--------|
| 1 | Basic functionality | 10 rows, 1 duplicate | ✅ Pass |
| 2 | Blank row handling | 7 rows, 2 blanks | ✅ Pass |
| 3 | Medium dataset | 50 rows, 3 duplicates | ✅ Pass |
| 4 | Phone extensions | 5 rows, extensions | ✅ Pass |
| 5 | Multi-file merge | 3 files, 9 rows | ✅ Pass |

**Latest Results:** 5/5 tests passing ✅

---

### Performance Testing

Successfully validated with large-scale tests:

**Test Methodology:**
- Generated realistic data (names, emails, dates, phones)
- Introduced duplicates (5-35% duplicate rate)
- Mixed date and phone formats
- Multiple file merging scenarios

**Results:**
- ✅ 450,000 rows processed without errors
- ✅ 34% duplicate rate handled (154,663 duplicates)
- ✅ 590,672 date standardizations
- ✅ 295,336 phone cleanings
- ✅ 84-second processing time
- ✅ No memory issues

---

## 📁 Project Structure
```
data_cleaner/
├── main.py                  # Main execution script
├── cleaner.py               # Core processing functions
├── config_loader.py         # Configuration management
├── config.json              # User settings
│
├── data/
│   ├── input/              # 📥 Place files here
│   └── output/             # 📤 Results appear here
│
├── tests/
│   ├── run_all_tests.py    # Automated test suite
│   ├── test_data/          # Test input files
│   ├── test_results/       # Test outputs (timestamped)
│   └── utilities/          # Test helper scripts
│
└── docs/
    ├── README.md           # This file
    └── scope.txt           # Project requirements
```

---

## 💡 Use Cases

### HR & Employee Management
- Merge employee records from multiple locations
- Deduplicate personnel databases
- Standardize hire dates and contact information
- Prepare data for payroll systems

### Sales & CRM
- Combine monthly sales reports
- Clean customer contact lists
- Remove duplicate leads
- Standardize transaction dates

### Data Analysis
- Prepare datasets for analysis
- Clean and merge data sources
- Standardize formats for consistency
- Remove data quality issues

### Finance & Accounting
- Merge transaction records
- Deduplicate payment entries
- Clean vendor information
- Standardize reporting dates

---

## 🛠️ Technical Details

**Built With:**
- Python 3.8+
- pandas (data processing)
- openpyxl (Excel formatting)

**Performance:**
- Processing rate: 5,000+ rows/second
- Tested capacity: 450,000 rows
- Memory: Efficient (standard laptop)
- Reliability: 100% test pass rate

**File Format Support:**
- `.xlsx` (Excel 2007+) ✅
- `.xls` (Excel 97-2003) ✅
- `.csv` (Comma-separated) ✅
- **Mixed format merging supported** ✅

---

## 📝 Dependencies
```
Python 3.8+
pandas >= 1.3.0
openpyxl >= 3.0.0
```

**Installation:**
```bash
pip install pandas openpyxl --break-system-packages
```

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Run tests before committing (`python3 tests/run_all_tests.py`)
4. Commit your changes (`git commit -m 'Add AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 🎯 Roadmap

**Planned Enhancements:**

- [ ] Column mapping (automatic schema alignment)
- [ ] Fuzzy duplicate matching (find similar entries)
- [ ] Additional data types (currency, percentages)
- [ ] GUI interface for non-technical users
- [ ] Batch processing (multiple projects)
- [ ] Custom validation rules
- [ ] Export to multiple formats (JSON, Parquet, SQL)

**Want a feature?** [Open an issue](https://github.com/AdrianaGRO/data-cleaner/issues)

---

## 📄 License

MIT License - Free for personal and commercial use.

See [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Adriana Gropan**

- GitHub: [@AdrianaGRO](https://github.com/AdrianaGRO)
- Email: adriana.gropan@gmail.com

*Built with focus on data quality and automation.*

---

## 🙏 Acknowledgments

Thanks to:
- pandas community for excellent data processing tools
- openpyxl for Excel manipulation capabilities
- The open-source community

---

## ❓ FAQ

**Q: Can I mix Excel and CSV files in one operation?**  
A: Yes! The tool automatically detects file types and processes them together.

**Q: What's the maximum file size?**  
A: Tested successfully with 450,000 rows. Limited by available RAM.

**Q: Does it modify my original files?**  
A: No. All original files remain unchanged. Output is saved to a new file.

**Q: Can I use it for production data?**  
A: Yes. The tool has been thoroughly tested and validated. Always backup important data before processing.

**Q: What if my files have different columns?**  
A: The tool will detect column mismatches and provide a clear error message.

---

**Built for data professionals who value clean, reliable data.** ✨

