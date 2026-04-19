"""
5-state Markov chain for donor lapse velocity.

States: Active → Warm → AtRisk → Lapsed → Lost
Anchored to the 24-month business-active boundary.
AtRisk donors (still business-active) have ~27% monthly
probability of crossing into Lapsed.
"""
import numpy as np
import pandas as pd


STATES = ["Active", "Warm", "AtRisk", "Lapsed", "Lost"]


def build_transition_matrix(transactions: pd.DataFrame) -> np.ndarray:
    """
    Estimate monthly transition probabilities from full donor history.
    Returns 5x5 matrix where entry [i,j] = P(state_j | state_i).
    """
    raise NotImplementedError("Implement in W7")


def assign_markov_state(rfm: pd.DataFrame, active_boundary_months: int = 24) -> pd.Series:
    """Assign current Markov state to each donor based on recency."""
    raise NotImplementedError("Implement in W7")


def compute_lapse_velocity(transition_matrix: np.ndarray) -> pd.Series:
    """
    Monthly probability of downward state transition per donor.
    Key output: AtRisk → Lapsed probability drives campaign prioritisation.
    """
    raise NotImplementedError("Implement in W7")
