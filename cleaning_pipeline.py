
import pandas as pd
import numpy as np

def clean_agent_data(txns, agents):
    """
    Clean agent transaction data and return a cleaned DataFrame
    together with a log of the cleaning actions.
    """
    clean = txns.copy()
    log = {}
    log["original_rows"] = len(clean)

    # Remove duplicate transactions
    before = len(clean)
    clean = clean.drop_duplicates(
        subset="txn_id", keep="first"
    ).copy()
    log["duplicate_rows_removed"] = before - len(clean)

    # Standardise transaction types
    clean["txn_type"] = (
        clean["txn_type"].astype(str).str.strip().str.lower()
    )
    clean["txn_type"] = clean["txn_type"].map({
        "deposit": "Deposit",
        "withdrawal": "Withdrawal"
    })

    # Convert amounts and fill missing values
    clean["amount"] = pd.to_numeric(
        clean["amount"], errors="coerce"
    )
    clean["amount_imputed"] = clean["amount"].isna()
    median_amount = clean["amount"].median()
    clean["amount"] = clean["amount"].fillna(median_amount)

    # Flag outliers using IQR
    q1 = clean["amount"].quantile(0.25)
    q3 = clean["amount"].quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    clean["is_outlier"] = (
        (clean["amount"] < lower_limit) |
        (clean["amount"] > upper_limit)
    )

    # Standardise transaction dates
    clean["txn_date"] = pd.to_datetime(
        clean["txn_date"],
        format="mixed",
        errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    # Add county information
    clean = clean.merge(
        agents[["agent_id", "county"]],
        on="agent_id",
        how="left"
    )

    log["unknown_agent_transactions"] = clean["county"].isna().sum()
    log["final_rows"] = len(clean)

    return clean, log
