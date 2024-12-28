from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from plotly import graph_objects as go

from . import charts


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.plot_1 = charts.temperature()

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
