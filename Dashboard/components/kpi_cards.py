import streamlit as st


# ============================================
# FORMAT LARGE NUMBERS
# ============================================

def format_number(value):

    if value is None:

        return "N/A"

    if abs(value) >= 1_000_000_000_000:
        return f"{value / 1_000_000_000_000:.2f}T"

    elif abs(value) >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"

    elif abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"

    elif abs(value) >= 1_000:
        return f"{value / 1_000:.2f}K"

    else:
        return f"{value:.2f}"


# ============================================
# GET LATEST VALUE
# ============================================

def get_latest_value(df, metric):

    metric_df = df[
        df[metric].notna()
    ].sort_values("Year")

    if metric_df.empty:

        return None

    return metric_df.iloc[-1][metric]


# ============================================
# GET DELTA VALUE
# ============================================

def get_delta_value(df, metric):

    metric_df = df[
        df[metric].notna()
    ].sort_values("Year")

    if len(metric_df) < 2:

        return None

    first_value = metric_df.iloc[0][metric]

    latest_value = metric_df.iloc[-1][metric]

    delta = latest_value - first_value

    return delta


# ============================================
# RENDER KPI CARD
# ============================================

def render_kpi_card(
    df,
    metric,
    label=None
):

    latest_value = get_latest_value(df, metric)

    delta_value = get_delta_value(df, metric)

    formatted_value = format_number(latest_value)

    formatted_delta = (
        format_number(delta_value)
        if delta_value is not None
        else None
    )

    inverse_metrics = [
        "Inflation",
        "Unemployment",
        "Interest_Rate",
        "Air_Pollution",
        "Death_Rate"
    ]

    delta_color = (
        "inverse"
        if metric in inverse_metrics
        else "normal"
    )

    st.metric(
    label=label or metric.replace("_", " "),
    value=formatted_value,
    delta=formatted_delta,
    delta_color=delta_color
)