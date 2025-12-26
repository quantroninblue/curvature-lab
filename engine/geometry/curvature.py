import numpy as np
import pandas as pd


def map_curvature(stress_energy: pd.Series) -> pd.Series:
    """
    Log-compressed curvature mapping.
    """
    x = stress_energy.copy()
    curvature = np.sign(x) * np.log1p(np.abs(x))
    curvature.name = "CURVATURE"
    return curvature
