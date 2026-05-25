import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# TRADE DASHBOARD
# ============================================

def render_trade_dashboard(df):

    st.subheader("🌐 Trade Dashboard")

    st.markdown("---")

    # ============================================
    # KPI CARDS
    # ============================================

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="Exports",
            label="Exports"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="Imports",
            label="Imports"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Trade_Percent_GDP",
            label="Trade % GDP"
        )

    with kpi4:

        render_kpi_card(
            df=df,
            metric="High_Tech_Exports",
            label="High Tech Exports"
        )

    st.markdown("---")

    # ============================================
    # FIRST ROW
    # ============================================

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="Exports",
            title="Exports Over Time",
            key="exports_chart"
        )

        create_line_chart(
            df=df,
            metric="Trade_Percent_GDP",
            title="Trade % GDP Over Time",
            key="trade_percent_gdp_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="Imports",
            title="Imports Over Time",
            key="imports_chart"
        )

        create_line_chart(
            df=df,
            metric="High_Tech_Exports",
            title="High Tech Exports Over Time",
            key="high_tech_exports_chart"
        )
