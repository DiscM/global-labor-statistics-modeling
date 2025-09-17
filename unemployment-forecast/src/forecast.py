import numpy as np, pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def rolling_origin_forecast(df: pd.DataFrame, country: str, min_train: int=10):
    d = df[df['country']==country].sort_values('year').dropna().copy()
    features = [c for c in d.columns if c.startswith('u_lag') or c.startswith('g_lag')]
    if not features:
        raise ValueError('No lag features found. Build supervised table first.')
    y, X = d['unemployment_rate'].values, d[features].values
    preds, trues = [], []
    for t in range(min_train, len(d)):
        model = LinearRegression().fit(X[:t], y[:t])
        p = model.predict(X[t:t+1])[0]
        preds.append(p); trues.append(y[t])
    return np.array(trues), np.array(preds)

def mae(trues, preds) -> float:
    return float(mean_absolute_error(trues, preds))
