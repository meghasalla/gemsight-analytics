"""Create a multi-plot Matplotlib dashboard for jewelry retail leadership."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "jewelry_monthly_performance.csv"
OUTPUT_PATH = ROOT / "reports" / "figures" / "jewelry_retail_dashboard.png"


def currency_axis(axis, orientation="y"):
    formatter = plt.FuncFormatter(lambda value, _: f"₹{value:,.0f}")
    if orientation == "y":
        axis.yaxis.set_major_formatter(formatter)
    else:
        axis.xaxis.set_major_formatter(formatter)


def create_dashboard(data: pd.DataFrame) -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    colors = {"navy": "#172554", "gold": "#C69214", "teal": "#0F766E", "red": "#B91C1C"}
    fig, axes = plt.subplots(2, 3, figsize=(17, 10))
    fig.suptitle("Synthetic Jewelry Retail Performance", fontsize=20, fontweight="bold", color=colors["navy"])

    monthly = data.groupby("month", as_index=False)["actual_sales_lakh"].sum()
    axes[0, 0].plot(monthly["month"], monthly["actual_sales_lakh"], marker="o", linewidth=2.2, color=colors["gold"])
    axes[0, 0].set_title("Total sales trend")
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].set_ylabel("Sales (₹ lakh)")
    axes[0, 0].tick_params(axis="x", rotation=45)
    currency_axis(axes[0, 0])

    regional = data.groupby("region")["actual_sales_lakh"].mean().sort_values()
    axes[0, 1].bar(regional.index, regional.values, color=colors["teal"])
    axes[0, 1].set_title("Average store-month sales by region")
    axes[0, 1].set_xlabel("Region")
    axes[0, 1].set_ylabel("Average sales (₹ lakh)")
    currency_axis(axes[0, 1])

    axes[0, 2].scatter(data["footfall"], data["actual_sales_lakh"], alpha=0.5, color=colors["navy"])
    slope, intercept = np.polyfit(data["footfall"], data["actual_sales_lakh"], 1)
    x_line = np.array([data["footfall"].min(), data["footfall"].max()])
    axes[0, 2].plot(x_line, slope * x_line + intercept, color=colors["red"], linewidth=2, label="Linear trend")
    axes[0, 2].set_title("Footfall relationship")
    axes[0, 2].set_xlabel("Monthly visitors")
    axes[0, 2].set_ylabel("Sales (₹ lakh)")
    axes[0, 2].legend()

    axes[1, 0].hist(data["actual_sales_lakh"], bins=16, color=colors["gold"], edgecolor="white")
    axes[1, 0].set_title("Distribution of store-month sales")
    axes[1, 0].set_xlabel("Sales (₹ lakh)")
    axes[1, 0].set_ylabel("Number of observations")

    regular = data.loc[data["festival_month"] == 0, "actual_sales_lakh"]
    festival = data.loc[data["festival_month"] == 1, "actual_sales_lakh"]
    axes[1, 1].boxplot([regular, festival], tick_labels=["Regular", "Festival"], patch_artist=True,
                       boxprops={"facecolor": colors["teal"]}, medianprops={"color": colors["gold"], "linewidth": 2})
    axes[1, 1].set_title("Festival sales comparison")
    axes[1, 1].set_xlabel("Month type")
    axes[1, 1].set_ylabel("Sales (₹ lakh)")

    axes[1, 2].scatter(data["predicted_sales_lakh"], data["residual_lakh"], alpha=0.5, color=colors["navy"])
    axes[1, 2].axhline(0, linestyle="--", color=colors["red"], linewidth=2)
    axes[1, 2].set_title("Forecast residual check")
    axes[1, 2].set_xlabel("Predicted sales (₹ lakh)")
    axes[1, 2].set_ylabel("Actual − predicted (₹ lakh)")

    for axis in axes.flat:
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(alpha=0.22)

    fig.text(0.5, 0.01, "Synthetic data for portfolio demonstration — not real retailer performance", ha="center", color="#555555")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=220, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved dashboard to {OUTPUT_PATH}")


if __name__ == "__main__":
    frame = pd.read_csv(DATA_PATH, parse_dates=["month"])
    create_dashboard(frame)


