import pandas as pd


def build_gravity(curvature: pd.Series, quantile: float = 0.9) -> pd.Series:
    """
    Binary gravity regime. Event horizon at top curvature quantile.
    """
    threshold = curvature.quantile(quantile)
    gravity = (curvature >= threshold).astype(int)
    gravity.name = "GRAVITY"
    return gravity
