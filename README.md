# Matplotlib Jewelry Retail Insights

A practical Matplotlib portfolio project that turns synthetic jewelry retail data into an executive visual story.

> All data is synthetic. It is not sourced from Tanishq, Malabar, or any other real retailer.

## Business use case

A jewelry retail leadership team needs a monthly performance review that answers:

1. Are sales growing, declining, or seasonal?
2. Which regions contribute the most revenue?
3. Does higher store footfall generally relate to higher sales?
4. How different are festival and regular months?
5. Are model errors random, or does the sales forecast systematically miss certain periods?

The output is a six-panel Matplotlib dashboard designed for marketing, store operations, inventory planning, and finance discussions.

## Why Matplotlib

Matplotlib is appropriate because it offers precise control over figures, axes, labels, annotations, layouts, and exported images. This project demonstrates:

- The Figure and Axes object model
- Line, bar, scatter, histogram, and box plots
- Multiple plots with `plt.subplots()`
- Labels, legends, grids, annotations, and formatting
- Actual-versus/forecast residual analysis
- High-resolution chart export
- Translation of charts into business decisions

## Project structure

```text
matplotlib-jewelry-retail-insights/
├── data/
│   └── jewelry_monthly_performance.csv
├── notebooks/
│   └── matplotlib_business_visualization.ipynb
├── reports/
│   └── figures/
│       └── jewelry_retail_dashboard.png
├── src/
│   ├── generate_data.py
│   └── create_dashboard.py
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Dataset

The generator creates 36 months of observations for 10 stores, producing 360 store-month rows.

| Field | Meaning |
|---|---|
| `month` | Month represented by the row |
| `store_id` | Synthetic store identifier |
| `region` | North, South, East, or West |
| `footfall` | Monthly store visitors |
| `digital_ad_spend_lakh` | Digital advertising investment |
| `festival_month` | Major jewelry-demand period indicator |
| `actual_sales_lakh` | Synthetic actual monthly sales |
| `predicted_sales_lakh` | Synthetic planning forecast |
| `residual_lakh` | Actual sales minus predicted sales |

## Dashboard panels

| Plot | Business question | Decision supported |
|---|---|---|
| Line chart | How are total sales changing over time? | Seasonal planning |
| Bar chart | Which region has the highest average sales? | Regional prioritization |
| Scatter plot | Is footfall associated with sales? | Store operations and conversion analysis |
| Histogram | What is the normal monthly sales range? | Target setting and anomaly review |
| Box plot | Do festival months behave differently? | Campaign and inventory timing |
| Residual plot | Where does the forecast over- or under-predict? | Model-risk and planning review |

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src\generate_data.py
python src\create_dashboard.py
```

The dashboard is saved to `reports/figures/jewelry_retail_dashboard.png`.

## Example business interpretation

- A visible festival uplift supports increasing inventory and campaign readiness before high-demand months.
- A positive footfall-sales relationship suggests traffic matters, but management should also examine conversion rate and average transaction value.
- Regional averages highlight where deeper store-level investigation is needed; they do not prove regional causation.
- A centered, pattern-free residual plot suggests the planning forecast is reasonably balanced. Curves or funnels would indicate model limitations.

## License

Released under the MIT License.


