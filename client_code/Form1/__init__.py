from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def switch_1_change(self, **event_args):
    """This method is called when the state of the component is changed."""
    if self.switch_1.selected:
      anvil.server.call("switch_1_on")
      return
    anvil.server.call("switch_1_off")

  def switch_2_change(self, **event_args):
    """This method is called when the state of the component is changed."""
    if self.switch_2.selected:
      anvil.server.call("switch_2_on")
      return
    anvil.server.call("switch_2_off")

  def switch_3_change(self, **event_args):
    """This method is called when the state of the component is changed."""
    if self.switch_3.selected:
      anvil.server.call("switch_3_on")
      return
    anvil.server.call("switch_3_off")



