# nest_monitor/thermostat.py
import anvil.secrets
import requests



def get_temperature(access_token):
  """Get current temperature from the Nest thermostat"""
  project_id = anvil.secrets.get_secret("google-cloud-project-id")
  device_id = anvil.secrets.get_secret("nest-device-id")
  url = f"https://smartdevicemanagement.googleapis.com/v1/enterprises/{project_id}/devices/{device_id}"
  headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
  }

  response = requests.get(url, headers=headers)
  data = response.json()

  temp_celsius = data["traits"]["sdm.devices.traits.Temperature"][
    "ambientTemperatureCelsius"
  ]
  return (temp_celsius * 9 / 5) + 32
