from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_on_click(self, **event_args):
    anvil.server.call("switch_1_on")

  def button_1_off_click(self, **event_args):
    anvil.server.call("switch_1_off")

  def button_2_on_click(self, **event_args):
    anvil.server.call("switch_2_on")

  def button_2_off_click(self, **event_args):
    anvil.server.call("switch_2_off")

  def button_3_on_click(self, **event_args):
    anvil.server.call("switch_3_on")

  def button_3_off_click(self, **event_args):
    anvil.server.call("switch_3_off")
