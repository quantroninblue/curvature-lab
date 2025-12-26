from engine.calm.alpha import institutional_calm_alpha
from engine.geometry.mass_inputs import load_calm_mass_fields


def run_calm_refinery(gravity):
    vix, teny, tb3m = load_calm_mass_fields()
    alpha = institutional_calm_alpha(vix, teny, tb3m)

    g = gravity.reindex(alpha.index).ffill().fillna(0)
    exposure = alpha * (1 - g)
    exposure.name = "CALM_EXPOSURE"
    return exposure
