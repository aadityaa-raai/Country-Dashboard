import streamlit as st
import plotly.express as px


# ============================================
# CHECK DATA AVAILABILITY
# ============================================

def has_sufficient_data(
    df,
    metric,
    threshold=0.5
):

    total_rows = len(df)

    available_rows = df[metric].notna().sum()

    availability_ratio = available_rows / total_rows

    return availability_ratio >= threshold


# ============================================
# DETERMINE NUMBER FORMAT
# ============================================

def get_axis_format(metric):

    percentage_metrics = [
        "Inflation",
        "Unemployment",
        "Interest_Rate",
        "Population_Growth",
        "Urbanization",
        "Trade_Percent_GDP",
        "Renewable_Energy",
        "Electricity_Access",
        "Military_Percent_GDP"
    ]

    if metric in percentage_metrics:

        return ".2f"

    return "~s"


# ============================================
# LINE CHART
# ============================================

def create_line_chart(
    df,
    metric,
    title=None,
    threshold=0.5,
    key=None
):

    # ============================================
    # DATA AVAILABILITY CHECK
    # ============================================

    if not has_sufficient_data(df, metric, threshold):

        st.warning(
            f"⚠️ Insufficient data available for {metric.replace('_', ' ')}"
        )

        return


    # ============================================
    # CREATE CHART
    # ============================================

    fig = px.line(
        df,
        x="Year",
        y=metric,
        color="Country",
        markers=True,
        title=title
    )

    fig.update_layout(
        hovermode="x unified",
        xaxis_title="Year",
        yaxis_title=metric.replace("_", " "),
        height=500
    )

    fig.update_yaxes(
        tickformat=get_axis_format(metric)
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key=key
    )
