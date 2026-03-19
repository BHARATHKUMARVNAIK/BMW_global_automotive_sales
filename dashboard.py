from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="BMW Global Sales Dashboard",
    page_icon="BMW",
    layout="wide",
)

DATA_PATH = Path(__file__).parent / "data" / "bmw_global_sales_2018_2025_cleaned.csv"
MONTH_ORDER = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df["Month"] = pd.Categorical(df["Month"], categories=MONTH_ORDER, ordered=True)
    return df.sort_values("Date")


df = load_data()

st.title("BMW Global Automotive Sales Dashboard")
st.caption("Interactive view of sales trends, EV adoption, and regional performance from 2018 to 2025.")

with st.sidebar:
    st.header("Filters")
    year_range = st.slider(
        "Year range",
        min_value=int(df["Year"].min()),
        max_value=int(df["Year"].max()),
        value=(int(df["Year"].min()), int(df["Year"].max())),
    )
    selected_regions = st.multiselect(
        "Regions",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique()),
    )
    selected_models = st.multiselect(
        "Models",
        options=sorted(df["Model"].unique()),
        default=sorted(df["Model"].unique()),
    )

filtered = df[
    df["Year"].between(year_range[0], year_range[1])
    & df["Region"].isin(selected_regions)
    & df["Model"].isin(selected_models)
].copy()

if filtered.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

total_units = int(filtered["Units_Sold"].sum())
avg_bev_share = filtered["BEV_Share"].mean() * 100
total_revenue = filtered["Revenue_EUR"].sum()
top_region = (
    filtered.groupby("Region")["Units_Sold"].sum().sort_values(ascending=False).index[0]
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Units Sold", f"{total_units:,}")
col2.metric("Average BEV Share", f"{avg_bev_share:.1f}%")
col3.metric("Total Revenue", f"EUR {total_revenue:,.0f}")
col4.metric("Top Region", top_region)

st.markdown("## Sales Trends")
monthly_sales = (
    filtered.groupby("Date", as_index=False)["Units_Sold"].sum().sort_values("Date")
)
st.line_chart(monthly_sales.set_index("Date")["Units_Sold"], height=360)

trend_col, season_col = st.columns(2)

with trend_col:
    st.markdown("### Annual Sales")
    annual_sales = filtered.groupby("Year", as_index=False)["Units_Sold"].sum()
    st.bar_chart(annual_sales.set_index("Year")["Units_Sold"], height=320)

with season_col:
    st.markdown("### Seasonality by Month")
    month_sales = (
        filtered.groupby("Month", as_index=False)["Units_Sold"]
        .sum()
        .sort_values("Month")
    )
    st.bar_chart(month_sales.set_index("Month")["Units_Sold"], height=320)

st.markdown("## EV Adoption")
bev_col1, bev_col2 = st.columns(2)

with bev_col1:
    st.markdown("### BEV Share Over Time")
    bev_year = filtered.groupby("Year", as_index=False)["BEV_Share"].mean()
    bev_year["BEV_Share"] = bev_year["BEV_Share"] * 100
    st.line_chart(bev_year.set_index("Year")["BEV_Share"], height=320)

with bev_col2:
    st.markdown("### BEV Share by Region")
    bev_region = filtered.groupby("Region", as_index=False)["BEV_Share"].mean()
    bev_region["BEV_Share"] = bev_region["BEV_Share"] * 100
    st.bar_chart(bev_region.set_index("Region")["BEV_Share"], height=320)

st.markdown("## Regional Comparison")
region_col1, region_col2 = st.columns(2)

with region_col1:
    st.markdown("### Units Sold by Region")
    region_sales = (
        filtered.groupby("Region", as_index=False)["Units_Sold"]
        .sum()
        .sort_values("Units_Sold", ascending=False)
    )
    st.bar_chart(region_sales.set_index("Region")["Units_Sold"], height=320)

with region_col2:
    st.markdown("### Revenue by Region")
    region_revenue = (
        filtered.groupby("Region", as_index=False)["Revenue_EUR"]
        .sum()
        .sort_values("Revenue_EUR", ascending=False)
    )
    st.bar_chart(region_revenue.set_index("Region")["Revenue_EUR"], height=320)

st.markdown("## Dashboard Notes")
st.write(
    "- Use the sidebar to isolate specific years, regions, or models.\n"
    "- The BEV charts are based on average `BEV_Share` within the selected slice.\n"
    "- Revenue is displayed in EUR using the cleaned dataset values."
)
