from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from plotly import graph_objects as go


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Plot data with custom styling
    self.plot_1.data = [
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
    self.plot_1.layout.update(
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
    self.plot_1.layout.height = "100%"
    self.plot_1.layout.width = "100%"
    self.plot_1.layout.align = "stretch"

  def button_1_on_click(self, **event_args):
    anvil.server.call("control_switch", "switch_1", True)

  def button_1_off_click(self, **event_args):
    anvil.server.call("control_switch", "switch_1", False)

  def button_2_on_click(self, **event_args):
    anvil.server.call("control_switch", "switch_2", True)

  def button_2_off_click(self, **event_args):
    anvil.server.call("control_switch", "switch_2", False)

  def button_3_on_click(self, **event_args):
    anvil.server.call("control_switch", "switch_3", True)

  def button_3_off_click(self, **event_args):
    anvil.server.call("control_switch", "switch_3", False)
