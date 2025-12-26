import pandas as pd


def build_event_table(curvature, gravity, returns, pnl):
    """
    Canonical gravity event table.
    """
    df = pd.concat({
        "curvature": curvature,
        "gravity": gravity,
        "returns": returns,
        "pnl": pnl
    }, axis=1).dropna()

    events = df[df["gravity"] == 1]
    return events
