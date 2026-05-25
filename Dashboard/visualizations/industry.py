import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# INDUSTRY DASHBOARD
# ============================================

def render_industry_dashboard(df):

    st.subheader("🏭 Industry Dashboard")

    st.markdown("---")

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="Agriculture",
            label="Agriculture"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="Industry",
            label="Industry"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Services",
            label="Services"
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="Agriculture",
            title="Agriculture Over Time",
            key="agriculture_chart"
        )

        create_line_chart(
            df=df,
            metric="Industry",
            title="Industry Over Time",
            key="industry_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="Services",
            title="Services Over Time",
            key="services_chart"
        )
