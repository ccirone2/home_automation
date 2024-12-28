import anvil.server
from plotly import graph_objects as go


def temperature_chart():
    fig = go.Figure()
    # Plot data with custom styling
    fig.data = [
        # Main data scatter plot
        go.Scatter(
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            y=[58, 56, 65, 72, 75, 73, 71, 72, 71, 84, 80, 75, 72, 71],
            marker=dict(
                color="rgb(255, 255, 0)",
                size=4,
            ),
            line=dict(width=1),
            mode="lines+markers",
            hovertemplate="%{y}<extra></extra>",
        ),
        # Add horizontal line at y=65
        go.Scatter(
            x=[1, 14],  # Start and end of x-axis
            y=[65, 65],
            mode="lines",
            line=dict(
                color="rgba(255, 255, 255, 0.3)",
                dash="dot",
                width=1,
            ),
            hoverinfo="none",
            showlegend=False,
        ),
        # Add horizontal line at y=75
        go.Scatter(
            x=[1, 14],  # Start and end of x-axis
            y=[75, 75],
            mode="lines",
            line=dict(
                color="rgba(255, 255, 255, 0.3)",
                dash="dot",
                width=1,
            ),
            hoverinfo="none",
            showlegend=False,
        ),
    ]

    # Configure layout
    fig.layout.update(
        template="material_dark",
        modebar_remove=[
            "zoom",
            "pan",
            "select",
            "lasso2d",
            "zoomIn",
            "zoomOut",
            "autoScale",
            "resetScale",
            "toImage",
        ],
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
            visible=False,
            fixedrange=True,
            range=[1, 14],
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
            visible=False,
            fixedrange=True,
            range=[55, 85],
        ),
        dragmode=False,
    )

    return fig
