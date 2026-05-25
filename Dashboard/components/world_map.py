import plotly.express as px


def create_world_map(

    df,

    metric_column:str,

    year:int,

    title:str
):
    
    filtered_df = df[
        df["Year"] == year
    ]

    filtered_df = filtered_df.dropna(

        subset=[
            "ISO3",
            metric_column
        ]
    )

    fig = px.choropleth(

        filtered_df,

        locations="ISO3",

        color=metric_column,

        hover_name="Country",

        hover_data={
            metric_column: ":,.2f"
        },

        color_continuous_scale="Viridis",

        projection="natural earth",

        title=title
    )

    fig.update_layout(

        height=550,

        margin=dict(
            l=0,
            r=0,
            t=50,
            b=0
        )
    )

    return fig