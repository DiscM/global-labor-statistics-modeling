import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from pathlib import Path

def main(data_path: str):
    out_dir = Path(__file__).resolve().parents[1] / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)
    # compute change in unemployment by country
    df = df.sort_values(["country", "year"])
    df["delta_ur"] = df.groupby("country")["unemployment_rate"].diff()
    df = df.dropna(subset=["delta_ur", "gdp_growth"])

    # simple fixed-effects via country dummies
    model = smf.ols("delta_ur ~ gdp_growth + C(country)", data=df).fit(cov_type="HC1")
    summary_text = model.summary().as_text()

    (out_dir / "okun_law_summary.txt").write_text(summary_text)

    # scatter plot
    plt.figure(figsize=(6,4))
    plt.scatter(df["gdp_growth"], df["delta_ur"], alpha=0.5)
    plt.xlabel("GDP growth (%)")
    plt.ylabel("Δ unemployment (pp)")
    plt.title("Okun's Law: Δunemployment vs GDP growth")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "okun_law_scatter.png", dpi=200)

    # also print key coefficient
    coef = model.params.get("gdp_growth", float("nan"))
    print(f"Okun coefficient (slope on GDP growth): {coef:.3f} pp per 1% growth")
    print(f"Results saved to: {out_dir}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True, help="CSV with columns: country, year, unemployment_rate, gdp_growth, ...")
    args = p.parse_args()
    main(args.data)
