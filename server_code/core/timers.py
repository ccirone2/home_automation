# core/timers.py

import anvil.server

from api.openweather import weather
from .temperature import fetch_nest_temperature


@anvil.server.callable
def refresh_page(location):
    """
    Refresh the page to update the temperature records.

    Args:
        location (dict): A dictionary with 'lat' and 'lon' keys for latitude and longitude.

    Returns:
        tuple: The indoor and outdoor temperatures.
    """
    indoor_temp = fetch_nest_temperature(save=False)
    outdoor_temp = weather.fetch_outdoor_temp(location)

    return indoor_temp, outdoor_temp
