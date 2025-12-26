import pandas as pd


def build_stress_energy(funding: pd.Series,
                         collateral: pd.Series,
                         liquidity: pd.Series) -> pd.Series:
    """
    Stress–energy field from funding, collateral and liquidity proxies.
    All inputs must be aligned time series.
    """

    df = pd.concat({
        "funding": funding,
        "collateral": collateral,
        "liquidity": liquidity
    }, axis=1).dropna()

    z = (df - df.mean()) / df.std()
    T = z.mean(axis=1)
    T.name = "STRESS_ENERGY"
    return T
