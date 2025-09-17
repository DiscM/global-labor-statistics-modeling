import numpy as np

def split_conformal_intervals(residuals, alpha=0.1):
    q = np.quantile(residuals, 1 - alpha)
    return float(q)

def apply_conformal(preds, q):
    lower = preds - q
    upper = preds + q
    return lower, upper

def empirical_coverage(trues, lower, upper):
    hits = (trues >= lower) & (trues <= upper)
    return float(np.mean(hits))
