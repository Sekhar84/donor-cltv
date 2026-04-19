# donor-cltv · Customer Lifetime Value + Donor Intelligence

> CLTV modelling, Markov chain state transitions, and Monte Carlo revenue
> simulation for non-profit donor base management.
> Part of the donor intelligence system — see
> [donor-intelligence-system](https://github.com/Sekhar84/donor-intelligence-system)

## What this does

Transforms a donor transaction history into a unified donor intelligence
table — one row per donor, four models combined into a single actionable
output.

| Column | Model | What it tells you |
|--------|-------|-------------------|
| p_alive | BG/NBD | Probability donor hasn't lapsed |
| cltv_1yr | BG/NBD + Gamma-Gamma | Expected 12-month revenue |
| markov_state | Markov chain | Current state: Active/Warm/AtRisk/Lapsed/Lost |
| monthly_lapse_risk | Markov transition matrix | Probability of state downgrade this month |
| revenue_p10/p50/p90 | Monte Carlo | Revenue confidence interval |
| action | Rule engine | retain / reactivate / winback / sunset |

## Quickstart

```bash
git clone https://github.com/Sekhar84/donor-cltv.git
cd donor-cltv
poetry install
poetry run pytest --cov=src
poetry run python -m src.intelligence \
  --transactions data/transactions.parquet \
  --output results/donor_intelligence.parquet
```

## Architecture

Transaction history → RFM → BG/NBD → Gamma-Gamma → CLTV
                                   → Markov chain → lapse velocity
                                   → Monte Carlo (LP inside) → revenue CI
                                   → donor_intelligence table

## Key design decisions

- Train on ALL donors (active + inactive) — BG/NBD needs lapsed donors
  to estimate dropout rate correctly
- 5-state Markov anchored to 24-month business boundary — At-Risk donors
  have 27% monthly probability of crossing into Lapsed
- LP inside Monte Carlo — gives selection probability per donor,
  not just binary in/out
- Scored on business-active donors only (≤24 months)

## Part of the DS modernisation project

[donor-ev-scorer](https://github.com/Sekhar84/donor-ev-scorer) ·
[donor-causal](https://github.com/Sekhar84/donor-causal) ·
[ds-mlops-stack](https://github.com/Sekhar84/ds-mlops-stack) ·
[donor-intelligence-system](https://github.com/Sekhar84/donor-intelligence-system)
