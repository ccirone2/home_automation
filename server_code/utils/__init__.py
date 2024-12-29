# utils/__init__.py

import anvil.server

from datetime import datetime, timedelta
import pytz

from . import database

# Central time
central = pytz.timezone("America/Chicago")  # UTC-6/UTC-5 with DST


def to_central_naive(dt):
    """Convert any datetime to Central time and remove tz info"""

    # Convert to Central time then strip tz info
    return dt.astimezone(central).replace(tzinfo=None)


@anvil.server.callable
def get_temperature_data():
    """Get temperature data for the last 24 hours and convert timestamps to Central time"""
    now = datetime.now()
    yesterday = now - timedelta(hours=24)
    readings = database.get_temperature_readings(yesterday, now)

    # Convert timestamps to Central time and prepare data
    data = [
        {"timestamp": to_central_naive(row["timestamp"]), "temperature": row["temperature"]}
        for row in readings
    ]
    return data