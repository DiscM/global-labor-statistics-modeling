# Global Labor: Okun's Law + Unemployment Forecasting

Side project. Two small modeling demos on a country–year panel (1991–2022).

**Folders**
- `okun-law/` — Estimate Okun’s coefficient (Δ unemployment vs GDP growth) with a quick OLS using country fixed effects.
- `unemployment-forecast/` — Fit simple per‑country time‑series baselines and plot forecasts.

**Quickstart**
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Open the notebooks
jupyter notebook okun-law/notebooks/01_eda_okun.ipynb
jupyter notebook unemployment-forecast/notebooks/02_forecast_models.ipynb
```

**Data**
- A tiny sample CSV is included at `<project>/data/raw/labor_panel_sample.csv` so everything runs out of the box.
- Replace it with your own panel when ready. Expected columns:
  - `country`, `year`, `unemployment_rate`, `gdp_growth`, `labor_force_participation`, `gdp_per_capita`, `region`
- Years are integers. Rates are percentages.

**Make targets**
```bash
make install        # create venv and install deps
make okun           # run Okun’s-law script and save outputs under okun-law/reports/
make forecast       # run forecasting script and save outputs under unemployment-forecast/reports/
make clean          # remove generated reports
```

**Notes**
- Methods are intentionally lightweight and non‑authoritative.
- Feel free to tweak formulas, models, and plots.
