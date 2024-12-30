# utils/__init__.py

import anvil.server
from datetime import datetime, timedelta
import pytz

from . import database
from . import weather
from nest_monitor import fetch_nest_temperature

# Central time
CENTRAL_TZ = pytz.timezone("America/Chicago")  # UTC-6/UTC-5 with DST


def to_central_naive(dt):
    """Convert any datetime to Central time and remove tz info."""
    return dt.astimezone(CENTRAL_TZ).replace(tzinfo=None)


@anvil.server.callable
def get_temperature_history(extend_range=False):
    """
    Get temperature data for the last 24 hours and convert timestamps to Central time.

    Args:
        extend_range (bool): If True, extend the range to the last 3 days.

    Returns:
        list: A list of temperature records with timestamps in Central time.
    """
    now = datetime.now()
    history = timedelta(days=3) if extend_range else timedelta(days=1)
    past = now - history
    records = database.get_temperature_records(past, now)

    # Convert timestamps to Central time and prepare data
    return [
        {
            "timestamp": to_central_naive(row["timestamp"]),
            "temperature": row["temperature"],
        }
        for row in records
    ]


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
