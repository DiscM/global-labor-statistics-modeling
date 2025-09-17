# Full Write-up: Unemployment Forecasting

**RQ1**: Accuracy of naive/linear baselines across countries.  
**RQ2**: Coverage and width of conformal intervals.  
**RQ3**: Value of including GDP growth among predictors.

**Data & Features**: Country–year unemployment with 3 lags; GDP growth computed from level where available.  
**Evaluation**: Rolling-origin per country; MAE/RMSE; coverage and interval width.  
**Limitations**: Small samples for some countries; non-stationarity; revisions.
