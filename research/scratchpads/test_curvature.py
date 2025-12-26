from engine.geometry.mass_inputs import load_mass_fields
from engine.geometry.stress_energy import build_stress_energy
from engine.geometry.curvature import map_curvature
from engine.geometry.gravity import build_gravity

funding, collateral, liquidity = load_mass_fields()

T = build_stress_energy(funding, collateral, liquidity)
C = map_curvature(T)
G = build_gravity(C)

print(G.value_counts())
print(G.tail())
