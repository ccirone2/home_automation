import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from plotly import graph_objects as go

from datetime import datetime, timedelta


def temperature_history_figure(extend_range=False):
  # Get readings from the server
  data, history = anvil.server.call("get_temperature_history", extend_range)

  # Extract timestamps and temperatures
  x_values = [row["timestamp"] for row in data]
  y_values = [row["temperature"] for row in data]

  fig = go.Figure()

  # Plot range from past to now
  now = datetime.now()
  past = now - timedelta(days=history)

  # Plot data with custom styling
  fig.data = [
    # Main data scatter plot
    go.Scatter(
      x=x_values,
      y=[round(y) for y in y_values],
      marker=dict(
        color="rgba(33, 183, 126, 1)",  # 21B77E
        size=4,
      ),
      line=dict(width=2),
      mode="lines",
      hovertemplate="%{y} °F<extra> %{x|%-I:%M %p}</extra>",
      hoverlabel=dict(
        bgcolor="rgba(28, 27, 31, 1)",
        bordercolor="rgba(225, 227, 223, 1)",
        # bgcolor="rgba(33, 183, 126, 0.8)",
        # bordercolor="rgba(28, 27, 31, 1)",
      ),
    ),
    # Add horizontal line at y=65
    go.Scatter(
      x=[past, now],
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
      x=[past, now],  # Start and end of x-axis
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
      showticklabels=True,
      visible=True,
      fixedrange=True,
      range=[past, now],
      type="date",
      tickformat="%-I %p",
      tickfont=dict(
        size=9,
        color="rgba(255, 255, 255, 0.4)",
      ),
      side="top",      
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
