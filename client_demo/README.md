# Try Data Cleaner - Free Demo

**See it work in 3 minutes with sample data!**

---

## 🎯 What You'll Learn

By trying this demo, you'll see how Data Cleaner:
- ✅ Merges multiple Excel files automatically
- ✅ Removes duplicate entries (based on email)
- ✅ Standardizes dates to YYYY-MM-DD format
- ✅ Formats phone numbers to (XXX) XXX-XXXX
- ✅ Removes blank rows
- ✅ Creates professional Excel formatting

**All in about 5 seconds of processing time!**

---

## 📋 What's Included

- `messy_sample.xlsx` - 100 rows of realistic messy business data
  * Contains duplicates (10%)
  * Mixed date formats (3 different styles)
  * Various phone number formats
  * Some blank rows (5%)

- `config_sample.json` - Pre-configured settings
  * Ready to use, no changes needed
  * Shows you how easy configuration is

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install pandas openpyxl --break-system-packages
```

### Step 2: Set Up Demo
```bash
# Copy sample file to input folder
cp client_demo/messy_sample.xlsx data/input/

# Use demo configuration (note single underscore)
cp client_demo/config_sample.json config.json
```

### Step 3: Run It!
```bash
python3 main.py
```

**Watch the magic happen!** ✨

---

## 📊 What You'll See

**Terminal Output:**
```
============================================================
 DATA CLEANER - FULL PIPELINE 
============================================================

Step 1: Merging files...
✅ Total rows: 100
✅ Duplicates removed: 10
✅ Final rows: 90

Step 2: Removing blank rows...
✅ Removed 5 blank row(s)

Step 3: Standardizing date columns...
✅ Standardized 85 date(s) to YYYY-MM-DD

Step 4: Cleaning phone numbers...
✅ Cleaned 85 phone number(s)

============================================================
✅ PIPELINE COMPLETED SUCCESSFULLY
============================================================
```

**Your cleaned file will be in:** `data/output/cleaned_sample.xlsx`

### Timestamped Output (Optional)
You can include a timestamp in the output filename via placeholders:

- `{date}` -> YYYYMMDD
- `{time}` -> HHMMSS
- `{datehour}` -> YYYYMMDD_HH
- `{datetime}` -> YYYYMMDD_HHMMSS

Example config snippet:

```json
{
  "files": {
    "input_files": ["data/input/messy_sample.xlsx"],
    "output_file": "data/output/cleaned_sample_{datehour}.xlsx"
  },
  "cleaning_options": { "duplicate_column": "Email" }
}
```

---

## 🔍 Compare Before & After

**Before (messy_sample.xlsx):**
```
Email               Phone           SignupDate
john@test.com      555-1234        01/15/2024
jane@test.com      (555) 234-5678  March 10, 2024
john@test.com      555.123.4567    2024-02-20
bob@test.com       5551234567      15-Jan-2024
                                                  ← Blank row!
```

**After (cleaned_sample.xlsx):**
```
Email               Phone           SignupDate
john@test.com      (555) 012-3400  2024-01-15
jane@test.com      (555) 234-5678  2024-03-10
bob@test.com       (555) 123-4567  2024-01-15
                                                  ← Blank removed
```

---

## 💡 Real-World Use Cases

**This tool is perfect for:**

- **HR Departments:** Merge employee records, remove duplicates
- **Sales Teams:** Combine monthly reports, clean contact lists
- **Data Analysts:** Prepare datasets, standardize formats
- **Finance Teams:** Merge transactions, clean vendor info

---

## 📈 Performance

**Tested and validated:**
- 100 rows: < 1 second
- 3,000 rows: 8 seconds
- 450,000 rows: 84 seconds ⚡

**Your data stays on YOUR computer** - nothing uploaded!

---

## 🎁 Portfolio Offer

I'm building my freelance portfolio and offering special rates for the first clients.

### Option 1: Done-For-You Service ⭐

**I'll clean your files so you don't have to do anything.**

- Up to 10,000 rows: **$25**
- Up to 100,000 rows: **$50**  
- 100,000+ rows: **$70**

**Delivery:** 24-48 hours, includes one revision

---

### Option 2: DIY With Setup Help

**I'll guide you to set it up on your computer and show you how to use it.**

**$50**

**Includes:** Installation, configuration, 30-minute training, and 3 days email support

---

### Option 3: Self-Service (Free)

**Download from GitHub and run it yourself anytime.** Perfect for tech-savvy users.

---

## 📞 Ready to Get Started?

**Contact me:**
- **Email:** adriana.gropan@gmail.com
- **Response time:** Usually within 2 hours
- **GitHub:** github.com/AdrianaGRO/data-cleaner

**Quick process:**
1. Email me your requirements
2. I confirm special pricing
3. You send files
4. I deliver clean data in 24-48 hours
5. You review and approve

---

## ⭐ After Your Project

If you're happy with the results:
- ✅ A brief testimonial (optional)
- ✅ Permission to mention your project type (anonymously)
- ✅ Referrals if you know others who need this

**Refer a friend = 50% off your next project!**

---

## 🚀 Try the Demo First!

Try the sample data included to see it in action, then decide if you want my help.

---

**Built by Adriana Gropan**  
*Freelance Python Developer | Data Automation*

*Last updated: January 12, 2026*
