# nest_monitor/worker.py
import anvil.server


@anvil.server.callable
def collect_temperature_data():
    from . import auth
    from . import thermostat
    from . import db_utils as database

    try:
        credentials = auth.setup_nest_credentials()
        access_token = auth.get_access_token(credentials)
        temperature = thermostat.get_temperature(access_token)
        database.save_temperature_reading(temperature)
        database.cleanup_old_readings()

    except Exception as e:
        print(f"Error collecting temperature data: {e}")
        pass


if __name__ == "__main__":
    """
    Connects to Anvil app using uplink and calls a server function
    """
    import os

    uplink_key = os.environ["ANVIL_UPLINK_KEY"]

    try:
        anvil.server.connect(uplink_key)
        anvil.server.call("collect_temperature_data")

    finally:
        anvil.server.disconnect()
