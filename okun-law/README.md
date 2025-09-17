# Okun's Law: GDP Growth & Unemployment (1991–2022)

**Goal**: Estimate Okun’s coefficient (β) by country and groups, relating Δunemployment to GDP growth.

## Methods (baseline)
- Panel FE regression: Δu_it = α + β g_it + μ_i + τ_t + ε_it
- Inference: **robust (HC1)** SEs via statsmodels.
- Optional extensions (not required to run): Driscoll–Kraay SEs; dynamic panel (Arellano–Bond).

## Data column mapping
| Source column | Used as |
|---|---|
| `Country Name` | `country` |
| `Year` | `year` |
| `Unemployment Rate` | `unemployment_rate` |
| `GDP (in USD)` | `gdp` |
| Employment sector columns | `emp_agri`, `emp_ind`, `emp_srv` |

## How to run
1. The dataset CSV is already in `data/raw/`.
2. Open `notebooks/01_eda_okun.ipynb` then `02_model_okun.ipynb`.
3. Outputs go to `reports/figures/` and `data/processed/`.

## References (authoritative)
- ILO unemployment topic & definition (ilostat.ilo.org)  
- World Bank WDI unemployment indicator **SL.UEM.TOTL.ZS** and metadata.  
- IMF World Economic Outlook (WEO) databases.  
- Penn World Table 10.x (PPP GDP).  
- Okun’s Law: Ball, Leigh, & Loungani (2013, NBER).  
- Robust inference (Driscoll–Kraay): Hoechle (2007, *Stata Journal*).  
- Dynamic panel (Arellano–Bond, 1991, *Review of Economic Studies*).
