import pandas as pd


def route_capital(leg1_pnl: pd.Series, leg2_exposure: pd.Series):
    """
    Two-body gravity portfolio routing.
    """
    idx = leg1_pnl.index.union(leg2_exposure.index)

    l1 = leg1_pnl.reindex(idx).fillna(0)
    l2 = leg2_exposure.reindex(idx).fillna(0)

    total = l1 + l2
    total.name = "PORTFOLIO_PNL"
    return total
