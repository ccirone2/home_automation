import anvil.http


def fetch_outdoor_temp(location):
    """
    Fetch the current outdoor temperature for a given location.

    Args:
        location (dict): A dictionary with 'lat' and 'lon' keys for latitude and longitude.

    Returns:
        str: The current outdoor temperature in Fahrenheit, rounded to the nearest integer.
    """
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={location['lat']}&lon={location['lon']}&appid={anvil.secrets.get_secret('open_weather_api_key')}&units=imperial"
    response = anvil.http.request(API_URL, json=True)
    outdoor_temp = response["main"]["temp"]
    return str(round(outdoor_temp))
