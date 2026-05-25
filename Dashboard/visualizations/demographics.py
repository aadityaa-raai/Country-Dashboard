import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# DEMOGRAPHICS DASHBOARD
# ============================================

def render_demographics_dashboard(df):

    st.subheader("👥 Demographics Dashboard")

    st.markdown("---")

    # ============================================
    # KPI CARDS
    # ============================================

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="Population",
            label="Population"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="Population_Growth",
            label="Population Growth"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Life_Expectancy",
            label="Life Expectancy"
        )

    with kpi4:

        render_kpi_card(
            df=df,
            metric="Literacy_Rate",
            label="Literacy Rate"
        )

    st.markdown("---")

    # ============================================
    # FIRST ROW
    # ============================================

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="Population",
            title="Population Over Time",
            key="population_chart"
        )

        create_line_chart(
            df=df,
            metric="Population_Density",
            title="Population Density Over Time",
            key="population_density_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="Population_Growth",
            title="Population Growth Over Time",
            key="population_growth_chart"
        )

        create_line_chart(
            df=df,
            metric="Urbanization",
            title="Urbanization Over Time",
            key="urbanization_chart"
        )

    # ============================================
    # SECOND ROW
    # ============================================

    col3, col4 = st.columns(2)

    with col3:

        create_line_chart(
            df=df,
            metric="Life_Expectancy",
            title="Life Expectancy Over Time",
            key="life_expectancy_chart"
        )

        create_line_chart(
            df=df,
            metric="Birth_Rate",
            title="Birth Rate Over Time",
            key="birth_rate_chart"
        )

    with col4:

        create_line_chart(
            df=df,
            metric="Literacy_Rate",
            title="Literacy Rate Over Time",
            key="literacy_rate_chart"
        )

        create_line_chart(
            df=df,
            metric="Death_Rate",
            title="Death Rate Over Time",
            key="death_rate_chart"
        )
