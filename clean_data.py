import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

# ============================================================
# CLEAN NAV HISTORY
# ============================================================

print("\nCleaning 02_nav_history.csv...")

nav = pd.read_csv(os.path.join(RAW_PATH, "02_nav_history.csv"))

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort data
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicate rows
nav = nav.drop_duplicates()

# Forward fill missing NAV values within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    os.path.join(PROCESSED_PATH, "02_nav_history.csv"),
    index=False
)

print("Rows after cleaning:", len(nav))
print("Missing NAV values:", nav["nav"].isnull().sum())
print("Duplicates:", nav.duplicated().sum())
print("✅ Cleaned file saved to data/processed/")
# ============================================================
# CLEAN INVESTOR TRANSACTIONS
# ============================================================

print("\nCleaning 08_investor_transactions.csv...")

transactions = pd.read_csv(os.path.join(RAW_PATH, "08_investor_transactions.csv"))

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]
transactions = transactions[
    transactions["transaction_type"].isin(valid_types)
]

transactions = transactions[
    transactions["amount_inr"] > 0
]

transactions["kyc_status"] = (
    transactions["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]
transactions = transactions[
    transactions["kyc_status"].isin(valid_kyc)
]

transactions = transactions.drop_duplicates()

transactions.to_csv(
    os.path.join(PROCESSED_PATH, "08_investor_transactions.csv"),
    index=False
)

print("Rows after cleaning:", len(transactions))
print("Missing Values:")
print(transactions.isnull().sum())
print("Duplicate Rows:", transactions.duplicated().sum())
print("✅ Cleaned file saved to data/processed/")
# ============================================================
# CLEAN SCHEME PERFORMANCE
# ============================================================

print("\nCleaning 07_scheme_performance.csv...")

performance = pd.read_csv(
    os.path.join(RAW_PATH, "07_scheme_performance.csv")
)

# Columns that should contain numeric return values
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert return columns to numeric
for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Remove rows with missing return values
performance = performance.dropna(subset=return_columns)

# Keep only valid expense ratios (0.1% to 2.5%)
performance = performance[
    (performance["expense_ratio_pct"] >= 0.1) &
    (performance["expense_ratio_pct"] <= 2.5)
]

# Remove duplicate rows
performance = performance.drop_duplicates()

# Save cleaned dataset
performance.to_csv(
    os.path.join(PROCESSED_PATH, "07_scheme_performance.csv"),
    index=False
)

print("Rows after cleaning:", len(performance))
print("Missing Values:")
print(performance.isnull().sum())
print("Duplicate Rows:", performance.duplicated().sum())
print("✅ Cleaned file saved to data/processed/")
