"""
Monte Carlo revenue simulation with LP inside each draw.

Running LP once on expected EV gives one optimal list.
Running LP inside 10,000 draws gives a distribution of
optimal lists — selection probability per donor, not binary.
"""
import numpy as np
import pandas as pd


def simulate_campaign_revenue(
    donor_intelligence: pd.DataFrame,
    budget: float,
    n_simulations: int = 10_000,
) -> dict:
    """
    Sample P(donate) uncertainty → run LP → revenue distribution.
    Returns p10, p50, p90 revenue and per-donor selection frequency.
    """
    raise NotImplementedError("Implement in W7")
