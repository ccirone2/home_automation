import anvil.http


@anvil.server.callable
def get_outdoor_temp(location):
  API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={location['lat']}&lon={location['lon']}&appid={anvil.secrets.get_secret('open_weather_api_key')}&units=imperial"
  response = anvil.http.request(API_URL, json=True)
  outdoor_temp = response["main"]["temp"]
  return str(round(outdoor_temp))
