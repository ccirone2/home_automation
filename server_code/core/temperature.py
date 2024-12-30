# core/temperature.py

from datetime import datetime, timedelta

import anvil.server

import _config
from api.nest import auth, thermostat
from data import database
from utils import to_central_naive


@anvil.server.callable
def fetch_nest_temperature(save=True):
  """
  Get temperature from Nest thermostat, save to database, cleanup old records.

  Args:
      save (bool): If True, save the temperature record to the database.

  Returns:
      str: The current temperature from the Nest thermostat, rounded to the nearest integer.
  """
  try:
    credentials = auth.setup_nest_credentials()
    access_token = auth.get_access_token(credentials)
    temperature = thermostat.read_temperature(access_token)

    if save:
      database.save_temperature(round(temperature, 2))
      database.remove_old_temperature_records()

    return str(round(temperature))

  except Exception as e:
    print(f"Error collecting temperature data: {e}")
    pass


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
  history = _config.HISTORY_EXTENDED if extend_range else _config.HISTORY_SHORT
  past = now - timedelta(days=history)
  records = database.get_temperature_records(past, now)

  # Convert timestamps to Central time and prepare data
  data = [
    {
      "timestamp": to_central_naive(row["timestamp"]),
      "temperature": row["temperature"],
    }
    for row in records
  ]

  return data, history
