"""
RFM feature engineering from raw transaction history.

All features computed at snapshot_date T — no lookahead.
Used by BG/NBD (frequency, recency, T) and as input
features for the EV model in donor-ev-scorer.
"""
import pandas as pd


def build_rfm(
    transactions: pd.DataFrame,
    snapshot_date: pd.Timestamp,
) -> pd.DataFrame:
    """
    Compute per-donor RFM summary anchored to snapshot_date.

    Returns DataFrame with columns:
        donor_id, frequency, recency, T, monetary,
        months_since_last, is_business_active
    """
    raise NotImplementedError("Implement in W7")
