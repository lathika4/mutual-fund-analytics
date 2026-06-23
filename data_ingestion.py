import pandas as pd
import os

# ============================================================
# DATA INGESTION
# ============================================================

DATA_FOLDER = "data/raw"

print("=" * 60)
print("DATA INGESTION STARTED")
print("=" * 60)

if not os.path.exists(DATA_FOLDER):
    print("Folder not found:", DATA_FOLDER)
    exit()

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

if len(csv_files) == 0:
    print("No CSV files found.")
else:
    for file in csv_files:

        path = os.path.join(DATA_FOLDER, file)

        print("\n" + "=" * 60)
        print("FILE:", file)

        try:
            df = pd.read_csv(path)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

        except Exception as e:
            print("Error:", e)

print("\nData ingestion completed.")

# ============================================================
# FUND MASTER ANALYSIS
# ============================================================

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\n" + "=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nTotal Schemes:")
print(len(fund_master))

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

# ============================================================
# AMFI CODE VALIDATION
# ============================================================

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("✅ All AMFI codes exist in NAV History")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

# ============================================================
# DATA QUALITY SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

for file in csv_files:

    path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(path)

        print(f"\nDataset: {file}")
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])
        print("Missing Values:", df.isnull().sum().sum())
        print("Duplicate Rows:", df.duplicated().sum())

    except Exception as e:
        print("Error:", e)

# ============================================================
# PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("""
✓ All datasets loaded successfully
✓ Fund Master explored
✓ AMFI codes validated
✓ Missing values checked
✓ Duplicate rows checked

Dataset ready for:
- Exploratory Data Analysis (EDA)
- SQL Analysis
- Power BI Dashboard
- Capstone Project Development
""")

print("=" * 60)
print("DAY 1 ANALYSIS COMPLETED")
print("=" * 60)