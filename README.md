# Global Labor Projects: Okun's Law & Unemployment Forecasting

Two reproducible research projects built from a country–year panel (1991–2022):
- **`okun-law/`** — Estimate Okun’s coefficient (Δunemployment vs. GDP growth) by country and group.
- **`unemployment-forecast/`** — Forecast unemployment with **calibrated** prediction intervals (split conformal).

**Data**: A copy of your CSV is included in each project under `data/raw/`.  
**Environment**: plain `pip` + Jupyter (no Docker/conda needed).

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Open the notebooks
jupyter notebook okun-law/notebooks/01_eda_okun.ipynb
jupyter notebook unemployment-forecast/notebooks/02_forecast_models.ipynb
```

## Reproducibility
- Deterministic splits & seeds where applicable.
- Minimal pinned dependencies in `requirements.txt`.
- Lightweight tests under `tests/` (schema & citation smoke checks).

## Notes on methods
The Okun notebook fits a **baseline** fixed-effects OLS with robust (HC1) standard errors; Driscoll–Kraay SEs and dynamic panel (Arellano–Bond) are listed as **optional extensions** in the README, not required to run the baseline.

## Key references
See each project's README for live links and full references (ILO, WDI, IMF WEO, PWT, Okun literature, conformal prediction).

_Generated 2025-09-17_
