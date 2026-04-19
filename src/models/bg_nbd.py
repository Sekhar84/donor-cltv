"""
BG/NBD model — P(alive) and expected future transactions.

Wraps the lifetimes BetaGeoFitter with project-specific
validation and MLflow logging.
"""
from lifetimes import BetaGeoFitter
import pandas as pd


def fit_bg_nbd(rfm: pd.DataFrame, penalizer_coef: float = 0.01) -> BetaGeoFitter:
    """
    Fit BG/NBD model on full donor population (active + inactive).
    Training on all donors — including lapsed — is required so the
    model sees what pre-lapse behaviour looks like.
    """
    raise NotImplementedError("Implement in W7")


def predict_p_alive(bgf: BetaGeoFitter, rfm: pd.DataFrame) -> pd.Series:
    """Return P(alive) per donor at snapshot date."""
    raise NotImplementedError("Implement in W7")


def predict_expected_purchases(
    bgf: BetaGeoFitter, rfm: pd.DataFrame, t: float
) -> pd.Series:
    """Return expected number of purchases in next t time units."""
    raise NotImplementedError("Implement in W7")
