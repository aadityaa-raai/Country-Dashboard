import streamlit as st

from components.charts import create_line_chart
from components.kpi_cards import render_kpi_card


# ============================================
# TECHNOLOGY DASHBOARD
# ============================================

def render_technology_dashboard(df):

    st.subheader("💻 Technology Dashboard")

    st.markdown("---")

    # ============================================
    # KPI CARDS
    # ============================================

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        render_kpi_card(
            df=df,
            metric="Internet_Users",
            label="Internet Users"
        )

    with kpi2:

        render_kpi_card(
            df=df,
            metric="Mobile_Subscriptions",
            label="Mobile Subscriptions"
        )

    with kpi3:

        render_kpi_card(
            df=df,
            metric="Broadband_Subscriptions",
            label="Broadband Subscriptions"
        )

    with kpi4:

        render_kpi_card(
            df=df,
            metric="RND_Expenditure",
            label="R&D Expenditure"
        )

    st.markdown("---")

    # ============================================
    # FIRST ROW
    # ============================================

    col1, col2 = st.columns(2)

    with col1:

        create_line_chart(
            df=df,
            metric="Internet_Users",
            title="Internet Users Over Time",
            key="internet_users_chart"
        )

        create_line_chart(
            df=df,
            metric="Broadband_Subscriptions",
            title="Broadband Subscriptions Over Time",
            key="broadband_subscriptions_chart"
        )

    with col2:

        create_line_chart(
            df=df,
            metric="Mobile_Subscriptions",
            title="Mobile Subscriptions Over Time",
            key="mobile_subscriptions_chart"
        )

        create_line_chart(
            df=df,
            metric="Secure_Servers",
            title="Secure Servers Over Time",
            key="secure_servers_chart"
        )

    # ============================================
    # SECOND ROW
    # ============================================

    create_line_chart(
        df=df,
        metric="RND_Expenditure",
        title="R&D Expenditure Over Time",
        key="rnd_expenditure_chart"
    )
