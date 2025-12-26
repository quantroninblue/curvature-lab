import pandas as pd
import numpy as np


def convex_signal(returns: pd.Series, power: float = 2.0) -> pd.Series:
    """
    Rare-event convex crash signal.
    """
    sig = np.abs(returns) ** power
    sig.name = "CONVEX_SIGNAL"
    return sig
