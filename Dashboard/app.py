import streamlit as st
import pandas as pd
import json
import plotly.express as px
from visualizations.economy import render_economy_dashboard
from visualizations.demographics import render_demographics_dashboard
from visualizations.trade import render_trade_dashboard
from visualizations.environment import render_environment_dashboard
from visualizations.industry import render_industry_dashboard
from visualizations.military import render_military_dashboard
from visualizations.technology import render_technology_dashboard


# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Country Intelligence Dashboard",
    page_icon="🌍",
    layout="wide"
)


# ============================================
# LOAD DATA REGISTRY
# ============================================

@st.cache_data
def load_data_registry(registry_path):

    with open(registry_path, "r") as file:

        registry = json.load(file)

    return registry


# ============================================
# LOAD SECTION DATA
# ============================================

@st.cache_data
def load_section_data(file_path):

    df = pd.read_csv(file_path)

    return df


# ============================================
# FILTER SINGLE COUNTRY
# ============================================

def filter_country(df, country):

    return df[df["Country"] == country]


# ============================================
# FILTER MULTIPLE COUNTRIES
# ============================================

def filter_countries(df, countries):

    return df[df["Country"].isin(countries)]


# ============================================
# FILTER YEAR RANGE
# ============================================

def filter_year_range(df, start_year, end_year):

    return df[
        (df["Year"] >= start_year)
        &
        (df["Year"] <= end_year)
    ]


# ============================================
# LOAD REGISTRY
# ============================================

DATA_REGISTRY_PATH = "artifacts/data/data_registry.json"

data_registry = load_data_registry(DATA_REGISTRY_PATH)


# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("🌍 Country Dashboard")


# --------------------------------------------
# SECTION SELECTOR
# --------------------------------------------

selected_section = st.sidebar.radio(
    "Select Dashboard Section",
    [
        "Economy",
        "Demographics",
        "Trade",
        "Technology",
        "Environment",
        "Industry",
        "Military"
    ]
)

# ============================================
# LOAD DATA
# ============================================

selected_file = data_registry[selected_section.lower()]

df = load_section_data(selected_file)
# --------------------------------------------
# LOAD COUNTRY OPTIONS
# --------------------------------------------

all_countries = sorted(
    df["Country"].dropna().unique().tolist()
)


# --------------------------------------------
# COUNTRY SELECTOR
# --------------------------------------------

country = st.sidebar.selectbox(
    "Select Country",
    options=all_countries,
    index=all_countries.index("India")
    if "India" in all_countries else 0
)


# --------------------------------------------
# COMPARE MODE
# --------------------------------------------

compare_mode = st.sidebar.toggle(
    "Enable Compare Mode"
)

compare_countries = []

if compare_mode:

    compare_countries = st.sidebar.multiselect(
        "Select Countries to Compare",
        options=all_countries,
        default=["India", "China"]
        if "China" in all_countries else [all_countries[0]],
        max_selections=3
    )

else:

    compare_countries = [country]


# --------------------------------------------
# YEAR RANGE
# --------------------------------------------

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=1960,
    max_value=2025,
    value=(2000, 2023)
)





# ============================================
# APPLY FILTERS
# ============================================

start_year, end_year = year_range

df = filter_year_range(
    df,
    start_year,
    end_year
)

df = filter_countries(
    df,
    compare_countries
)


# ============================================
# MAIN PAGE
# ============================================

st.title("🌍 Country Intelligence Dashboard")

st.markdown("---")

# ============================================
# VIEW MODE INFO
# ============================================

if compare_mode:

    st.info(
        f"Comparing: {' vs '.join(compare_countries)}"
    )

else:

    st.info(
        f"Viewing: {country}"
    )


# ============================================
# KPI PLACEHOLDERS
# ============================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Country",
        country
    )

with col2:

    st.metric(
        "Section",
        selected_section
    )

with col3:

    st.metric(
        "Rows Loaded",
        len(df)
    )


st.markdown("---")

# ============================================
# SECTION VISUALIZATIONS
# ============================================

if selected_section == "Economy":

    render_economy_dashboard(df)

elif selected_section == "Demographics":

    render_demographics_dashboard(df)

elif selected_section == "Trade":

    render_trade_dashboard(df)

elif selected_section == "Technology":

    render_technology_dashboard(df)

elif selected_section == "Environment":

    render_environment_dashboard(df)

elif selected_section == "Industry":

    render_industry_dashboard(df)

elif selected_section == "Military":

    render_military_dashboard(df)