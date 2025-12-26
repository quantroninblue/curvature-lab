from engine.data_loader import load_fred_series


def load_mass_fields():
    """
    Core gravity mass fields.
    """
    funding = load_fred_series("DTB3")["DTB3"]          # 3m T-bill yield
    collateral = load_fred_series("M2SL")["M2SL"]       # Money supply
    liquidity = load_fred_series("WALCL")["WALCL"]      # Fed balance sheet
    return funding, collateral, liquidity


def load_calm_mass_fields():
    """
    Calm-regime carry & liquidity fields.
    """
    vix = load_fred_series("VIXCLS")["VIXCLS"]      # VIX
    teny = load_fred_series("DGS10")["DGS10"]       # 10Y
    tb3m = load_fred_series("DTB3")["DTB3"]         # 3M
    return vix, teny, tb3m

