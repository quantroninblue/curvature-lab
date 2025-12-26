import pandas as pd
import numpy as np


def institutional_calm_alpha(vix: pd.Series,
                              teny: pd.Series,
                              tb3m: pd.Series):
    """
    Carry + liquidity + vol compression calm alpha.
    """

    carry = teny - tb3m
    vol_comp = -vix.diff()
    liq = -(vix - vix.rolling(12).mean()) / vix.rolling(12).std()

    df = pd.concat([carry, vol_comp, liq], axis=1).dropna()
    carry, vol_comp, liq = df.iloc[:,0], df.iloc[:,1], df.iloc[:,2]

    raw = np.sign(carry) * liq * vol_comp
    alpha = raw.clip(-2, 2).fillna(0)
    alpha.name = "CALM_ALPHA"
    return alpha
