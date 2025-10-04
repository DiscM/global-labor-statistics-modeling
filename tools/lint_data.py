import sys
from pathlib import Path
import pandas as pd
from schemas.panel_schema import SCHEMA

def main(path: str):
    p = Path(path)
    df = pd.read_csv(p)
    SCHEMA.validate(df, lazy=True)
    dups = df.duplicated(["country", "year"]).sum()
    if dups:
        raise AssertionError(f"{dups} duplicate country-year rows")
    print(f"{p} ✓")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "okun-law/data/raw/labor_panel_sample.csv")
