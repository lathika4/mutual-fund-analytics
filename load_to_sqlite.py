from sqlalchemy import create_engine
import pandas as pd
import os

DATA_PATH = "data/processed"

engine = create_engine("sqlite:///bluestock_mf.db")

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 60)
print("LOADING DATA INTO SQLITE")
print("=" * 60)

for file in files:
    path = os.path.join(DATA_PATH, file)

    if os.path.exists(path):
        table_name = file.replace(".csv", "")
        df = pd.read_csv(path)

        df.to_sql(table_name, engine, if_exists="replace", index=False)

        print(f"Loaded {table_name}: {len(df)} rows")

    else:
        print(f"File not found: {file}")

print("\nSQLite database created successfully!")