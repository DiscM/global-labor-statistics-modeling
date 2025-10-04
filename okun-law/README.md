# Okun's Law demo

Quick OLS of Δ unemployment on GDP growth using country dummies.

**Run**
```bash
python -m venv ../../.venv && source ../../.venv/bin/activate  # Windows: ../../.venv\Scripts\activate
pip install -r ../../requirements.txt
python src/fit_okun.py --data data/raw/labor_panel_sample.csv
```

Outputs land in `reports/`:
- `okun_law_summary.txt`
- `okun_law_scatter.png`
