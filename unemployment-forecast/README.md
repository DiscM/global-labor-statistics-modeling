# Unemployment forecasting demo

Univariate per‑country baselines with tiny rolling forecasts.

**Run**
```bash
python -m venv ../../.venv && source ../../.venv/bin/activate  # Windows: ../../.venv\Scripts\activate
pip install -r ../../requirements.txt
python src/forecast_unemployment.py --data data/raw/labor_panel_sample.csv
```

Outputs land in `reports/`:
- `forecast_metrics.csv`
- `forecast_example_USA.png`
