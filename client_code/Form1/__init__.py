from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .charts import temperature_history_figure


class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.location = {"lat": 37.084229, "lon": -94.513283}  # For OpenWeather API call
        self.plot_1.figure = temperature_history_figure()

        # Set the indoor and outdoor temperature display
        self.timer_1_tick()

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

    def toggle_icon_button_1_click(self, **event_args):
        if self.toggle_icon_button_1.selected:
            self.plot_1.figure = temperature_history_figure(extend_range=True)
            return
        self.plot_1.figure = temperature_history_figure()

    def timer_1_tick(self, **event_args):
        indoor_temp, outdoor_temp = anvil.server.call("refresh_page", self.location)
        self.text_4.text = indoor_temp + " °F"
        self.text_5.text = outdoor_temp + " °F"
