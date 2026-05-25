import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# ECONOMY DASHBOARD
# ============================================

def render_economy_dashboard(df):

    st.subheader("📈 Economy Dashboard")

    st.markdown("---")

    # ============================================
    # KPI CARDS
    # ============================================

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="GDP",
            label="GDP"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="GDP_Per_Capita",
            label="GDP Per Capita"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Inflation",
            label="Inflation"
        )

    with kpi4:

        render_kpi_card(
            df=df,
            metric="Unemployment",
            label="Unemployment"
        )

    st.markdown("---")

    # ============================================
    # FIRST ROW
    # ============================================

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="GDP",
            title="GDP Over Time",
            key="gdp_chart"
        )

        create_line_chart(
            df=df,
            metric="Inflation",
            title="Inflation Over Time",
            key="inflation_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="GDP_Per_Capita",
            title="GDP Per Capita Over Time",
            key="gdp_per_capita_chart"
        )

        create_line_chart(
            df=df,
            metric="Unemployment",
            title="Unemployment Over Time",
            key="unemployment_chart"
        )

    # ============================================
    # SECOND ROW
    # ============================================

    col3, col4 = st.columns(2)

    with col3:

        create_line_chart(
            df=df,
            metric="Interest_Rate",
            title="Interest Rate Over Time",
            key="interest_rate_chart"
        )

        create_line_chart(
            df=df,
            metric="FDI",
            title="FDI Over Time",
            key="fdi_chart"
        )

    with col4:

        create_line_chart(
            df=df,
            metric="Forex_Reserves",
            title="Forex Reserves Over Time",
            key="forex_reserves_chart"
        )

        create_line_chart(
            df=df,
            metric="Current_Account_Balance",
            title="Current Account Balance Over Time",
            key="current_account_balance_chart"
        )