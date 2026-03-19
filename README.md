# BMW Global Automotive Sales Analysis

End-to-end analysis of BMW global automotive sales from `2018` to `2025`, covering data cleaning, exploratory data analysis, forecasting, and an interactive dashboard.

## Project Overview

This project answers three core questions:

- How have BMW sales changed over time?
- Which models, regions, and market patterns drive performance?
- What actions should the business take based on those findings?

The workflow is split into notebooks for cleaning, EDA, and forecasting, with a `Streamlit` dashboard for interactive exploration.

## Project Structure

```text
BMW_global_automotive_sales/
├── data/
│   ├── bmw_global_sales_2018_2025.csv
│   └── bmw_global_sales_2018_2025_cleaned.csv
├── notebooks/
│   ├── 1_cleaning.ipynb
│   ├── 2_EDA.ipynb
│   └── 3_Forcasting.ipynb
├── dashboard.py
└── README.md
```

## Dataset

Main cleaned file:

- `data/bmw_global_sales_2018_2025_cleaned.csv`

Key fields used in the analysis:

- `Year`, `Month`, `Date`
- `Region`, `Model`
- `Units_Sold`, `Revenue_EUR`, `Avg_Price_EUR`
- `BEV_Share`, `Premium_Share`
- `GDP_Growth`, `Fuel_Price_Index`

## Tools Used

- `Python`
- `Pandas`, `NumPy`
- `Matplotlib`, `Seaborn`
- `Statsmodels`
- `Prophet`
- `Streamlit`

## Notebooks

### 1. Data Cleaning

- Loads the raw sales dataset
- Handles formatting and cleanup
- Produces the cleaned dataset used by the rest of the project

Notebook:
- `notebooks/1_cleaning.ipynb`

### 2. Exploratory Data Analysis

- Sales trend analysis across years and months
- Model-level and regional sales comparison
- EV adoption trend analysis
- Fuel price and macroeconomic relationship checks
- Business insights and strategic recommendations

Notebook:
- `notebooks/2_EDA.ipynb`

### 3. Forecasting

- Train/test forecasting workflow
- Exponential Smoothing, ARIMA, and Prophet comparison
- 24-month forward forecast

Notebook:
- `notebooks/3_Forcasting.ipynb`

## Key Insights

- Global BMW sales rise from `2.77M` units in `2018` to `3.36M` units in `2025`.
- Sales are seasonal, with stronger months such as `March`, `June`, `September`, and `December`.
- SUVs are the largest sales driver, contributing about `37.6%` of total unit volume.
- EV models already contribute about `25.5%` of total units sold.
- China is the largest region, but sales are broadly balanced across major markets.
- `BEV_Share` rises from about `2.1%` to `19.4%`, showing strong electrification momentum.
- Higher fuel prices are strongly associated with higher EV adoption.
- Revenue is driven more by sales volume than by regional pricing differences.

## Forecasting Results

Based on the saved holdout evaluation in the forecasting notebook:

- `Exponential Smoothing` performs best with the lowest error
- `ARIMA` ranks second
- `Prophet` is useful for trend and seasonality visualization, but is not the best-performing model in this notebook

Saved model comparison:

- `Exponential Smoothing`: `MAE ≈ 22,187`, `RMSE ≈ 27,416`
- `ARIMA`: `MAE ≈ 23,093`, `RMSE ≈ 30,665`
- `Prophet`: `MAE ≈ 33,830`, `RMSE ≈ 40,326`

Forecast takeaway:

- Sales are projected to remain broadly stable over the next `24` months with recurring seasonal fluctuations.

## Strategic Recommendations

### EV Strategy

- Increase EV production capacity because `BEV_Share` rises sharply across the dataset period.
- Focus EV campaigns on markets that are more sensitive to fuel-price changes.
- Expand the EV SUV lineup because SUVs lead demand and EV adoption is growing.

### Product Strategy

- Continue investing in SUV models because they are the strongest volume segment.
- Strengthen the EV portfolio because it already represents a meaningful share of total units sold.
- Plan launches and promotions around stronger seasonal demand windows.

### Regional Strategy

- Maintain a balanced global market approach because performance is diversified across regions.
- Strengthen China selectively because it is the single largest regional contributor.
- Avoid overstating Europe as the EV leader, since this dataset does not show a meaningful gap by region.

### Pricing Strategy

- Prioritize volume growth over aggressive regional price differentiation.
- Preserve premium positioning while scaling sales.
- Use targeted incentives by model or season instead of broad price cuts.

## Interactive Dashboard

The project includes a `Streamlit` dashboard for interactive exploration of:

- sales trends
- annual and monthly seasonality
- EV adoption
- regional sales and revenue comparison

Dashboard file:

- `dashboard.py`

Run locally:

```bash
cd BMW_global_automotive_sales
streamlit run dashboard.py
```

## How To Run

If you want to reproduce the project locally, install the main dependencies and then open the notebooks or run the dashboard.

Example:

```bash
cd BMW_global_automotive_sales
pip install -r requirements.txt
streamlit run dashboard.py
```

## Limitations

- The dataset does not contain negative GDP growth periods, so no strong conclusion can be made about sales drops during recessions.
- Regional BEV differences are small in this data, so any claim that one region clearly leads EV adoption should be treated cautiously.
- Forecasting notebook results are based on the current saved run and should be revalidated in a fully configured environment before production use.

## Advanced Layer

This project includes one advanced layer: an interactive `Streamlit` dashboard that makes the analysis easier to explore and present on GitHub or during interviews.
