# nest_monitor/worker.py
import anvil.server


@anvil.server.callable
def fetch_nest_temperature(save=True):
    """Get temperature from Nest thermostat, save to database, cleanup old records."""
    from . import auth
    from . import thermostat
    from ..utils import database

    try:
        credentials = auth.setup_nest_credentials()
        access_token = auth.get_access_token(credentials)
        temperature = thermostat.read_temperature(access_token)
        if not save:
            return str(round(temperature))
        database.save_temperature_reading(round(temperature, 2))
        database.cleanup_old_readings()

    except Exception as e:
        print(f"Error collecting temperature data: {e}")
        pass
