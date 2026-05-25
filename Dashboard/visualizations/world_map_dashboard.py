import streamlit as st

from components.world_map import (
    create_world_map
)


def render_world_map_dashboard(df):

    metric_columns = [

        col for col in df.columns

        if col not in [
            "Country",
            "Country_Code",
            "ISO3",
            "Year"
        ]
    ]

    selected_metric = st.selectbox(

        "Select Metric",

        metric_columns
    )

    available_years = sorted(
        df["Year"].dropna().unique()
    )

    selected_year = st.selectbox(

        "Select Year",

        available_years,

        index=len(available_years)-1
    )

    fig = create_world_map(

        df=df,

        metric_column=selected_metric,

        year=selected_year,

        title=f"{selected_metric} ({selected_year})"
    )

    st.plotly_chart(

        fig,

        use_container_width=True
    )