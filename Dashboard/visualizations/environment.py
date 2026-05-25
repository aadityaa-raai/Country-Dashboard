import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# ENVIRONMENT DASHBOARD
# ============================================

def render_environment_dashboard(df):

    st.subheader("🌱 Environment Dashboard")

    st.markdown("---")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="Air_Pollution",
            label="Air Pollution"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="Forest_Area",
            label="Forest Area"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Renewable_Energy",
            label="Renewable Energy"
        )

    with kpi4:

        render_kpi_card(
            df=df,
            metric="Electricity_Access",
            label="Electricity Access"
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="Air_Pollution",
            title="Air Pollution Over Time",
            key="air_pollution_chart"
        )

        create_line_chart(
            df=df,
            metric="Renewable_Energy",
            title="Renewable Energy Over Time",
            key="renewable_energy_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="Forest_Area",
            title="Forest Area Over Time",
            key="forest_area_chart"
        )

        create_line_chart(
            df=df,
            metric="Electricity_Access",
            title="Electricity Access Over Time",
            key="electricity_access_chart"
        )
