# nest_monitor/worker.py
import anvil.server


@anvil.server.callable
def fetch_nest_temperature(save=True):
    """
    Get temperature from Nest thermostat, save to database, cleanup old records.

    Args:
        save (bool): If True, save the temperature record to the database.

    Returns:
        str: The current temperature from the Nest thermostat, rounded to the nearest integer.
    """
    from . import auth
    from . import thermostat
    from ..utils import database

    try:
        credentials = auth.setup_nest_credentials()
        access_token = auth.get_access_token(credentials)
        temperature = thermostat.read_temperature(access_token)
        if not save:
            return str(round(temperature))
        database.save_temperature(round(temperature, 2))
        database.remove_old_temperature_records()

    except Exception as e:
        print(f"Error collecting temperature data: {e}")
        pass
