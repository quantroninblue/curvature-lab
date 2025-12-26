from engine.geometry.mass_inputs import load_mass_fields
from engine.geometry.stress_energy import build_stress_energy
from engine.geometry.curvature import map_curvature
from engine.geometry.gravity import build_gravity
from engine.core.reactor import run_reactor
from engine.data_loader import load_fred_series
import numpy as np

# Build gravity field
funding, collateral, liquidity = load_mass_fields()
T = build_stress_energy(funding, collateral, liquidity)
C = map_curvature(T)
G = build_gravity(C)

# Load market
sp = load_fred_series("SP500")["SP500"].pct_change().dropna()

# Run reactor
pnl = run_reactor(sp, G)

print("Total PnL:", pnl.sum())
print("Active months:", (pnl != 0).sum())
print(pnl[pnl != 0].tail())
