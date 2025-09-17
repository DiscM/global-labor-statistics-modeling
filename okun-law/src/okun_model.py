import pandas as pd
import statsmodels.api as sm

def fe_okun(df: pd.DataFrame):
    d = df.dropna(subset=['du','gdp_growth','country','year']).copy()
    d = pd.get_dummies(d, columns=['country','year'], drop_first=True)
    y = d['du']
    X = d.drop(columns=['du'])
    X = sm.add_constant(X, has_constant='add')
    model = sm.OLS(y, X).fit(cov_type='HC1')
    return model
