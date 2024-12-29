# utils/__init__.py

import anvil.server
from datetime import datetime, timedelta
import pytz
from . import database

# Central time
CENTRAL_TZ = pytz.timezone("America/Chicago")  # UTC-6/UTC-5 with DST


def to_central_naive(dt):
  """Convert any datetime to Central time and remove tz info."""
  return dt.astimezone(CENTRAL_TZ).replace(tzinfo=None)


@anvil.server.callable
def get_temperature_data(extend_range=False):
  """Get temperature data for the last 24 hours and convert timestamps to Central time."""
  now = datetime.now()
  history = timedelta(days=3) if extend_range else timedelta(days=1)
  past = now - history
  readings = database.get_temperature_readings(past, now)

  # Convert timestamps to Central time and prepare data
  return [
    {
      "timestamp": to_central_naive(row["timestamp"]),
      "temperature": row["temperature"],
    }
    for row in readings
  ]
