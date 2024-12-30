# nest_monitor/db_utils.py
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta


def save_temperature(temperature):
    """
    Save a temperature record to the database.

    Args:
        temperature (float): The temperature record to save.
    """
    app_tables.temperature_records.add_row(timestamp=datetime.now(), temperature=temperature)


def remove_old_temperature_records():
    """
    Remove temperature records older than 7 days from the database.
    """
    week_ago = datetime.now() - timedelta(days=7)
    old_rows = app_tables.temperature_records.search(timestamp=q.less_than(week_ago))
    for row in old_rows:
        row.delete()


def get_temperature_records(start_time, end_time):
    """
    Get temperature records between start_time and end_time.

    Args:
        start_time (datetime): The start time for the query.
        end_time (datetime): The end time for the query.

    Returns:
        list: A list of temperature records.
    """
    return app_tables.temperature_records.search(timestamp=q.between(start_time, end_time))
