import pandas as pd, re, numpy as np, pathlib

def _normalize_columns(cols):
    out = []
    for c in cols:
        c2 = c.strip().lower().replace(' ', '_')
        c2 = c2.replace(':','').replace('(','').replace(')','').replace('/','_').replace('-','_')
        c2 = re.sub(r'__+','_', c2)
        out.append(c2)
    return out

def _apply_default_mappings(df: pd.DataFrame) -> pd.DataFrame:
    mapping = {
        'country_name': 'country',
        'gdp_in_usd': 'gdp',
        'employment_sector_agriculture': 'emp_agri',
        'employment_sector_industry': 'emp_ind',
        'employment_sector_services': 'emp_srv',
        'unemployment_rate': 'unemployment_rate'
    }
    for k,v in mapping.items():
        if k in df.columns and v not in df.columns:
            df = df.rename(columns={k:v})
    return df

def load_raw_any(raw_dir: str) -> pd.DataFrame:
    p = pathlib.Path(raw_dir)
    files = list(p.glob('*.csv'))
    assert files, f'No CSVs found in {raw_dir}'
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    df.columns = _normalize_columns(df.columns)
    df = _apply_default_mappings(df)
    return df

def make_supervised(df: pd.DataFrame, lags: int=3) -> pd.DataFrame:
    out = df.copy().sort_values(['country','year'])
    assert {'country','year','unemployment_rate'}.issubset(out.columns)
    # GDP growth if possible
    if 'gdp_growth' not in out.columns and 'gdp' in out.columns:
        out['gdp'] = pd.to_numeric(out['gdp'], errors='coerce')
        out['gdp_growth'] = out.groupby('country')['gdp'].pct_change()*100.0
    out['unemployment_rate'] = pd.to_numeric(out['unemployment_rate'], errors='coerce')
    for L in range(1, lags+1):
        out[f'u_lag{L}'] = out.groupby('country')['unemployment_rate'].shift(L)
        if 'gdp_growth' in out.columns:
            out[f'g_lag{L}'] = out.groupby('country')['gdp_growth'].shift(L)
    out = out.dropna(subset=[f'u_lag{lags}'])
    return out