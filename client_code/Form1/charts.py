import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from plotly import graph_objects as go
from datetime import datetime, timedelta


def temperature_chart():
  # Get last 14 readings from the database
  readings = app_tables.temperature_readings.search(
    tables.order_by("timestamp", ascending=False)
  )
  readings = list(readings)[:14]  # Get last 14 readings
  readings.reverse()  # Reverse to show oldest first

  # Extract timestamps and temperatures
  x_values = list(range(1, len(readings) + 1))  # Keep the same x-axis numbering
  y_values = [row["temperature"] for row in readings]

  fig = go.Figure()

  # Plot data with custom styling
  fig.data = [
    # Main data scatter plot
    go.Scatter(
      x=x_values,
      y=y_values,
      marker=dict(
        color="rgb(255, 255, 0)",
        size=4,
      ),
      line=dict(width=1),
      mode="lines+markers",
      hovertemplate="%{y:.1f}°F<extra></extra>",
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

  # Find min and max temperatures to adjust y-axis range
  min_temp = min(y_values) if y_values else 55
  max_temp = max(y_values) if y_values else 85
  y_range_min = min(min_temp - 5, 55)  # At least 5 degrees below min temp
  y_range_max = max(max_temp + 5, 85)  # At least 5 degrees above max temp

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
      range=[y_range_min, y_range_max],
    ),
    dragmode=False,
  )

  return fig
