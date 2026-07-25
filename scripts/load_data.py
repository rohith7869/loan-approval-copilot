"""
Load all 7 Home Credit CSVs into PostgreSQL.
Run with: poetry run load
"""

import pandas as pd
from sqlalchemy import text

from app.db.database import engine

FILES = [
    ("data/raw/application_train.csv", "applicants"),
    ("data/raw/bureau.csv", "bureau"),
    ("data/raw/bureau_balance.csv", "bureau_balance"),
    ("data/raw/previous_application.csv", "previous_application"),
    ("data/raw/POS_CASH_balance.csv", "pos_cash_balance"),
    ("data/raw/installments_payments.csv", "installments_payments"),
    ("data/raw/credit_card_balance.csv", "credit_card_balance"),
]

CHUNK_SIZE = 10_000


def load_file(csv_path, table_name):
    print(f"\nLoading {csv_path} → {table_name}")

    # Clear existing data first
    with engine.connect() as conn:
        conn.execute(text(f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE'))
        conn.commit()
        print(f"  Cleared existing data from {table_name}")

    # Load in chunks
    total_rows = 0
    for i, chunk in enumerate(pd.read_csv(csv_path, chunksize=CHUNK_SIZE)):
        chunk.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False,
            method="multi",
        )
        total_rows += len(chunk)
        print(f"  Chunk {i+1}: {total_rows:,} rows loaded", end="\r")

    print(f"  ✓ Done — {total_rows:,} total rows loaded into {table_name}")
    return total_rows


def main():
    print("=== Loading Home Credit data into PostgreSQL ===")
    summary = {}

    for csv_path, table_name in FILES:
        try:
            rows = load_file(csv_path, table_name)
            summary[table_name] = rows
        except Exception as e:
            print(f"  ✗ Failed to load {table_name}: {e}")
            summary[table_name] = "FAILED"

    print("\n=== Summary ===")
    for table, rows in summary.items():
        print(
            f"  {table}: {rows:,} rows"
            if isinstance(rows, int)
            else f"  {table}: {rows}"
        )


if __name__ == "__main__":
    main()
