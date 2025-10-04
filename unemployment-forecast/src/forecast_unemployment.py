import argparse
import warnings
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def fit_one_country(ts, train_tail=3):
    ts = ts.sort_values("year")
    y = ts["unemployment_rate"].values
    years = ts["year"].values
    # hold out last 'train_tail' years
    if len(y) <= train_tail + 3:
        return None  # too short
    y_train, y_test = y[:-train_tail], y[-train_tail:]
    years_train, years_test = years[:-train_tail], years[-train_tail:]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = ARIMA(y_train, order=(1,0,0))
        res = model.fit()
        fc = res.forecast(steps=train_tail)
    mae = float(np.mean(np.abs(fc - y_test)))
    return {
        "mae": mae,
        "years_test": years_test.tolist(),
        "y_test": y_test.tolist(),
        "y_pred": fc.tolist()
    }

def main(data_path: str):
    out_dir = Path(__file__).resolve().parents[1] / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)
    metrics = []
    example_plot_done = False

    for country, g in df.groupby("country"):
        res = fit_one_country(g)
        if res is None:
            continue
        metrics.append({"country": country, "mae": res["mae"]})
        # plot only the first country as an example
        if not example_plot_done:
            years = g["year"].values
            y = g["unemployment_rate"].values
            plt.figure(figsize=(7,4))
            plt.plot(years, y, label="actual")
            # align preds to test years
            plt.plot(res["years_test"], res["y_pred"], label="forecast")
            plt.xlabel("Year")
            plt.ylabel("Unemployment rate (%)")
            plt.title(f"Unemployment forecast example: {country}")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(out_dir / "forecast_example_USA.png", dpi=200)
            example_plot_done = True

    pd.DataFrame(metrics).sort_values("mae").to_csv(out_dir / "forecast_metrics.csv", index=False)
    print(f"Saved metrics and example plot to {out_dir}")

if __name__ == \"__main__\":
    p = argparse.ArgumentParser()
    p.add_argument(\"--data\", required=True, help=\"CSV with columns: country, year, unemployment_rate, ...\")
    args = p.parse_args()
    main(args.data)
