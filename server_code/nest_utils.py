import requests
from datetime import datetime, timedelta
import time

import anvil.secrets
import anvil.tables
from anvil.tables import app_tables
import anvil.tables.query as q


@anvil.server.callable
def setup_nest_credentials():
  """
  Get OAuth2 credentials from Anvil Secrets.
  Assumes you've stored these secrets in your Anvil app:
  - nest_client_id
  - nest_client_secret
  - nest_refresh_token
  """
  return {
    "client_id": anvil.secrets.get_secret("nest_client_id"),
    "client_secret": anvil.secrets.get_secret("nest_client_secret"),
    "refresh_token": anvil.secrets.get_secret("nest_refresh_token"),
  }


def get_access_token(credentials):
  """Get a new access token using the refresh token"""
  token_url = "https://www.googleapis.com/oauth2/v4/token"
  data = {
    "client_id": credentials["client_id"],
    "client_secret": credentials["client_secret"],
    "refresh_token": credentials["refresh_token"],
    "grant_type": "refresh_token",
  }

  response = requests.post(token_url, data=data)
  return response.json()["access_token"]


def get_temperature(access_token):
  """Get the first Nest thermostat device ID"""
  project_id = anvil.secrets.get_secret("google-cloud-project-id")
  device_id = anvil.secrets.get_secret("nest-device-id")
  url = f"https://smartdevicemanagement.googleapis.com/v1/enterprises/{project_id}/devices/{device_id}"
  headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
  }

  response = requests.get(url, headers=headers)
  data = response.json()

  # Extract temperature from traits
  temp_celsius = data["traits"]["sdm.devices.traits.Temperature"][
    "ambientTemperatureCelsius"
  ]
  temp_fahrenheit = (temp_celsius * 9 / 5) + 32

  return temp_fahrenheit


@anvil.server.background_task
def collect_temperature_data():
  """
  Background task to collect temperature data every 20 minutes
  and store it in the Anvil database
  """
  while True:
    try:
      # Get credentials and authenticate
      credentials = setup_nest_credentials()
      access_token = get_access_token(credentials)

      # Get temperature and current timestamp
      temperature = get_temperature(access_token)
      timestamp = datetime.now()

      # Store in Anvil database
      app_tables.temperature_readings.add_row(
        timestamp=timestamp, temperature=temperature
      )

      # Clean up old data (keep only last 7 days)
      week_ago = datetime.now() - timedelta(days=7)
      old_rows = app_tables.temperature_readings.search(timestamp=q.less_than(week_ago))
      for row in old_rows:
        row.delete()

      # Wait 20 minutes before next reading
      time.sleep(10)  # 10 minutes = 600 seconds

    except Exception as e:
      print(f"Error collecting temperature data: {str(e)}")
      time.sleep(10)  # Wait 1 minute before retrying if there's an error


# Start the background task when the server module loads
anvil.server.call("collect_temperature_data")
