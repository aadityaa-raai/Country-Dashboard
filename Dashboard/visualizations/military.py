import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# MILITARY DASHBOARD
# ============================================

def render_military_dashboard(df):

    st.subheader("🛡️ Military Dashboard")

    st.markdown("---")

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="Military_Expenditure",
            label="Military Expenditure"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="Military_Percent_GDP",
            label="Military % GDP"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Armed_Forces_Personnel",
            label="Armed Forces Personnel"
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="Military_Expenditure",
            title="Military Expenditure Over Time",
            key="military_expenditure_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="Military_Percent_GDP",
            title="Military % GDP Over Time",
            key="military_percent_gdp_chart"
        )

    create_line_chart(
        df=df,
        metric="Armed_Forces_Personnel",
        title="Armed Forces Personnel Over Time",
        key="armed_forces_personnel_chart"
    )
