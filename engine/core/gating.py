import pandas as pd


def apply_gravity_gate(signal: pd.Series, gravity: pd.Series) -> pd.Series:
    """
    Hard binary gating.
    """
    g = gravity.reindex(signal.index).fillna(0)
    gated = signal * g
    gated.name = "GATED_SIGNAL"
    return gated
