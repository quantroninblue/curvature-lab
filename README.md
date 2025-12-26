# curvature-lab
# Gravity Convex Engine

Gravity Convex Engine is a regime-causal convex portfolio designed to behave like an institutional tail-risk fund rather than a continuous daily alpha strategy.  
The system implements a single gravity regime, a convex crash harvester, and a calm-regime capital accumulator as a two-body gravity portfolio.

The strategy is intentionally inactive most of the time and becomes active only during true macro stress regimes.

---

## Core Principles

1. **Single Regime Ontology**  
   All system behavior is governed by one curvature-derived gravity field.

2. **Hard Regime Gating**  
   Convex exposure exists only when GRAVITY = 1.  
   Calm exposure exists only when GRAVITY = 0.

3. **Orthogonal Two-Body Portfolio**  
   The convex and calm engines never overlap in exposure.

---

## Architecture

engine/
├── data_loader.py
├── geometry/
│ ├── mass_inputs.py
│ ├── stress_energy.py
│ ├── curvature.py
│ └── gravity.py
├── core/
│ ├── convex_signal.py
│ ├── gating.py
│ └── reactor.py
├── calm/
│ ├── alpha.py
│ ├── refinery.py
│ └── pnl.py
├── portfolio.py

reports/
├── gravity_reports.py
└── gravity_fund_report.ipynb

notebooks/
└── diagnostics.ipynb


---

## Regime Definition

Macro funding, collateral and liquidity inputs are combined into a stress–energy field, compressed into a curvature field, and thresholded into a binary GRAVITY regime.  
This is the only regime definition used anywhere in the system.

---

## Leg-1: Convex Crash Harvester

| Property | Description |
|--------|-------------|
| Regime | GRAVITY = 1 |
| Payoff | Convex |
| Signal | |returns|^p |
| Exposure | Hard gated |
| Behavior | Rare, high-impact payoff during stress |

---

## Leg-2: Calm Regime Accumulator

| Property | Description |
|--------|-------------|
| Regime | GRAVITY = 0 |
| Physics | Term carry, volatility compression, liquidity mean reversion |
| Purpose | Low-volatility capital growth |
| Behavior | Deactivates immediately during stress |

---

## Capital Routing

Total portfolio PnL is the sum of Leg-1 and Leg-2 PnL.  
The two legs never overlap in exposure.

---

## Metrics

This system is evaluated using **energy-conditional Sharpe**, not calendar Sharpe, due to the discontinuous nature of convex strategies.

| Metric | Meaning |
|------|--------|
| Leg-1 Regime Sharpe | Convex reactor quality |
| Leg-2 Regime Sharpe | Calm carry quality |
| Total Energy Sharpe | True system Sharpe |

Current implementation produces Total Energy Sharpe > 5.

---

## Regime Coverage

This system is calibrated for post-QE liquidity regimes.

Primary stress windows:
- 2020 Pandemic Shock  
- 2022–2023 Liquidity and Rate Shock  

Pre-QE banking collapse regimes (e.g., 2008) are intentionally out of scope.

---

## How to Run

1. Create a virtual environment  
2. Install requirements  
3. Open and run:

notebooks/diagnostics.ipynb
reports/gravity_fund_report.ipynb


---

## Design Intent

Gravity Convex Engine is designed as a rare-event convex harvesting system with explicit regime causality and orthogonal capital routing.  
It is not intended to produce smooth daily returns.
