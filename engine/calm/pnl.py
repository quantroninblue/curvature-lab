import pandas as pd


def calm_pnl(exposure: pd.Series, price: pd.Series):
    """
    Exposure × next return.
    """
    ret = price.pct_change().shift(-1)
    pnl = exposure * ret
    pnl.name = "CALM_PNL"
    return pnl
