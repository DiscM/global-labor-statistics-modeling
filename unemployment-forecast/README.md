# Unemployment Forecasting with Calibrated Uncertainty

**Goal**: Forecast country-level unemployment rates and provide **well-calibrated** prediction intervals (split conformal).

## Methods (baseline)
- Features: lags of unemployment (and GDP growth if available).
- Models: Linear baseline with rolling-origin evaluation; add ML as extensions.
- Uncertainty: **split conformal** intervals with empirical coverage checks.

## Data column mapping
| Source column | Used as |
|---|---|
| `Country Name` | `country` |
| `Year` | `year` |
| `Unemployment Rate` | `unemployment_rate` |
| `GDP (in USD)` | `gdp` |

## How to run
1. The dataset CSV is already in `data/raw/`.
2. Open `notebooks/01_eda_forecast.ipynb` then `02_forecast_models.ipynb`.

## References (authoritative)
- ILO unemployment definition/topic (ilostat.ilo.org).  
- World Bank WDI unemployment indicator **SL.UEM.TOTL.ZS** (metadata, definitions).  
- Conformal prediction tutorials/papers (Angelopoulos & Bates; Shafer & Vovk).
