import pandas as pd

from engine.core.convex_signal import convex_signal
from engine.core.gating import apply_gravity_gate


def run_reactor(returns: pd.Series, gravity: pd.Series, power: float = 2.0):
    """
    Execute convex crash reactor.
    """
    signal = convex_signal(returns, power)
    gated = apply_gravity_gate(signal.shift(1), gravity)
    pnl = gated
    pnl.name = "REACTOR_PNL"
    return pnl
