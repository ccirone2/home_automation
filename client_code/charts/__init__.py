import anvil.server
# This is a package.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#    from . import charts
#    charts.temperature()


def temperature():
  # Plot data with custom styling
  data = [
    # Main data scatter plot
    go.Scatter(
      x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
      y=[51, 56, 65, 72, 75, 73, 71, 72, 71, 86, 80, 75, 72, 71],
      marker=dict(color="rgb(255, 255, 0)"),
      mode="lines+markers",
      hovertemplate="%{y}<extra></extra>",
    ),
    # Add horizontal line at y=65
    go.Scatter(
      x=[1, 14],  # Start and end of x-axis
      y=[65, 65],
      mode="lines",
      line=dict(color="rgba(255, 255, 255, 0.3)", dash="dash"),
      hoverinfo="none",
      showlegend=False,
    ),
    # Add horizontal line at y=75
    go.Scatter(
      x=[1, 14],  # Start and end of x-axis
      y=[75, 75],
      mode="lines",
      line=dict(color="rgba(255, 255, 255, 0.3)", dash="dash"),
      hoverinfo="none",
      showlegend=False,
    ),
  ]

  # Configure layout
  layout.update(
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
    margin=dict(l=20, r=20, t=20, b=20),
    autosize=True,
    showlegend=False,
    xaxis=dict(
      showgrid=False,
      zeroline=False,
      showline=False,
      showticklabels=False,
      visible=False,
      fixedrange=True,
    ),
    yaxis=dict(
      showgrid=False,
      zeroline=False,
      showline=False,
      range=[50, 90],
      fixedrange=True,
    ),
    dragmode=False,
  )

  # Configure plot component to fill container
  layout.height = "100%"
  layout.width = "100%"
  layout.align = "stretch"
