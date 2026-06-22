import pandas as pd
import os

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