"""Generate deterministic synthetic jewelry retail performance data."""

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "jewelry_monthly_performance.csv"
STORES = [
    ("STR-01", "West"), ("STR-02", "North"), ("STR-03", "South"),
    ("STR-04", "South"), ("STR-05", "South"), ("STR-06", "West"),
    ("STR-07", "East"), ("STR-08", "West"), ("STR-09", "North"),
    ("STR-10", "South"),
]


def generate() -> pd.DataFrame:
    rng = np.random.default_rng(73)
    rows = []
    for month_index, month in enumerate(pd.date_range("2023-09-01", periods=36, freq="MS")):
        festival = int(month.month in {3, 4, 10, 11})
        for store_index, (store_id, region) in enumerate(STORES, start=1):
            footfall = int(rng.integers(900, 3600))
            ad_spend = rng.uniform(5, 23)
            predicted = 55 + 0.025 * footfall + 1.4 * ad_spend + 19 * festival + store_index * 1.2 + month_index * 0.25
            actual = predicted + rng.normal(0, 9)
            rows.append({
                "month": month.strftime("%Y-%m-%d"),
                "store_id": store_id,
                "region": region,
                "footfall": footfall,
                "digital_ad_spend_lakh": round(ad_spend, 2),
                "festival_month": festival,
                "actual_sales_lakh": round(actual, 2),
                "predicted_sales_lakh": round(predicted, 2),
                "residual_lakh": round(actual - predicted, 2),
            })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data = generate()
    data.to_csv(OUTPUT, index=False)
    print(f"Created {OUTPUT}")
    print(f"Rows: {len(data)} | Stores: {data.store_id.nunique()} | Months: {data.month.nunique()}")


